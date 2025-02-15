from enum import Enum, auto
from colorama import Fore, Back, Style
from PIL import Image
import io
from pathlib import Path

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from mutagen.mp4 import MP4
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from mutagen.oggopus import OggOpus

import subprocess
import requests
import tinytag
import json
from json import JSONDecodeError
from mutagen import MutagenError
from mutagen import File


# from OctaveEngine.MediaControls_VLC import VLCPlayer
from .errors import *
import filetype
import aiohttp

import asyncio

SUPPORTED_FILE_FORMATS = ['WAV', 'FLAC', 'OPUS', 'M4A', 'MP3', 'MP4']

class OctaveStreamFetchPreference(Enum):
    QUALITY_FIRST = 0
    CODEC_FIRST = 2
    
class OctaveStreamAudioQuality(Enum):

    HIGH =  140.00
    STANDARD =  128.00
    LOW =  60.00
    WORSE = 40.00

class OctaveAudioBackend(Enum):
    VLC = auto()
    DEFUALT = auto()


class OctaveStreamSupportedCodec(Enum):
    avc1 = 2
    vp9 = 4
    mp4a = 8
    opus = 10

class OctaveSearchProtocol(Enum):
    OCTAVE = 0
    GRAPE = 2

class OctaveGrapeSearchMethod(Enum):
    Top3 = 0
    DeepSearch = 3

import requests
from concurrent.futures import ThreadPoolExecutor

