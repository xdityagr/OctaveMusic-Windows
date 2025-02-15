"""
QueueObj (queue) -> isshuffle, next, prev, current
PlayerObj  (SongObj) -> Playback
CurrentSongObj (file_path) -> (is_liked, coverArt, title, artist, songLen, in_album )
"""

from socket import timeout
from mutagen.mp4 import MP4
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from mutagen.oggopus import OggOpus

import subprocess
import tinytag
import json
from json import JSONDecodeError
from mutagen import MutagenError

import asyncio
import mimetypes
import filetype
import gc

import multiprocessing as mp

from .errors import *
# from OctaveEngine.audioClient import *

from .definitions import *

from mutagen import File
from PIL import Image
import io
from pathlib import Path
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import io
import threading
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pytubefix import Search
from enum import Enum, auto
from ffpyplayer.player import MediaPlayer

import yt_dlp
import json
from PIL import Image
import requests
from io import BytesIO

import pickle, os

from OctaveEngine.definitions import *
from . import *

import multiprocessing as mp
import threading
import time
from ffpyplayer.player import MediaPlayer

class MASS:
    """OctaveMusic (M)ultiprocessed (A)udio (S)treaming (S)ervice: 
    Service for streaming audio & controlling it in an isolated process."""

    def __init__(self):
        self.player_process = None
        self.control_queue = None

    def _player_worker(self, stream_url, control_queue, volume, update_callback):
        """Worker function running the MediaPlayer in a separate process."""
        print(f"Starting player with stream: {stream_url}")
        try:
            player = MediaPlayer(stream_url, ff_opts={'sync': 'audio'}, timeout=30)
            player.set_volume(volume)

            # Start a thread to call the callback periodically with the playback position
            def position_updater():
                while True:
                    if not control_queue.empty():
                        command = control_queue.get()
                        if command == "STOP":
                            print("Stopping player...")
                            player.close_player()
                            break
                        elif command == "PAUSE":
                            print("Pausing player...")
                            player.set_pause(True)
                        elif command == "RESUME":
                            print("Resuming player...")
                            player.set_pause(False)
                        elif isinstance(command, tuple):
                            if command[0] == "VOLUME":
                                new_volume = command[1]
                                print(f"Setting volume to {new_volume}")
                                player.set_volume(new_volume)
                            elif command[0] == "SEEK":
                                seek_position = command[1]
                                print(f"Seeking to {seek_position} seconds...")
                                player.seek(seek_position)

                    # Update the current position every 100ms
                    if player.get_pts() is not None:
                        current_position_ms = player.get_pts() * 1000  # Convert to milliseconds
                        update_callback(current_position_ms)

                    time.sleep(0.1)  # Prevent busy-waiting

            # Start the position updater thread
            threading.Thread(target=position_updater, daemon=True).start()

            # Keep the player running
            while True:
                if not player.is_playing():
                    break
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Error in player process: {e}")

    def load_stream(self, stream_url, volume=0.5, update_callback=lambda pos: None):
        """Loads a new audio stream by stopping the existing process and starting a new one."""
        self.stop()  # Stop any existing process

        print("Starting new player process...")
        self.control_queue = mp.Queue()
        self.player_process = mp.Process(
            target=self._player_worker,
            args=(stream_url, self.control_queue, volume, update_callback),
        )
        self.player_process.start()

    def stop(self):
        """Stops the player process gracefully."""
        if self.player_process and self.player_process.is_alive():
            print("Stopping player process...")
            self.control_queue.put("STOP")
            self.player_process.join(timeout=2)
            print("Player stopped.")
            self.player_process = None  # Reset the process reference

    def set_pause(self, pause=True):
        """Pauses or resumes playback."""
        if self.player_process and self.player_process.is_alive():
            command = "PAUSE" if pause else "RESUME"
            self.control_queue.put(command)

    def set_volume(self, volume):
        """Adjusts the volume."""
        if self.player_process and self.player_process.is_alive():
            self.control_queue.put(("VOLUME", volume))

    def set_seek(self, seek_position):
        """Seeks to a specified position in seconds."""
        if self.player_process and self.player_process.is_alive():
            self.control_queue.put(("SEEK", seek_position))




