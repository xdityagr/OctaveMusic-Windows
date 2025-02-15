from tokenize import String
from flask.cli import pass_script_info

import time
import asyncio, aiohttp
from pytubefix import Search
import re
import json
from json import JSONDecodeError
from typing import List, Dict
import sys, os
from datetime import datetime
from .ai_utils import StringProcessor

class Fetcher:        
    def __init__(self, cache=True):
        
        self.results = []
        self.current_query = ""
        self.results_cache_fp = "cache/.results_cache.json"
        self.MAX_RESULT_THRESHOLD = 100
        self.results_fetch_time = ()
        self._search_response_object = None
        self.cachingEnabled = cache
        self.cacheExpiresAfter = 1 # day
        self.string_processor = StringProcessor()

        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        if self.cachingEnabled:
            self._cache_lookup()
        

    def _parse_metadata(self, raw_data: str) -> Dict:
            # Logic to parse video metadata from raw HTML
            details_pattern = re.compile('videoDetails\":(.*?)\"isLiveContent\":.*?}')
            upload_date_pattern = re.compile("<meta itemprop=\"uploadDate\" content=\"(.*?)\">")
            genre_pattern = re.compile("<meta itemprop=\"genre\" content=\"(.*?)\">")
            like_count_pattern = re.compile("iconType\":\"LIKE\"},\"defaultText\":(.*?)}}")
            url_pattern = re.compile('"streamingData":(\{.*?\})')
            
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
                    'author': metadata['author'],
                    'upload_date': upload_date,
                    'url': f"https://www.youtube.com/watch?v={metadata['videoId']}",
                    'thumbnails': metadata.get('thumbnail', {}).get('thumbnails'),
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

                try:
                    data['url'] = url_pattern.search(raw_data).group(1)
                except AttributeError:
                    data['url'] = None

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

            if limit>self._search_response_length and not auto_next:
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
            matches = self._cache_lookup(query)
            print('Looking up in cache .. ')
            print(f'matches : {len(matches) if matches else matches}')
            if matches:
                print('Found. Fetching from cache ..')
                if len(matches) >= limit:
                    return matches[:limit]
                # else:
                    
        
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
            computed = self.string_processor.compute_similarity(query, match_candidates, threshold=0.70)
            bsm = list(filter(None, [all_data[i][1][1] if s == True else None for i, _, s in computed]))

            bsm = [j for i in bsm for j in i]
            
            known_ids = set()
            for match in bsm:    
                if match['id'] not in known_ids :
                        best_matches.append(match)
                        known_ids.add(match['id'])

            # for i in best_matches:
                # print(i['title'], i['id'], '\n')

                # print(similarity_scores)
            for index, score, surpasses_threshold in computed:
                print(f"Found index {index} with similarity score: {score:.4f} -> Surpasses threshold : {surpasses_threshold}")


            return best_matches if best_matches != [] and query != None else None

fetcher = Fetcher(cache=True)        
print("Octave Fetcher - Fetch metadata the fastest way. Enter your query & go.")
while True:
    query= ""
    limit = 0
    autonext = True
    force_new= False
    inp = input('> ')
    # query:limit:autonext:force_new
    args = inp.split(':')
    query, limit, autonext, force_new = args
    limit=int(limit)
    autonext = True if autonext=='True' else False
    force_new = True if force_new == 'True' else False
    
    resp = fetcher.fetch(query, limit, autonext, force_new)

    print(f'> {len(resp)} Responses fetched in {fetcher.results_fetch_time[0] if fetcher.results_fetch_time != () else  "--"} ')
    for i in resp:
        print(i['title'], i['url'])
    print(';')



 