# ISSUE -> fetching thumbnails in async freezes .
class OctaveCoverArt:
    def __init__(self, coverArtData) -> None:
        self.DEFAULT_ART = "resources\i.png"
        self.coverArtData = coverArtData if coverArtData else None

        self.choices = None
        self.available_dimensions = None

        if isinstance(coverArtData, list):
            try:

                self.thumbnails = {}
                self.thumbnail_urls = []

                for dat in coverArtData:
                    self.thumbnails[dat['url']] = f"{dat['width']}x{dat['height']}"

                self.thumbnail_urls = [i for i in list(self.thumbnails.keys())]   

                cover_arts = self.thumbnails_to_coverarts(self.thumbnail_urls) 
                # print('fetched cover arts : ', cover_arts)
                
                # self.choices = [i. for i in self.thumbnails]

                self.choices = [{self.thumbnails[url]:content} for url, content in cover_arts]

                

                self.available_dimensions = [i for i in list(self.thumbnails.values())]   
                
                print(self.available_dimensions, str(self.choices)[:10])

            except Exception as e:
                print(f'Error encountered : {e.with_traceback()}')
        self.quality_levels=[100, 85, 70, 50, 30]
    
    def return_coverarts_data(self):
        return self.choices

    async def _fetch_thumbnail(self, session, url):
        try:
            async with session.get(url) as response:
                return url, await response.read()  # Read the response content
        except Exception as e:
            return url, None
        
    async def _fetch_thumbnails(self, thumbnail_urls, max_concurrent=10):
        results = {}
        connector = aiohttp.TCPConnector(limit_per_host=max_concurrent)
        
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self._fetch_thumbnail(session, url) for url in thumbnail_urls]
            for task in asyncio.as_completed(tasks):
                url, content = await task
                results[url] = content
        return results

    def thumbnails_to_coverarts(self, thumbnail_urls):
        print('running async thumnbail fetcher ')
        thumbnails= asyncio.run(self._fetch_thumbnails(thumbnail_urls))
        print('done with async thumnbail fetcher ')
        # thumbnails = self._fetch_thumbnails_concurrently(thumbnail_urls, max_workers=10)

        for url, content in thumbnails.items():
            if content:
                print(f"Fetched {len(content)} bytes from {url}")
            else:
                print(f"Failed to fetch {url}")
        
        # print(thumbnails)
        cover_arts = [(url, content) for url, content in thumbnails.items()]
        
        return cover_arts


    def save(self, name,quality=100, path=None):
        if self.coverArtData:
            image = Image.open(io.BytesIO(self.coverArtData))
            output_filename = f'{name}.jpg'
            if path:
                output_filepath = Path.joinpath(Path(path), output_filename)
            else:
                output_filepath = output_filename
            if quality in self.quality_levels:
                image.save(output_filepath, format='JPEG', quality=quality)

    def return_coverArtAsBytes(self):
        return self.coverArtData if self.coverArtData else None
    
    def return_designed_pixmap(self, size=50, radius=25, dimension='smallest'):
        pixmap = QPixmap()
        if self.choices:
            print('choices.')
            try:
                options = ['smallest', 'medium', 'largest']
                options.extend(self.available_dimensions)
                
                if dimension in options:
                    if dimension=='smallest': 
                        dimension = self.available_dimensions[0]
                    if dimension == 'medium': 
                        dimension = self.available_dimensions[int(len(self.available_dimensions)//2)]
                    if dimension == 'largest': 
                        dimension = self.available_dimensions[-1]
                    
                    byteData = None
                    for i in self.choices:
                        get = i.get(dimension, None)
                        if  get is not None:
                            byteData = get
                            break
                    if byteData is not None:
                        pixmap.loadFromData(byteData) 

            except Exception as e:
                print(f'Error:return_designed_pixmap - {e}')


        else:
            print('nochoices.')
            if self.coverArtData:
                pixmap.loadFromData(self.coverArtData) 
            else:
                pixmap = QPixmap(self.DEFAULT_ART)

        # Step 1: Resize the pixmap to 50x50
        resized_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # Step 2: Create a mask for rounded corners
        rounded_pixmap = QPixmap(size, size)
        rounded_pixmap.fill(Qt.transparent)  # Make background transparent

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a rounded rectangle (the mask)
        painter.setBrush(QBrush(Qt.black))
        painter.drawRoundedRect(QRect(0, 0, size, size), radius, radius)

        # Set the mask to the resized pixmap
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.drawPixmap(0, 0, resized_pixmap)
        painter.end()
        print('returning pixmap now.')
        return rounded_pixmap


class LocalMediaObject:
    def __init__(self, fpath=None) -> None:
        self.filePath = fpath
        self.coverArt = None
        self.title = None
        self.artist = None
        self.duration = None
        self.duration_formatted = None
        self.mimeType = None
        self.encoding = None
        self.mimeType =filetype.guess(self.filePath).mime
        self.isLiked = False
        self.isStreamable = False
        # self.external_metadata_ctx = ExtMetadata()
        # self.ext_metadata = self.external_metadata_ctx.getMetadatafromData(self)
        # print(self.ext_metadata)
        
      
        print(self.mimeType)
        
        self.extractMetadata()
        # print('title ', self.title, '\nalbum ', self.album, '\nartist', self.artist,'\nmimeType ',  self.mimeType)

        if self.coverArt:
            self.coverArt.save('cover_art_30', quality=30)

    

    def __repr__(self):
        return (f"Octave Engine:Media Object -> title={self.title!r}, artist={self.artist!r}, "f"duration={self.duration_formatted!r}, mimeType={self.mimeType!r}, "f"filePath={self.filePath!r})")

    def extractMetadata(self):
        mutObj = File(self.filePath)
        if mutObj is None:
            raise FileFormatNotSupported(self.mimeType, 'Could not load this file or unsupported format.')
        
        # try:
            # if self.mimeType == 'mp3':
            #     # Handle MP3 files
            #     audio = MP3(self.filePath, ID3=ID3)
            #     self.title = audio.tags.get('TIT2') or audio.tags.get('\xa9nam')
            #     self.artist = audio.tags.get('TPE1') or audio.tags.get('\xa9ART')
            #     self.album = audio.tags.get('TALB') or audio.tags.get('\xa9alb')
            #     self.duration = audio.info.length
            
            # elif self.mimeType == 'm4a':
            #     # Handle M4A files
            #     audio = MP4(self.filePath)
            #     self.title = audio.tags.get('\xa9nam') or audio.tags.get('title')
            #     self.artist = audio.tags.get('\xa9ART') or audio.tags.get('artist')
            #     self.album = audio.tags.get('\xa9alb') or audio.tags.get('album')
            #     self.duration = audio.info.length
            
            # elif self.mimeType == 'flac':
            #     # Handle FLAC files
            #     audio = FLAC(self.filePath)
            #     self.title = audio.tags.get('title')
            #     self.artist = audio.tags.get('artist')
            #     self.album = audio.tags.get('album')
            #     self.duration = audio.info.length
            
            # elif self.mimeType == 'wav':
            #     # Handle WAV files
            #     audio = WAVE(self.filePath)
            #     self.title = audio.tags.get('title')
            #     self.artist = audio.tags.get('artist')
            #     self.album = audio.tags.get('album')
            #     self.duration = audio.info.length
            
            # elif self.mimeType == 'opus':
            #     # Handle OPUS files (may need additional libraries)
            #     raise NotImplementedError("OPUS files are not natively supported..")
        warn("MIME TYPE", "MIME TYPE IS", self.mimeType)
        if self.mimeType == 'audio/ogg' or self.mimeType == 'audio/opus':

            tag = tinytag.TinyTag.get(self.filePath)
            # image_data = tag.get_image()

            self.title = tag.title
            self.artist = tag.artist
            self.album = tag.album
            self.duration = tag.duration
            
        elif self.mimeType == 'audio/mpeg':
            # MP3 file
            audio = MP3(self.filePath, ID3=ID3)
            self.title = audio.tags.get('TIT2') or audio.tags.get('\xa9nam')
            self.artist = audio.tags.get('TPE1') or audio.tags.get('\xa9ART')
            self.album = audio.tags.get('TALB') or audio.tags.get('\xa9alb')
            self.duration = audio.info.length
            

        elif self.mimeType in ['audio/mp4', 'audio/m4a', 'video/m4a', 'video/mp4']:
            # M4A/MP4 file
            audio = MP4(self.filePath)
            self.title = audio.tags.get('\xa9nam') or audio.tags.get('title')
            self.artist = audio.tags.get('\xa9ART') or audio.tags.get('artist')
            self.album = audio.tags.get('\xa9alb') or audio.tags.get('album')
            self.duration = audio.info.length

        elif self.mimeType == 'audio/flac':
            # FLAC file
            audio = FLAC(self.filePath)
            self.title = audio.tags.get('title')
            self.artist = audio.tags.get('artist')
            self.album = audio.tags.get('album')
            self.duration = audio.info.length

        elif self.mimeType == 'audio/wav':
            # WAV file
            audio = WAVE(self.filePath)
            self.title = audio.tags.get('title')
            self.artist = audio.tags.get('artist')
            self.album = audio.tags.get('album')
            self.duration = audio.info.length

        else:
            raise Exception("Unsupported file format")

        
        if self.duration is not None:
            minutes = int(self.duration // 60)
            seconds = int(self.duration % 60)
            self.duration_formatted = f"{minutes}:{seconds:02}"
        else:
            self.duration_formatted = "Unknown"


        self.title = self.title[0] if self.title else Path(self.filePath).stem
        self.artist = self.artist[0] if self.artist else "Unknown Artist"
        self.album = self.album[0] if self.album else "Unknown Album"
        
        # except MutagenError as e:
        #     print(f"Mutagen error: {e}")
        #     raise
        # except Exception as e:
        #     print(f"Error extracting metadata: {e}")
        #     raise


        # self.title = mutObj.get('\xa9nam') or mutObj.get('TIT2')  # Title (for MP4 and MP3)
        # print(self.title)
        # self.title = self.title[0]
        # self.artist = mutObj.get('\xa9ART') or mutObj.get('TPE1')  # Artist
        # self.artist = self.artist[0]
        # self.album = mutObj.get('\xa9alb') or mutObj.get('TALB')  # Album
        # self.album = self.album[0]

        # self.duration = mutObj.info.length
        # minutes = int(self.duration // 60)
        # seconds = int(self.duration % 60)
        # self.duration_formatted = f"{minutes}:{seconds}"


        cvrData = None
        try:
            mutObj = File(self.filePath)
            
            if mutObj is None:
                raise FileFormatNotSupported(self.mimeType, 'Could not load this file or unsupported format.')
            
            elif self.mimeType == 'audio/mpeg':
                if 'APIC:' in mutObj.tags:
                    # MP3
                    cvrData = mutObj.tags['APIC:'].data
            
            elif self.mimeType in ['audio/mp4', 'audio/m4a']:
                if 'covr' in mutObj:
                    # M4A/MP4
                    cvrData = mutObj['covr'][0]
            
            elif self.mimeType == 'audio/flac':
                if 'metadata_block_picture' in mutObj:
                    # FLAC
                    import base64
                    from mutagen.flac import Picture
                    pic_data = base64.b64decode(mutObj['metadata_block_picture'][0])
                    picture = Picture()
                    picture.parse(pic_data)
                    cvrData = picture.data
            
            elif self.mimeType == 'audio/wav':
                tag = tinytag.TinyTag.get(self.filePath, image=True)           
                cvrData = tag.get_image()
            
            elif self.mimeType == 'audio/ogg' or self.mimeType == 'audio/opus':
                tag = tinytag.TinyTag.get(self.filePath, image=True)           
                cvrData = tag.get_image()
            
            else:
                raise NotImplementedError(f"File format '{self.mimeType}' not supported for cover art extraction.")
        
        except Exception as e:
            print(f"Error extracting cover art: {e}")

    
        self.coverArt = OctaveCoverArt(cvrData)



        # cvrData = None
        # # Extract cover art
        # if 'APIC:' in mutObj.tags:
        #     # MP3
        #     cvrData = mutObj.tags['APIC:'].data
        # elif 'covr' in mutObj:
        #     # M4A/MP4
        #     cvrData = mutObj['covr'][0]

        # elif 'metadata_block_picture' in mutObj:
        #     # FLAC
        #     import base64
        #     from mutagen.flac import Picture
            
        #     pic_data = base64.b64decode(mutObj['metadata_block_picture'][0])
        #     picture = Picture()
        #     picture.parse(pic_data)
        #     cvrData = picture.data

        # elif 'artwork' in mutObj:
        #     # OGG Vorbis (some variations)
        #     cvrData = mutObj['artwork'][0]
        # else:
        #     warn("Octave Engine - Media Framework", "Cover Art Missing", f"Cover Art data not found in {self.filePath}")

        # if cvrData:
        #     self.coverAr  t = CoverArt(cvrData)
        # else: self.coverArt = None


class StreamMediaObject:
    def __init__(self, mediaMetadata:dict) -> None:
        self.watchid = None
        self.views = None
        self.tags = None
        self.upload_date = None
        self.thumbnails = None

        self.stream_url=None
        self.watch_url=None
        self.coverArt = None
        self.title = None
        self.artist = None
        self.duration = None
        self.duration_formatted = None
        self.mimeType = None
        
        
        self.isLiked = False
        self.thumbnail_url = None
        self.isStreamable = True

        self.mediaMetadata = mediaMetadata if mediaMetadata else None
        
        if self.mediaMetadata:
            self.watchid = self.mediaMetadata.get('id')
            self.views = self.mediaMetadata.get('views')
            self.tags = self.mediaMetadata.get('tags')
            self.upload_date = self.mediaMetadata.get('upload_date')
            
            self.thumbnails = self.mediaMetadata.get('thumbnails')
            self.thumbnail_byte_data = None
            self.watch_url=self.mediaMetadata.get('watch_url')

            
            # self.coverArts=self.mediaMetadata.get('thumbnail_bytes')

            # if not isinstance(self.thumbnails, list):
            #     # response = requests.get(self.thumbnails['url'])
            #     # self.thumbnail_bytes = response.content
            #     self.coverArt = OctaveCoverArt(self.thumbnails)

            # else:    
            self.coverArt = OctaveCoverArt(self.thumbnails)
            self.thumbnail_byte_data = self.coverArt.return_coverarts_data()
            
            # self.thumbnail_url=self.mediaMetadata.get('thumbnail_url')

            self.title=self.mediaMetadata.get('title')
            self.artist=self.mediaMetadata.get('artist')
            self.duration=int(self.mediaMetadata.get('duration'))
            self.mimeType=self.mediaMetadata.get('mimeType')
            self.encoding=self.mediaMetadata.get('codec', None)
            self.stream_url=self.mediaMetadata.get('stream_url', None)

            minutes = int(self.duration // 60)
            seconds = int(self.duration % 60)
            
            self.duration_formatted = f"{minutes:02}:{seconds:02}"

    # def __repr__(self):
    #     return self.