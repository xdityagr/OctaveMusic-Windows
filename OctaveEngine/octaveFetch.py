
import time
import asyncio, aiohttp
from turtle import st
from cv2 import threshold
from pytubefix import Search
import re
import json
from json import JSONDecodeError
from typing import List, Dict, final
import sys, os
from datetime import datetime

from pathlib import Path


from .ai_utils import *
from .definitions import OctaveGrapeSearchMethod, StreamMediaObject, OctaveStreamAudioQuality, OctaveStreamSupportedCodec, OctaveStreamFetchPreference, OctaveSearchProtocol

from ._innertube import InnerTube
from ._innertube.config import config

import yt_dlp

class OctaveFetch:
    def __init__(self, cachingEnabled=True, protocol=OctaveSearchProtocol.OCTAVE, searchMethod=None, loggingEnabled=True):
        self.results = []
        self.current_query = ""
        self.results_cache_fp = "OctaveEngine/cache/.results_cache.json"
        self.client_info_fp = "OctaveEngine/Data/.client_info.json"
        self.search_response_log_fp = "OctaveEngine/Logs/.search_logs.json"
        self.search_mappings_log_fp = "OctaveEngine/Logs/.search_mappings.json"

        self.MAX_RESULT_THRESHOLD = 100
        self.BEST_CLIENTS = self._load_clients()
        self.results_fetch_time = ()
        self._search_response_object = None
        self.cachingEnabled = cachingEnabled
        self.cacheExpiresAfter = 1 # day
        self.string_processor = StringProcessor()
        self.protocol = protocol
        self.grapeDeepSearchEnabled = False

        self.logging = loggingEnabled

        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        if self.cachingEnabled:
            self._cache_lookup()

        if self.protocol.name =='GRAPE':
            self.grapeDeepSearchEnabled= searchMethod

    def _load_clients(self):
        BEST_CLIENTS  = ['ANDROID_VR', 'IOS', 'WEB_PARENT_TOOLS'] 
        faulty = self._verify_clients(BEST_CLIENTS)
        for c in BEST_CLIENTS: 
            if c in faulty: 
                BEST_CLIENTS.remove(c)
        
        return BEST_CLIENTS

    def _verify_clients(self, clients):
        test_id = 'dQw4w9WgXcQ' # Don't open it up on youtube...
        faulty = []

        for client_name in clients:
            client = InnerTube(client_name) 
            data = client.player(test_id)
            playability_status = data["playabilityStatus"]["status"]

            if playability_status != 'OK':
                faulty.append(client_name)
        
        return faulty
        

    def generate_client_file(self,  force_new=False, force_verify=False):
        path = Path(self.client_info_fp)
        test_id = 'dQw4w9WgXcQ' # Don't open it up on youtube...
        clients = None

        if path.exists():
            doesnotexist = False
            if force_new:
                print("Forcing generation ... ")
                os.remove(str(path))
                clients: List[str] = [client.client_name for client in config.clients]
            else:
                print("Client info already exists.")
                loaded = None

                try:
                    with open(self.client_info_fp, 'r') as clientfile:
                        loaded = json.load(clientfile)
                except JSONDecodeError as e:
                    self._generate_client_file(force_new=True)

                if loaded:
                    if force_verify:
                        clients = list(loaded['working'].keys())
                    else:
                        return loaded
            
        else:
            print("Client info does not exist, Generating client info file ...")
            doesnotexist = True
            clients: List[str] = [client.client_name for client in config.clients]

        if force_verify or force_new or doesnotexist:

            OK = ['OK']
            NOT_OK = ['UNPLAYABLE', 'LOGIN_REQUIRED']
            not_working_clients  = {}
            working_clients  = {}

            s = time.time()
            for client in clients:
                print(f"running for {client} ...")
                start= time.time()
                crr = InnerTube(str(client))    
                try:
                    response = crr.player(test_id)
                    response = response["playabilityStatus"]["status"]
                    end = time.time()

                    time_taken = end-start

                    if response in NOT_OK:
                        not_working_clients[str(client)] = response

                    if response in OK:
                        working_clients[str(client)] = ({'Time':time_taken}, response)

                except Exception as e:
                    not_working_clients[str(client)] = f'Error : {e}'

                print(f'Done {clients.index(client) + 1}/{len(clients)}')
            
            en = time.time()

            data = {'not_working':not_working_clients, 'working':working_clients}

            with open(self.client_info_fp, 'w') as tmp: pass
            try:
                with open(self.client_info_fp, 'w') as clientfile:
                    json.dump(data, clientfile, indent=4)
                
                print(f'Client Data Generated/Verified. Took {en-s} seconds.')
            except JSONDecodeError as e:
                print(f'Error encountered, Trying again ... ')
                os.remove(str(path))
                with open(self.client_info_fp, 'w') as tmp: pass
                with open(self.client_info_fp, 'w') as clientfile:
                    json.dump(data, clientfile, indent=4)

            loaded = None

            try:
                with open(self.client_info_fp, 'r') as clientfile:
                    loaded = json.load(clientfile, indent=4)
            except JSONDecodeError as e:
                self._generate_client_file(force_new=True)
            finally:
                return loaded
                    
    def _parse_metadata(self, raw_data: str) -> Dict:
        # Logic to parse video metadata from raw HTML
        details_pattern = re.compile('videoDetails\":(.*?)\"isLiveContent\":.*?}')
        upload_date_pattern = re.compile("<meta itemprop=\"uploadDate\" content=\"(.*?)\">")
        genre_pattern = re.compile("<meta itemprop=\"genre\" content=\"(.*?)\">")
        like_count_pattern = re.compile("iconType\":\"LIKE\"},\"defaultText\":(.*?)}}")

        
        try : 
            raw_details = details_pattern.search(raw_data).group(0)
            upload_date = upload_date_pattern.search(raw_data).group(1)
            metadata = json.loads(raw_details.replace('videoDetails\":', ''))
            
            # with open('raw_search_resuls.json', 'w') as m: pass
            # with open('raw_search_resuls.json', 'w') as m2: json.dump(metadata,m2, indent=4)
    
    
            data = {
                'title': metadata['title'],
                'id': metadata['videoId'],
                'views': metadata.get('viewCount'),
                'duration': metadata['lengthSeconds'],
                'artist': metadata['author'],
                'upload_date': upload_date,
                'watch_url': f"https://www.youtube.com/watch?v={metadata['videoId']}",
                'thumbnails': metadata.get('thumbnail', {}).get('thumbnails'),
                'mimeType':metadata.get('mimeType', None),
                'tags': metadata.get('keywords'),
                # 'description': metadata.get('shortDescription'),
            }
            try:
                likes_count = like_count_pattern.search(raw_data).group(1)
                data['likes'] = json.loads(likes_count + '}}}')[ 
                    'accessibility'
                ]['accessibilityData']['label'].split(' ')[0].replace(',', '')
            except (AttributeError, KeyError, json.decoder.JSONDecodeError):
                data['likes'] = None
            try:
                data['genre'] = genre_pattern.search(raw_data).group(1)
            except AttributeError:
                data['genre'] = None

            # try:
            #     data['url'] = url_pattern.search(raw_data).group(1)
            # except AttributeError:
            #     data['url'] = None

            return data

        except Exception as e:
            print(f"Error parsing metadata: {e}")
            return {}
    
    async def _fetch_metadata(self, video_id: str) -> dict:
        base_url = f"https://www.youtube.com/watch?v={video_id}"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/107.0.0.0 Safari/537.36"
            ),
        }

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(base_url) as response:
                    if response.status != 200:
                        print(f"Failed to fetch metadata for {video_id}, HTTP {response.status}")
                        return {}
                    html = await response.text()
                    return self._parse_metadata(html)
        except aiohttp.ClientError as e:
            print(f"HTTP error for {video_id}: {e}")
            return {}
    
    async def _fetch_all_metadata(self, video_ids: List[str]) -> List[Dict]:
        tasks = [self._fetch_metadata(video_id) for video_id in video_ids]
        return await asyncio.gather(*tasks)

    async def _fetch(self, query:str, limit=10, auto_next=False):
        # keywrds = query.split(':')[0]
        # limit = int(query.split(':')[1])

        # print(f"> Fetching [{limit}] result(s) for query [{keywrds}] ... ")
        self.current_query = query.strip()

        search_time_start = time.time()

        if limit <= self.MAX_RESULT_THRESHOLD:
            
            try:
                self._search_response_object = Search(self.current_query)
            except Exception as e:
                print(f'Error : {e}')
                return None
            
            self._search_response_length = len(self._search_response_object.videos)

            if auto_next and self._search_response_length < limit:
                print(f'Only fetched [{self._search_response_length}] Results, Lazy fetching started ... ')

                while len(self._search_response_object.videos) < limit:
                    self._search_response_object.get_next_results()
                    print(f'Loaded {len(self._search_response_object.videos) - self._search_response_length} more results ... ')
                    
                self._search_response_length = len(self._search_response_object.videos)
                print(f'Loaded total [{len(self._search_response_object.videos)}] results, fetching metadata for [{limit}] ...')

            if limit > self._search_response_length and not auto_next:
                limit = self._search_response_length
                print(f'Only fetching {[limit]} results ... ')

            video_ids =[self._search_response_object.videos[i].video_id for i in range(limit)] 

            search_time_end = time.time()

            search_time = search_time_end-search_time_start

            metadatafetch_time_start = time.time()
            
            try:
                metadata = await self._fetch_all_metadata(video_ids)
                self.results.extend(metadata)

            except Exception as e:
                print(f'Exception : {e}')
                return None

            final_results_len = len(metadata)

            metadatafetch_time_end = time.time()

            metadata_time = metadatafetch_time_end-metadatafetch_time_start
            self.results_fetch_time = [metadata_time+search_time, search_time, metadata_time]

            return self.results
        
        else:
            return None
        
    def fetch(self, query, limit=10, auto_next=False, force_new=False):
        self.results = []
        """Fetch method to fetch results 

        Args:
            query (str): Search query
            limit (int, optional): number of results. Defaults to 10.
            auto_next (bool, optional): auto find next page results if limit exceeds length of currently fetched data. Defaults to False.
            force_new (bool, optional): force a new search, will not load from cache. Defaults to False.

        Returns:
            response: response can be None, results.
        """
        print(f'LIMIT = {limit}')
        if not force_new:
            match_start_time = time.time()
            matches = self._cache_lookup(query)
            print('Looking up in cache .. ')
            print(f'matches : {len(matches) if matches else matches}')
            if matches:
                print('Found. Fetching from cache ..')
                if len(matches) >= limit:
                    match_end_time = time.time()
                    self.results_fetch_time = [match_end_time-match_start_time, 0, 0]
                    return matches[:limit]
                
        
        print('Not in cache, Searching ... ')
        if self.protocol.name == 'GRAPE':
            pass
        else:                    
            print('Not in cache, Searching ... ')
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                response = loop.run_until_complete(self._fetch(query, limit, auto_next))
            finally:
                loop.close()
                if self.cachingEnabled and response != None:
                    self._cache_new(self.current_query, response)

            return response
    
    async def _fetch_next(self, next=10):
        if self.results:
            print(f'Only fetched [{self._search_response_length}] Results, Lazy fetching started ... ')
            fetched = 0
            new_results = []
            while fetched < next:
                self._search_response_object.get_next_results()
                fetched =len(self._search_response_object.videos) - self._search_response_length
                
                new_results.extend(self._search_response_object.videos[self._search_response_length:])

                print(f'Loaded {len(self._search_response_object.videos) - self._search_response_length} more results ... ')

            self._search_response_length = len(self._search_response_object.videos)
            print(f'Loaded total [{len(self._search_response_object.videos)}] results, fetching metadata for [{next}] ...')

            try:
                metadata = await self._fetch_all_metadata(new_results)
                self.results.extend(metadata)

                final_results_len = len(metadata)

                metadatafetch_time_end = time.time()

                return self.results
            
            except Exception as e:
                print(f'Exception : {e}')
                return None
        else:
            return None
        
    def fetch_next(self, next=10):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(self._fetch_next(next))
        finally:
            loop.close()
            if self.cachingEnabled and response != None:
                
                self._cache_new(self.current_query, response)

        
        return response


    def _cache_new(self, query, results, nochange=False):
        temp = {'results_cache': []}

        if os.path.exists(self.results_cache_fp):
            try:
                with open(self.results_cache_fp, 'r') as f:
                    old_results = json.load(f)
                    if nochange: 
                        return old_results

                if not nochange:
                    results_cache = old_results.setdefault('results_cache', [])
                    query_entry = next((entry for entry in results_cache if query in entry), None)
                    if query_entry:
                        timestamp, existing_results = query_entry[query]
                    
                        for result in results:
                            if result not in existing_results:
                                existing_results.append(result)
                    
                    else:
                        # If the query doesn't exist, add it to the results cache
                        results_cache.append({query: (str(datetime.today()), list(results))})

                    with open(self.results_cache_fp, 'w') as fp2:
                        old_results = json.dump(old_results, fp2, indent=4)

            except json.JSONDecodeError as e:
                os.remove(self.results_cache_fp)

        else:
            with open(self.results_cache_fp, 'w') as f: pass
            with open(self.results_cache_fp, 'w') as f2: json.dump(temp,f2, indent=4)
            self._cache_new(query, results, nochange)

    def _cache_lookup(self, query=None):
        
        lookup= self._cache_new(query=None, results=None, nochange=True)
        
        best_matches = []
        match_candidates = []
        all_data = []
        current_datetime = datetime.today()
        if not lookup :
            return None
        
        if lookup['results_cache'] == []:
            return None
        
        for idx, item in enumerate(lookup['results_cache']):
            for k,v in item.items():

                time, val = v
                cache_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
                diff = cache_time - current_datetime 

                if diff.days > self.cacheExpiresAfter:
                    i = lookup['results_cache'].pop(idx)
                    print(f'Removed cache = {idx}:"{query}", lasted for {diff.days}d:{diff.seconds//3600}h:{(diff.seconds % 3600)//60}m')

                all_data.append((k,v))

                try:
                    with open(self.results_cache_fp, 'w') as f2: json.dump(lookup, f2, indent=4)
                except JSONDecodeError as e:
                    print(f'Error : {e}')

        if query:         
            print('NOW running matching algo : ')
            match_candidates = [q for q, v in all_data]
            print('match_candidates : ', match_candidates)


            # IMPORTANT ! DO NOT ERASE.

            # computed = self.string_processor.compute_similarity(query, match_candidates, threshold=0.70)
            # bsm = list(filter(None, [all_data[i][1][1] if s == True else None for i, _, s in computed]))

            # bsm = [j for i in bsm for j in i]
            
            # known_ids = set()
            # for match in bsm:    
            #     if match['id'] not in known_ids :
            #             best_matches.append(match)
            #             known_ids.add(match['id'])

            # # for i in best_matches:
            #     # print(i['title'], i['id'], '\n')

            #     # print(similarity_scores)
            # for index, score, surpasses_threshold in computed:
            #     print(f"Found index {index} with similarity score: {score:.4f} -> Surpasses threshold : {surpasses_threshold}")


            # return best_matches if best_matches != [] and query != None else None

                # Use TfidfVectorizer to compute similarity
            vectorizer = TfidfVectorizer().fit(match_candidates + [query])
            query_vec = vectorizer.transform([query])
            candidate_vecs = vectorizer.transform(match_candidates)

            similarities = cosine_similarity(query_vec, candidate_vecs).flatten()
            best_indices = similarities.argsort()[::-1]  # Sort indices by similarity score in descending order

            for i in best_indices:
                score = similarities[i]
                surpasses_threshold = score >= 0.70  # Adjust threshold as needed
                print(f"Found index {i} with similarity score: {score:.4f} -> Surpasses threshold : {surpasses_threshold}")
                if surpasses_threshold:
                    best_matches.extend(all_data[i][1][1])

            # Remove duplicates based on ID
            known_ids = set()
            best_matches = [match for match in best_matches if not (match['id'] in known_ids or known_ids.add(match['id']))]

        return best_matches if best_matches else None   
    
    def fetch_stream(self, video_id, preference= OctaveStreamFetchPreference.QUALITY_FIRST, codec=OctaveStreamSupportedCodec.opus, quality=OctaveStreamAudioQuality.HIGH):    
        qlist = [140.00, 128.00, 60.00, 40.00]

        quality_responses = 'QUALITY_OK', 'QUALITY_NOTFOUND'
        codec_responses = 'CODEC_OK', 'CODEC_NOT_FOUND'

        client_name = self.BEST_CLIENTS[0]
        print(self.BEST_CLIENTS,client_name)
        client = InnerTube(str(client_name))
        
        fetched = []
        
        upper_limit = qlist[qlist.index(quality.value)-1] if quality.value != 140.00 else 100_000_000
        print(f'Upper limit = {upper_limit}')

        quality_thresh = quality.value
        quality_query = 'MEDIUM' if quality_thresh>=128  else 'LOW'

        data = client.player(video_id)
        
        # TO FIX -> 
        with open('lalala.json', 'w') as j:
            json.dump(data, j, indent=8)

        formats = data['streamingData']['adaptiveFormats']
        # print(formats)
        for format in formats:
            if format['mimeType'].startswith("audio"):
               if format["audioQuality"] == f"AUDIO_QUALITY_{quality_query}":
                    fetched.append(format)

        print(f'{len(fetched)} responses fetched ... ')

        responses  = []
        best_matches = []
        
        for available in fetched:
            
            quality_resp = quality_responses[1]
            codec_resp = codec_responses[1]

            curr_bitrate = round(int(available['bitrate'])/1000, 2)
            
            if upper_limit > curr_bitrate >= quality_thresh:    
                quality_resp = quality_responses[0]

            if codec.name in format['mimeType']:
                codec_resp = codec_responses[0]
            
            # print('CURRENT BIRATE ', curr_bitrate, ' THRESHOLD ', quality_thresh ,  'RESPONSE ', quality_resp)
            # print('CURRENT CODEC ', format['mimeType'], ' REQUIRED CODEC ', codec.name , 'RESPONSE ', codec_resp)
            # print()
            
            responses.append((quality_resp, codec_resp, available))

        # print(len(responses))
        for response in responses:
            # response = {'quality':, 'codec':, 'ultimatum':''}
            output = {}
            if response[0] == quality_responses[0] and response[1] == codec_responses[0]:
                output['quality'] = response[0]
                output['codec'] = response[1]
                output['ultimatum'] = 'BOTH_OK'

                best_matches.append({'response':output, 'info':response[2]})

            else:
                
                if preference.name == 'QUALITY_FIRST':
                    if response[0] == quality_responses[0]:
                        
                        output['quality'] = response[0]
                        output['codec'] = response[1]
                        output['ultimatum'] = 'QUALITY_OK&CODEC_NOMATCH'

                        best_matches.append({'response':output, 'info':response[2]})

                    else:

                        if response[1] == codec_responses[0]:

                            output['quality'] = response[0]
                            output['codec'] = response[1]
                            output['ultimatum'] = f"{output['quality']}&{output['codec']}"

                            best_matches.append({'response':output,'info':response[2]})
                        else:
                            output['quality'] = response[0]
                            output['codec'] = response[1]
                            output['ultimatum'] = "BOTH_NOMATCH"

                            best_matches.append({'response':output,'info':response[2]})

                elif preference.name == 'CODEC_FIRST':
                    if response[1] == codec_responses[0]:
                        
                        output['quality'] = response[0]
                        output['codec'] = response[1]
                        output['ultimatum'] = f"{output['quality']}&{output['codec']}"

                        best_matches.append({'response':output, 'info':response[2]})
                        
                    else:
                        if response[0] == quality_responses[0]:
                            
                            output['quality'] = response[0]
                            output['codec'] = response[1]
                            output['ultimatum'] = f"{output['quality']}&{output['codec']}"

                            best_matches.append({'response':output,'info':response[2]})
                        else:
                            output['quality'] = response[0]
                            output['codec'] = response[1]
                            output['ultimatum'] = "BOTH_NOMATCH"

                            best_matches.append({'response':output,'info':response[2]})
        best_matches.reverse()
        
        return best_matches
    
        
    def grape_fetch(self, query):

        api = "AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc"
        # params = {'androidSdkVersion':31, }

        search_client = InnerTube('ANDROID_MUSIC')
        audio_client = InnerTube('ANDROID_VR')

        start= time.time()
        
        contents = None
        query_correction_info = None

        if not self.grapeDeepSearchEnabled:
            response = search_client.search(query)
            mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
            get = mappings[1].get('musicShelfRenderer', None)
            
            if  get is not None: 
                contents =  get['contents']  

        else:
            response = search_client.search(query, params='EgWKAQIIAWoMEAMQBBAJEAoQBRAV')
            
            mappings = response['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']

            if len(mappings) != 1:
                    
                query_correction_info = mappings[0]['itemSectionRenderer']['contents'][0]['showingResultsForRenderer']
                contents= mappings[1].get('musicShelfRenderer', None)
                contents =contents['contents']
        
            else:
                contents = mappings[0]['musicShelfRenderer']['contents']

        if self.logging:
            with open(self.search_mappings_log_fp, 'w') as f:
                json.dump(response, f, indent=4)

        scraped = []

        print(f'Found {len(contents)} results, fetching & filtering now ...')

        for i in range(len(contents)):
            print('Fetching title, subtitle, thumbnails, video Id ...')
            data = {}
            data['title'] =            contents[i]['musicTwoColumnItemRenderer']['title']['runs'][0]['text']
            sub= contents[i]['musicTwoColumnItemRenderer']['subtitle'] 
            data['artist'] = sub['runs'][0]['text']
            data['formattedDuration'] = sub['runs'][2]['text']
            data['plays'] = sub['runs'][4]['text']

            correctedQuery = query_correction_info['correctedQuery'] if query_correction_info is not None else None
            correctedQueryString = ""
            correctedQueryInParts = []
            
            if correctedQuery is not None:
                for q in correctedQuery['runs']:
                    if q.get('italics', False):
                        correctedQueryInParts.append({'text':q['text'], 'isCorrected':True})
                    else:
                        correctedQueryInParts.append({'text':q['text'], 'isCorrected':False})

                    correctedQueryString+= q['text']

            data['queryCorrection'] = correctedQueryString, correctedQueryInParts
            
            data['thumbnails'] =             contents[i]['musicTwoColumnItemRenderer']['thumbnail']['musicThumbnailRenderer']['thumbnail']['thumbnails']
            data['id'] =  contents[i]['musicTwoColumnItemRenderer']['navigationEndpoint']['watchEndpoint']['videoId']
            print('Done. ')

            try:
                print('Fetching audio info ...')
                audioInfo = audio_client.player(data['id'])
                with open('sample.json', 'w') as f1:
                    json.dump(audioInfo, f1, indent=4)

                suitable_audio_urls = []
                formats = audioInfo['streamingData']['adaptiveFormats']
                print(f'Found {len(formats)} formats ... ')
                print(f'Filtering for audio only formats ... ')
                for idx, format in enumerate(formats):
                    print(f'-> Processing format {idx+1} ')
                    if 'audio' in format['mimeType']:
                        suitable_audio_urls.append(format)
                    
                print(f'Done, Found {len(suitable_audio_urls)} audio formats')

            except Exception as e:
                print(f'Could not fetch audio info, Error : {e}')
                audioUrl = None
                break

            data['streamUrls'] = suitable_audio_urls

            scraped.append(data)
            print(f'Finally fetched {len(scraped)} results, Now filtering ...')


        ids = set()
        sorted_data = []
        
        for i in scraped:
            if i['id'] not in ids:
                ids.add(i['id'])
                sorted_data.append(i)

        end= time.time()
        print(f'\n{len(sorted_data)} Results fetched , Took {end-start} seconds ')
        print()
        for k in sorted_data:
            print('    ', k['title'], ' by ', k['artist'],' • ' ,k['formattedDuration'], ' ', k['plays'])

        templ = {'scraped_data': scraped}
        with open('main_search_results.json', 'w') as f:
            json.dump(templ, f, indent=4)

        return sorted_data
    
                



# ocf = OctaveFetch(cachingEnabled=False, protocol=OctaveSearchProtocol.OCTAVE)
# retr = ocf.fetch_stream('yzTuBuRdAyA', preference=OctaveStreamFetchPreference.QUALITY_FIRST, quality=OctaveStreamAudioQuality.HIGH, codec=OctaveStreamSupportedCodec.opus)
# print(retr[0]['info']['url'])

# ocf.fetch_stream('https://www.youtube.com/watch?v=yzTuBuRdAyA') # 3.873204469680786


# rtr = ocf.fetch('the hills weeknd')
# objects = objectify(StreamMediaObject,rtr)
# for object in objects:
#     print(object.title)
