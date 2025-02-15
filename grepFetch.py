import asyncio

import json
import time
from OctaveEngine._innertube import InnerTube
from colorama import Fore, Back

class GrepFetcher:
    def __init__(self, deepSearchEnabled=False, debugMode=(True, 0)):
        self.grapeDeepSearchEnabled = deepSearchEnabled
        self.debugMode = debugMode
        self.loggingEnabled, self.debug_level = debugMode

    def set_debug_mode(self, debugMode):
        self.debugMode = debugMode
        self.loggingEnabled, self.debug_level = debugMode

    async def _fetch_audio_info(self, audio_client, video_id):
        try:
            if self.debug_level > 2:
                print(f'Fetching audio info for {video_id}...')

            audio_info = await asyncio.to_thread(audio_client.player, video_id)
            playability_status = audio_info["playabilityStatus"]["status"]

            if playability_status != 'OK':
                print(Fore.RED + f"Playability status not OK, check 'audio_info.json' ... "+ Fore.RESET)
                with open('audio_info.json', 'w') as f1:
                    json.dump(audio_info, f1, indent=4)
                
                return -1

            formats = audio_info['streamingData']['adaptiveFormats']
            if self.debug_level > 2:               
                print(f'Found {len(formats)} formats ... ')
                print(f'Filtering for audio-only formats ... ')

            suitable_audio_urls = [
                format for format in formats if 'audio' in format['mimeType']
            ]
            if self.debug_level > 2:
                print(f'Done, Found {len(suitable_audio_urls)} audio formats')

            return suitable_audio_urls
        
        except Exception as e:
            with open('audio_info.json', 'w') as f1:
                json.dump(audio_info, f1, indent=4)

            print(f'Could not fetch audio info, Error: {e}')
            return []

    async def _grape_fetch_sanitizedata(self, contents, query_correction_info, audio_client):
        scraped = []

        async def process_content(i):
            if self.debug_level > 2:
                print(f'[{i+1}] Fetching title, subtitle, thumbnails, video Id ...')

            data = {}
            content = contents[i]['musicTwoColumnItemRenderer']
            data['title'] = content['title']['runs'][0]['text']
            sub = content['subtitle']
            data['artist'] = sub['runs'][0]['text']
            data['formattedDuration'] = sub['runs'][2]['text']
            data['plays'] = sub['runs'][4]['text']

            corrected_query = query_correction_info.get('correctedQuery') if query_correction_info else None
            if corrected_query:
                corrected_query_parts = [
                    {'text': q['text'], 'isCorrected': q.get('italics', False)}
                    for q in corrected_query['runs']
                ]
                corrected_query_string = ''.join(q['text'] for q in corrected_query['runs'])
                data['queryCorrection'] = corrected_query_string, corrected_query_parts
            else:
                data['queryCorrection'] = '', []

            data['thumbnails'] = content['thumbnail']['musicThumbnailRenderer']['thumbnail']['thumbnails']
            data['id'] = content['navigationEndpoint']['watchEndpoint']['videoId']

            # Fetch audio info asynchronously
            urls = await self._fetch_audio_info(audio_client, data['id'])
            # if urls != -1 or urls != []:
            data['streamUrls'] = urls

            if self.debug_level > 2:
                print('Done.')

            return data
            

        tasks = [process_content(i) for i in range(len(contents))]
        scraped = await asyncio.gather(*tasks)
        scraped = [item for item in scraped if item['streamUrls'] != -1]
        if self.debug_level > 1:
            print(Fore.MAGENTA + f'-> Finally fetched {len(scraped)} results, Now filtering ...' + Fore.RESET)

        ids = set()
        sorted_data = []
        for item in scraped:
            if item['id'] not in ids:
                ids.add(item['id'])
                sorted_data.append(item)

        return sorted_data

    async def _grape_fetch_search_content(self, query, search_client, continuation_token=None):
        if not self.grapeDeepSearchEnabled:
            if continuation_token:
                response = search_client.search(continuation=continuation_token)
                mappings = response['continuationContents']['musicShelfContinuation']
                contents = mappings['contents']
            else:
                response = search_client.search(query)
                mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
                get = mappings[1].get('musicShelfRenderer', None)
                if get is not None: 
                    contents = get['contents']
                else:
                    contents = []
        else:
            if continuation_token:
                response = search_client.search(continuation=continuation_token, params='EgWKAQIIAWoMEAMQBBAJEAoQBRAV')
                mappings = response['continuationContents']['musicShelfContinuation']
                contents = mappings['contents']
            else:
                response = search_client.search(query, params='EgWKAQIIAWoMEAMQBBAJEAoQBRAV')
                mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
                contents = []
                if len(mappings) > 1:
                    get = mappings[1].get('musicShelfRenderer', None)
                    if get:
                        contents = get['contents']

            # Log the response for debugging
            if self.debug_level > 2:
                with open('search_response_continuation.json', 'w') as f:
                    json.dump(response, f, indent=4)

        continuation_tkn = mappings.get('continuations', None)
        current_continuation_token = continuation_tkn[0]["nextContinuationData"]["continuation"] if continuation_tkn else None

        return contents, current_continuation_token


    async def grape_fetch(self, query, limit):
        search_client = InnerTube('ANDROID_MUSIC')
        audio_client = InnerTube('ANDROID_VR')

        start = time.time()

        contents = None
        query_correction_info = None

        if not self.grapeDeepSearchEnabled:
            response = search_client.search(query)
            mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
            get = mappings[1].get('musicShelfRenderer', None)

            if get is not None:
                contents = get['contents']
        else:
            response = search_client.search(query, params='EgWKAQIIAWoMEAMQBBAJEAoQBRAV')
            if  self.debug_level > 2:
                with open('mappings.json', 'w') as f:
                    json.dump(response, f, indent=4)
            try:
                mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
            except KeyError:
                print(Fore.RED + '-> No results found, Exiting ...' + Fore.RESET)
                return []

            if len(mappings) > 1:
                query_correction_info = mappings[0]['itemSectionRenderer']['contents'][0]['showingResultsForRenderer']
                contents = mappings[1].get('musicShelfRenderer', None)['contents']
                continuation_tkn = mappings[1]['musicShelfRenderer'].get('continuations', None)
            else:
                contents = mappings[0]['musicShelfRenderer']['contents']
                continuation_tkn = mappings[0]['musicShelfRenderer'].get('continuations', None)

        root_continuation_token = continuation_tkn[0]["nextContinuationData"]["continuation"] if continuation_tkn else None

        scraped = []
        initial_length = len(contents)

        if initial_length < limit:
            start_len = initial_length
            curr_continuation_token = root_continuation_token
            net_content = contents.copy()

            while start_len < limit:
                if self.debug_level > 1:
                    print(Fore.MAGENTA + f'-> Continuing search... {start_len}/{limit} fetched' + Fore.RESET)

                continuation_contents, curr_continuation_token = await self._grape_fetch_search_content(query, search_client, curr_continuation_token)
                start_len += len(continuation_contents)
                net_content.extend(continuation_contents)
            
            if self.debug_level > 1:
                print(Fore.MAGENTA + f'-> Found {len(net_content)} results, fetching & filtering now ...' + Fore.RESET)

            sorted_data = await self._grape_fetch_sanitizedata(net_content, query_correction_info, audio_client)
        else:
            if self.debug_level > 1:
                print(Fore.MAGENTA + f'-> Found {len(contents)} results, fetching & filtering now ...' + Fore.RESET)
            
            sorted_data = await self._grape_fetch_sanitizedata(contents, query_correction_info, audio_client)
            if len(sorted_data) > limit:
                sorted_data = sorted_data[:limit]
                
        end = time.time()
        if self.debug_level > 0:
            print(Back.MAGENTA + Fore.WHITE +f'\n{len(sorted_data)} Results fetched, Took {end - start:.2f} seconds.'+Fore.RESET + Back.RESET)

        if self.loggingEnabled and self.debug_level > 0:
            print()

            for k in sorted_data:
                print(Fore.MAGENTA + '    ', k['title'], 'by', k['artist'], '•', k['formattedDuration'], '•', k['plays']  + Fore.RESET + Back.RESET)

        return sorted_data