class OctaveQueue:
    def __init__(self) -> None:
        self.current_queue = None
        self.current_playing = None
        self.length = None
        self.SAVEDQUEUES_PATH = os.path.join(os.getcwd(), "OctaveEngine/savedQueues/.queue")
    
    def empty(self):
        self.current_queue = []
        self.current_playing = None
        self.length = 0
    def next(self): 
        if self.current_playing[0] != len(self.current_queue)-1 :
            self.current_playing = (self.current_playing[0] + 1, self.current_queue[self.current_playing[0] + 1])
            warn("Octave Engine", "QueueManager:Next", f"Loaded next media, {self.current_playing[1]}")
        elif self.current_playing[0] == len(self.current_queue)-1 :
            self.current_playing = (0, self.current_queue[0])
            warn("Octave Engine", "QueueManager:Previous", f"Unable to load next media. Currently at {self.current_playing[0]}")
        return self.current_playing

    def previous(self): 
        if self.current_playing[0] > 0:
            self.current_playing = (self.current_playing[0] - 1, self.current_queue[self.current_playing[0] - 1])
            warn("Octave Engine", "QueueManager:Previous", f"Loaded previous media, {self.current_playing[1]}")
        else:
            self.current_playing = (self.length -1 , self.current_queue[-1])
            warn("Octave Engine", "QueueManager:Previous", f"Unable to load previous media. Currently at {self.current_playing[0]}")
        return self.current_playing
    def clear(self):
        self.current_queue = None
        self.current_playing = None

    def listAll(self):
        if self.current_queue:
            for i, media in enumerate(self.current_queue):
                warn("Octave Engine", "QueueManager:ListAll", f"[{i+1}] {media}")


    def queueToFile(self, queue, path):
        crr_path = Path(path)
        # crr_path = path if Path.exists(path) else None
        if crr_path:
            if self.isQueueVerified(queue):            
                with open(path, "wb") as f:
                    obj = pickle.dump(queue, f)
                    warn("Octave Engine", "QueueManager:queueToFile", f"'{queue}' saved successful, saved to : {path} ")
            else:   
                warn("Octave Engine", "QueueManager:queueToFile", f"'{queue}' cannot be verified. ")
        else:
            warn("Octave Engine", "QueueManager:queueToFile", f"'{str(path)}' Path does not exist. ")    

    def loadFromFile(self, queueFile):
        try :
            with open(queueFile, "rb") as f:
                self.current_queue = pickle.load(f)
                warn("Octave Engine", "QueueManager:queueToFile", f"'{queueFile}' loaded successfully. ")
                self.current_playing = (0, self.current_queue[0])
                self.length = len(self.current_queue)

        except FileNotFoundError as e:
            warn("Octave Engine", "QueueManager:LoadFromFile", f"'{queueFile}' File Not Found. ")

    def isQueueVerified(self, queue):
        verf = False
        if type(queue) == list and len(queue) >= 1:
            for i in queue:
                if not type(i) == LocalMediaObject:
                    warn("Octave Engine", "QueueManager:queueToFile:Verification", f"{i} is not of type OctaveEngine.LocalMedia, Invalid Queue.")    
                    verf = False
                    break
                else: 
                    verf = True
        else:
            verf = False
            warn("Octave Engine", "QueueManager:queueToFile:Verification", f"Invalid Queue.")  

        return verf  

    def addToQueue(self, LocalMedia):
        if self.current_queue:
            self.current_queue.append(LocalMedia)
            
            self.queueToFile(self.current_queue, self.SAVEDQUEUES_PATH)
            self.loadFromFile(self.SAVEDQUEUES_PATH)
        
    def removeFromQueue(self, index):
        if self.current_queue:
            self.current_queue.pop(index)
            self.queueToFile(self.current_queue, self.SAVEDQUEUES_PATH)
            self.loadFromFile(self.SAVEDQUEUES_PATH)
            

