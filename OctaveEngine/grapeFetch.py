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

from sympy import Idx
from ai_utils import *
from definitions import OctaveGrapeSearchMethod, StreamMediaObject, OctaveStreamAudioQuality, OctaveStreamSupportedCodec, OctaveStreamFetchPreference, OctaveSearchProtocol

from _innertube import InnerTube
from _innertube.config import config

import asyncio
import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class Grape:

    async def _fetch_metadata(self, video_id: str) -> dict:

        headers = {
                "X-Goog-Api-Format-Version": "1",
                "X-YouTube-Client-Name": '21',
                "X-YouTube-Client-Version": "5.01",
                "User-Agent":  "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
                "Referer": "https://music.youtube.com/"
            }
            
                    
                    
        # base_url = f"https://www.youtube.com/watch?v={video_id}"
        # headers = {
        #     "User-Agent": (
        #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        #         "AppleWebKit/537.36 (KHTML, like Gecko) "
        #         "Chrome/107.0.0.0 Safari/537.36"
        #     ),
        # }

        base_url="https://youtubei.googleapis.com/youtubei/v1/"


        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post() as response:
                    if response.status != 200:
                        print(f"Failed to fetch metadata for {video_id}, HTTP {response.status}")
                        return {}
                    html = await response.text()
                    return self._parse_metadata(html)
        except aiohttp.ClientError as e:
            print(f"HTTP error for {video_id}: {e}")
            return {}
        



        # ClientContext(
        #     client_id=21,
        #     client_name="ANDROID_MUSIC",
        #     client_version="5.01",
        #     user_agent=USER_AGENT_ANDROID,
        #     api_key="AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI",
        # ),

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
            with open('raw_search_results.json', 'w') as m2: json.dump(metadata,m2, indent=4)
    
    
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
        

    def fetch(self, videoId):
        return asyncio.run(self._fetch_metadata(videoId))

        
gr = Grape()
dat = gr.fetch('dQw4w9WgXcQ')
with open('raw_responsedata.json', 'w') as f:
    json.dump(dat, f, indent=4)