def ask_for_debug_mode():
    
    level = input('-> Select Debug level : \n1. User-only\n2. Log\n3. Detailed log\n(Select 1, 2 or 3) > ')
    if level.isdigit():
        level = int(level)
    else:
        level = 0
        print(Fore.RED + '-> Invalid debug level, Debug level defaulting to User-only.'+Fore.RESET)

    print(Fore.MAGENTA + f'Debug level set to : {level}' + Fore.RESET)
    debug_mode  = True if level > 0 else False
    return debug_mode, level


if __name__ == '__main__':
    art = """
   ______                   ___    ____     
  / ____/_______  ____     |__ \  / __ \    
 / / __/ ___/ _ \/ __ \    __/ / / / / /    
/ /_/ / /  /  __/ /_/ /   / __/_/ /_/ /     
\____/_/   \___/ .___/   /____(_)____/      
              /_/                           
"""
    print(Fore.MAGENTA + art + Fore.RESET)
    debug_mode = 0
    i1 = time.time()
    fetcher = GrepFetcher(deepSearchEnabled=True, debugMode=(True, debug_mode))
    i2 = time.time()
    print(Back.MAGENTA + Fore.GREEN + f'Grep Fetcher (v2.0 ASYNC-M CLI), Developed by Aditya Gaur (Init took {i2-i1:.2f})' + Fore.RESET + Back.RESET + '\n')
    debug_mode, level = ask_for_debug_mode()
    fetcher.set_debug_mode((debug_mode, level))

    while True:
        _ = input("Press enter to continue [or 'q' to quit, or 's' to open settings] ...\n")
        if _.lower() == 'q':
            break
        if _.lower() == 's':
            debug_mode, level = ask_for_debug_mode()
            fetcher.set_debug_mode((debug_mode, level))

        query = input(Fore.WHITE + 'Enter search query > ')
        if query =="":
            print(Fore.RED + '-> Invalid query, Exiting ...' + Fore.RESET)
            break

        limit = input('Enter number of results to fetch > ' + Fore.RESET)
        if limit.isdigit() and limit != '0':
            limit = int(limit)

        else:
            limit = 10
            print(Fore.RED + '-> Invalid limit, defaulting to 10.'+ Fore.RESET)

        print(Fore.MAGENTA + '\n-> Fetching results ...' + Fore.RESET)
        r2 = asyncio.run(fetcher.grape_fetch(query, limit))
        print(Back.MAGENTA + Fore.YELLOW + f"Grep Fetcher (v2.0 ASYNC-M), For results check 'search_results.json' " + Fore.RESET + Back.RESET + '\n')
        if debug_mode > 2:
            print(Back.MAGENTA + Fore.YELLOW + f"(info) For mappings & continuation mappings check 'search_response_mappings.json' & 'search_response_continuation.json', respectively. " + Fore.RESET + Back.RESET + '\n')

        with open('search_results.json', 'w') as f:
            json.dump(r2, f, indent=4)