class OctaveMediaController: 
    def __init__(self, parent, debug=False):
        self.parent = parent

        self.isPlaying = False

        self.debug = debug

        self.audio_segment = None
        self.audio_data = None
        self.samplerate = None
        self.channels = None

        self.player_obj = None
        self.stream_player_obj = None

        self.current_position = 0  
        self.buffer_size = 1024
        self.frames_played = 0

        self.lock = threading.Lock()
        self.play_thread = None
        self.position_thread = None
        self.stop_event = threading.Event() 
        self.playback_complete = threading.Event()    

        self.position_callback = None  # Callback for updating position
        self.current_volume = 100
        self.target_volume = 1.0  # Target volume level (0.0 to 1.0)
        self.volume_step = 0.1  # Step size for volume adjustment
        self.volume_change_interval = 0.001  # Time interval for volume changes (seconds)
        self.is_adjusting_volume = False
        self.current_volume = 1.0  # Current volume level
    
        self.isMediaStreamable = False
        self.MediaObject = None
        self.last_pts = -1

        self.prev_callback =None

    def setMedia(self, MediaObject):
        if self.isPlaying: 
            self.stop()
            self.isPlaying = False
            self.stop_event.clear()
            
            

        self.MediaObject = MediaObject

        if self.debug:

            warn("Octave Engine", "Media Playback", f"Media Loaded '{self.MediaObject.title}' By {self.MediaObject.artist}")

        self.current_position = 0

        if self.MediaObject.isStreamable: 
            print('here')
            self.isMediaStreamable = True
            self.__load_audio_from_stream()
            
        else:
            self.isMediaStreamable = False
            self.__load_audio_from_file()


    def play(self): 
        """
        Play method for playing media ( StreamableMedia | LocalMedia )
        """

        self.stop_event.clear()
        self.playback_complete.clear()
        self.isPlaying = True

        self.setVolume(self.current_volume)

        if self.isMediaStreamable:
            self.play_thread = threading.Thread(target=self.__stream_audio, daemon=True)
            self.play_thread.start()

        else:

            if self.audio_data is None:
                self.__load_audio_from_file()
                if self.debug:
                    warn("Octave Engine", "Media Playback", f"Media Playing Now '{self.MediaObject.title}' By {self.MediaObject.artist}")

            # Reset playback state
            self.frames_played = int((self.current_position / 1000) * self.samplerate)  # Seek to the current position


            # Start playback in a new thread
            self.play_thread = threading.Thread(target=self.__play_localaudio)
            self.play_thread.start()


        

        # self.position_thread = threading.Timer(1, self.update_position)
        # self.position_thread.start()
        

        self.position_thread = threading.Thread(target=self.update_position)
        
        self.position_thread.start()

    def update_position(self):
        
        last_update_time = time.perf_counter()
        
        while self.isPlaying and not self.stop_event.is_set():
        
            current_time = time.perf_counter()
            elapsed_time = current_time - last_update_time
            if elapsed_time >= 0.01:
                with self.lock:
                    if self.isMediaStreamable: 
                    
                        # self.current_position = (self.frames_played / self.samplerate) * 1000
                        # self.current_position = (self.frames_played / self.samplerate)*1000
                        
                        stuck, self.last_pts = self.is_playback_stuck(self.last_pts)
                        # stuck = False
                        # self.last_pts = 1
                        if stuck:
                            self.stop()
                            print('playback ended.')
                        else:
                            self.current_position = round(self.last_pts) * 1000
                            # self.current_position = self.last_pts

                        # if self.current_position is not None:
                            # print(f"Current playback position: {self.current_position} seconds")
                        
                        current_position = self.current_position
                        # print(current_position)
                        # current_position = 

                        
                    else:
                        current_position = (self.frames_played / self.samplerate) * 1000  # Convert to milliseconds
            
                    formatted_time = self.format_time(current_position)
                    # print('formatted : ',formatted_time)
                
                    if self.debug : print(Back.BLUE + f"Current Position: " + Back.LIGHTBLUE_EX + f"{formatted_time}" + Back.RESET, end='\r')  # Update position on the same line
                
                    if self.position_callback:


                        # self.position_callback(round(current_position, 4) * 1000)
                    
                        self.position_callback(self.current_position)

                        # print(f'position callback is called. with args [{round(current_position, 4) * 1000}]')
                        # print(f'position callback is called. with args [{self.current_position}]')
                    else:warn('no position callback found')
                    last_update_time = current_time

            time.sleep(1)

    def set_position_callback(self, callback):
        self.position_callback = callback

    def callback(self, outdata, frames, time, status):
        if status:
            print(status, flush=True)

        start_index = int(self.frames_played)
        end_index = start_index + frames

        # Ensure we do not exceed data length
        if end_index > len(self.audio_data):
            end_index = len(self.audio_data)
        
        # Slice data to match the output buffer size
        audio_chunk = self.audio_data[start_index:end_index]

        # Ensure audio_chunk has the right shape for outdata
        if audio_chunk.shape[0] < frames:

            # Padding audio_chunk with zeros if it's smaller than frames (usually occurs at End of data)
            padding = frames - audio_chunk.shape[0]
            audio_chunk = np.vstack([audio_chunk, np.zeros((padding, self.channels), dtype=np.float32)])
        
        audio_chunk *= self.current_volume        
        # with self.lock:
            # outdata[:frames] = audio_chunk

        outdata[:frames] = audio_chunk
        self.frames_played += frames

        # Stop playback if the stop event is set
        if self.stop_event.is_set():
            raise sd.CallbackStop

        # Signal playback completion when data ends
        if end_index >= len(self.audio_data):
            self.playback_complete.set()
            
    def __play_localaudio(self):
        try:
            self.player_obj = sd.OutputStream(
                samplerate=self.samplerate,
                channels=self.channels,
                callback=self.callback,
                blocksize=self.buffer_size
            )

            self.player_obj.start()

            
            # Wait for playback to finish or be 
            while not self.playback_complete.is_set() and not self.stop_event.is_set():
                time.sleep(0.01)  # Short sleep to avoid busy-waiting

            # Ensure the update thread stops
            self.stop_event.set()
            self.position_thread.join(timeout=1)  
            
            
        except Exception as e:
            print(f"Error during playback: {e}")

        finally:
            
            self.isPlaying = False

    def is_playback_stuck(self, last_pts):
        """Check if playback is stuck within a tolerance range."""
        pts = self.stream_player_obj.get_pts()
        

        if pts is None:  # If PTS is None, playback likely ended
            return True, pts
        
        # Inaccuracies might be caused.
        if round(pts) == self.MediaObject.duration:
            return True, pts

        return False, pts

    def __stream_audio(self):
        
        # self.samplerate = self.stream_player_obj.get_metadata()
        
        self.isPlaying = True

        self.frames_played = 0  

        try:
            last_pts = -1
            while not self.playback_complete.is_set() and not self.stop_event.is_set():
                
                frame, val = self.stream_player_obj.get_frame()
                if val == 'eof':
                    print("End of Stream.")
                    break
    
            if not self.stop_event.is_set():
                self.stop_event.set()
                            
            self.position_thread.join(timeout=1)  
                
        except Exception as e:
            print(f"Error during playback: {e}")

        finally:    
            self.isPlaying = False


    def pause(self): 
        """
        Pause media method for pausing media ( StreamableMedia | LocalMedia )
        """
        if self.isMediaStreamable:
            if self.stream_player_obj is not None:
                self.stream_player_obj.set_pause(True)

        else:
            if self.player_obj is not None:
                self.stop_event.set()  # Signal the callback to stop playback
                self.player_obj.stop()  # Stop playback
            
                with self.lock:
                    self.current_position = (self.frames_played / self.samplerate) * 1000  # Convert to milliseconds
            
        self.prev_callback = self.position_callback 

        self.set_position_callback(None)

        if self.debug:
            print(f"Media Paused at {self.format_time(self.current_position)}")

        self.isPlaying = False

    def resume(self): 
        """Resume media method for resuming media from the last position ( StreamableMedia | LocalMedia )
        """
        if self.isMediaStreamable and not self.isPlaying:
            self.stream_player_obj.set_pause(False)

            self.isPlaying = True

        else:
            if self.audio_data is not None:
                if not self.isPlaying:
                    # Restart playback with the updated position
                    self.play()
                    self.isPlaying = True

        self.set_position_callback(self.parent.update_slider_position)
        # self.set_position_callback(self.prev_callback)
        
        if self.debug:
            print(f"Media Resumed from {self.format_time(self.current_position)}")
        
        self.position_thread = threading.Thread(target=self.update_position)
        print('position thread about to start')
        self.position_thread.start()
        
    
    def stop(self):
        """Stop media method for stopping media playback completely. ( StreamableMedia | LocalMedia )
        """
        if self.isMediaStreamable:
            if self.stream_player_obj is not None:
                self.stream_player_obj.set_pause(True)

        else:
            if self.player_obj is not None:
                self.player_obj.stop()  # Stop playback
        
        # self.stop_event.set()  # Signal the callback to stop playback
        self.stop_event.clear()
        self.playback_complete.clear()
        
        # self.position_thread.join()

        if self.debug:
            warn("Octave Engine", "Media Playback", f"Media Stopped.")

        self.current_position = 0
        self.isPlaying = False

    def seek(self, seconds): 
        self.pause()
        print('PAUSED FOR SEEK.')
        if self.isMediaStreamable:
            # self.current_position = seconds
            
            self.stream_player_obj.seek(seconds, relative=False)
            print(f'SEEKED to {seconds}')

        else:
            # Ensure audio is loaded
            if self.audio_segment is None:
                self.load_audio()

            # Check if the position is within valid range
            if seconds < 0 or seconds > len(self.audio_segment):
                raise ValueError("Seek position out of range")

            # Update the current position
            self.current_position = seconds

            # Recalculate frames_played based on the new position
            self.frames_played = int((self.current_position / 1000) * self.samplerate)
            # Update the UI slider to reflect the new position immediately
            if self.position_callback:
                self.position_callback(self.current_position)

        if self.parent:
            print(f'UPDATE SLIDER POS CALLED FOR {seconds}')
            self.parent.update_slider_position(seconds*1000)

        if self.debug:
            print(f"Media Seeked to {self.format_time(self.current_position)}")

    """
    okay so, i am building a music player, it can play audio from stream or from a file. for playing with local file i have defined an update position method which is called in another thread to update the position of the progress bar in the user interface if any, it is as follows : 

    """

    def setVolume(self, VolumeLevel): 
        if 0.0 <= VolumeLevel <= 1.0:
            self.volume_level = VolumeLevel
            if self.isMediaStreamable:
                if self.stream_player_obj is not None:
                    self.stream_player_obj.set_volume(VolumeLevel)

            self.current_volume = VolumeLevel
            print(f"Volume set to {VolumeLevel * 100}%.")
        else:
            print("Volume should be between 0.0 and 1.0.")
    

    def endSession(self): 
        self.stop()
        print("Session ended. Cleaned up.")


    def __load_audio_from_file(self):
        self.audio_segment = AudioSegment.from_file(self.MediaObject.filePath)

        self.samplerate = self.audio_segment.frame_rate
        self.channels = self.audio_segment.channels
        
        # Raw audio audio_data
        self.audio_data = np.array(self.audio_segment.get_array_of_samples())
        
        # reshaping audio_data into 2D array of audio samples for each channel
        self.audio_data = self.audio_data.reshape(-1, self.channels)  

        # Converting to float32 
        self.audio_data = self.audio_data.astype(np.float32) 

        #Normalization of audio to a range of [-1.0, 1.0]
        self.audio_data = self.audio_data / np.max(np.abs(self.audio_data))  # Normalize to [-1.0, 1.0]

    def __load_audio_from_stream(self):
        if self.stream_player_obj:
            
            self.stop()
            try:
                print("Closing current player...")
                self.stream_player_obj.close_player()  # Close the player safely
            except Exception as e:
                print(f"Error closing player: {e}")
            
            del self.stream_player_obj
            print('object set to none')
            gc.collect()
            print('gc collect')
            time.sleep(0.1)
            print('now defining new mediaplayer object')

        for attempt in range(5):
            try:
                self.stream_player_obj = MediaPlayer(self.MediaObject.stream_url,  ff_opts={'sync': 'audio'}, timeout=30, autoexit = True) 
                self.stream_player_obj.set_volume(self.current_volume)
                break
            except Exception as e:
                warn("Octave Audio Stream", f"Attempt [{attempt}] Error initializing player",f"Got {e}, trying again ... ")



    def format_time(self, ms):
        # returns formatted time
        
        minutes = int(ms // 60000)
        seconds = int((ms % 60000) // 1000)
        return f"{minutes:02}:{seconds:02}"
    

class OctaveFetch:
    async def fetchQuery(self, query, results=6, codec=OctaveStreamSupportedCodec.opus, quality=OctaveStreamAudioQuality.WORSE):
        results = self.__search(query=query, fetch=results)
        # results = youtube_search(query, fetch=results)
        result_infos = []

        # for i in results:
        #     print(i)
        
        fetched = await self.getfetchVideoData(results, codec, quality)
        # fetched = self.fe(i, codec, quality)
        for r in fetched:
            result_infos.append(StreamMediaObject(r))

        return result_infos
    
    def __search(self, query, fetch=5):
        response = Search(query)
        results = []
        for i in range(fetch):
            results.append(response.videos[i].watch_url)
            
        return results
    

    async def __fetch_video_data_(self, url, codec, quality):
        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(None, self.fetch_info, url, codec, quality)
        return info

    async def getfetchVideoData(self, urls, codec, quality):
        tasks = [self.__fetch_video_data_(url, codec, quality) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


    def fetch_info(self, url, codec=OctaveStreamSupportedCodec.opus, quality=OctaveStreamAudioQuality.STANDARD):
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extract_flat':True,
            # 'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': f'{codec}',
                'preferredquality': f'{quality.value}',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            
            title = info.get('title', 'Unkown Title')
            channel = info.get('channel', 'Unkown Channel')
            duration = info.get('duration', 'Unknown')
            artist = info.get('creator', 'Unknown Artist')
            release_date = info.get('release_date', None)
            thumbnail_url = info.get('thumbnail', None) 

            response = requests.get(thumbnail_url)
            thumbnail_bytes = response.content


            watch_url = url
            all_info = {'title':title, 'channel':channel, 'duration':duration, 'thumbnail_url':thumbnail_url, 'thumbnail_bytes':thumbnail_bytes,'stream_url':audio_url, 'watch_url':watch_url, 'duration':duration, 'artist':artist, 'release_date': release_date}
            
            return all_info
        


# ocf = OctaveFetch()

# omc = OctaveMediaController(ui=None, debug=True)
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

# # Run the fetchQuery asynchronously in the new loop
# try:
#     time_started = time.time()
#     query_results = loop.run_until_complete(
#         ocf.fetchQuery("the weeknd, starboy kygo remix", results=1)
#     )
# finally:
#     loop.close()

# # omc.setMedia(LocalMedia("C:\\Users\\Aditya\\Projects\\OctaveMusic\\Often.mp3"))
# omc.setMedia(query_results[0])
# print(query_results[0].stream_url)
# omc.play()

# print('after play')