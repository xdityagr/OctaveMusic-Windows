# """
# QueueObj (queue) -> isshuffle, next, prev, current
# PlayerObj  (SongObj) -> Playback
# CurrentSongObj (file_path) -> (is_liked, coverArt, title, artist, songLen, in_album )

# """

# from mutagen.mp4 import MP4
# from mutagen.id3 import ID3
# from mutagen.mp3 import MP3
# from mutagen.mp4 import MP4
# from mutagen.flac import FLAC
# from mutagen.wave import WAVE
# from mutagen.oggopus import OggOpus

# import subprocess
# import tinytag
# import json
# from json import JSONDecodeError
# from mutagen import MutagenError

# import asyncio
# import mimetypes
# import filetype

# # from OctaveEngine.errors import *
# # from OctaveEngine.audioClient import *

# from errors import *
# # from errors import *
# from mutagen import File
# from PIL import Image
# import io
# from pathlib import Path
# import sounddevice as sd
# import numpy as np
# from pydub import AudioSegment
# import io
# import threading
# import time

# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *

# from pytubefix import Search

# from ffpyplayer.player import MediaPlayer

# import yt_dlp
# import json
# from PIL import Image
# import requests
# from io import BytesIO

# import pickle, os

# class Queue:
#     def __init__(self) -> None:
#         self.current_queue = None
#         self.current_playing = None
#         self.length = None
#         self.SAVEDQUEUES_PATH = os.path.join(os.getcwd(), "OctaveEngine/savedQueues/.queue")
    
#     def empty(self):
#         self.current_queue = []
#         self.current_playing = None
#         self.length = 0
#     def next(self): 
#         if self.current_playing[0] != len(self.current_queue)-1 :
#             self.current_playing = (self.current_playing[0] + 1, self.current_queue[self.current_playing[0] + 1])
#             warn("Octave Engine", "QueueManager:Next", f"Loaded next media, {self.current_playing[1]}")
#         elif self.current_playing[0] == len(self.current_queue)-1 :
#             self.current_playing = (0, self.current_queue[0])
#             warn("Octave Engine", "QueueManager:Previous", f"Unable to load next media. Currently at {self.current_playing[0]}")
#         return self.current_playing

#     def previous(self): 
#         if self.current_playing[0] > 0:
#             self.current_playing = (self.current_playing[0] - 1, self.current_queue[self.current_playing[0] - 1])
#             warn("Octave Engine", "QueueManager:Previous", f"Loaded previous media, {self.current_playing[1]}")
#         else:
#             self.current_playing = (self.length -1 , self.current_queue[-1])
#             warn("Octave Engine", "QueueManager:Previous", f"Unable to load previous media. Currently at {self.current_playing[0]}")
#         return self.current_playing
#     def clear(self):
#         self.current_queue = None
#         self.current_playing = None

#     def listAll(self):
#         if self.current_queue:
#             for i, media in enumerate(self.current_queue):
#                 warn("Octave Engine", "QueueManager:ListAll", f"[{i+1}] {media}")


#     def queueToFile(self, queue, path):
#         crr_path = Path(path)
#         # crr_path = path if Path.exists(path) else None
#         if crr_path:
#             if self.isQueueVerified(queue):            
#                 with open(path, "wb") as f:
#                     obj = pickle.dump(queue, f)
#                     warn("Octave Engine", "QueueManager:queueToFile", f"'{queue}' saved successful, saved to : {path} ")
#             else:   
#                 warn("Octave Engine", "QueueManager:queueToFile", f"'{queue}' cannot be verified. ")
#         else:
#             warn("Octave Engine", "QueueManager:queueToFile", f"'{str(path)}' Path does not exist. ")    

#     def loadFromFile(self, queueFile):
#         try :
#             with open(queueFile, "rb") as f:
#                 self.current_queue = pickle.load(f)
#                 warn("Octave Engine", "QueueManager:queueToFile", f"'{queueFile}' loaded successfully. ")
#                 self.current_playing = (0, self.current_queue[0])
#                 self.length = len(self.current_queue)

#         except FileNotFoundError as e:
#             warn("Octave Engine", "QueueManager:LoadFromFile", f"'{queueFile}' File Not Found. ")

#     def isQueueVerified(self, queue):
#         verf = False
#         if type(queue) == list and len(queue) >= 1:
#             for i in queue:
#                 if not type(i) == LocalMedia:
#                     warn("Octave Engine", "QueueManager:queueToFile:Verification", f"{i} is not of type OctaveEngine.LocalMedia, Invalid Queue.")    
#                     verf = False
#                     break
#                 else: 
#                     verf = True
#         else:
#             verf = False
#             warn("Octave Engine", "QueueManager:queueToFile:Verification", f"Invalid Queue.")  

#         return verf  

#     def addToQueue(self, LocalMedia):
#         if self.current_queue:
#             self.current_queue.append(LocalMedia)
            
#             self.queueToFile(self.current_queue, self.SAVEDQUEUES_PATH)
#             self.loadFromFile(self.SAVEDQUEUES_PATH)
        
#     def removeFromQueue(self, index):
#         if self.current_queue:
#             self.current_queue.pop(index)
#             self.queueToFile(self.current_queue, self.SAVEDQUEUES_PATH)
#             self.loadFromFile(self.SAVEDQUEUES_PATH)
            
# # class LocalMediaControl:
#     def __init__(self, ui, debug=True) -> None:
#         self.ui = ui
#         self.isPlaying = False
#         self.debug = debug
#         self.audio_segment = None
#         self.data = None
#         self.samplerate = None
#         self.channels = None
#         self.player_obj = None
#         self.current_position = 0  
#         self.buffer_size = 1024
#         self.frames_played = 0
#         self.lock = threading.Lock()
#         self.play_thread = None
#         self.position_thread = None
#         self.stop_event = threading.Event() 
#         self.playback_complete = threading.Event()    
#         self.position_callback = None  # Callback for updating position
#         self.current_volume = 100
#         self.target_volume = 1.0  # Target volume level (0.0 to 1.0)
#         self.volume_step = 0.1  # Step size for volume adjustment
#         self.volume_change_interval = 0.001  # Time interval for volume changes (seconds)
#         self.is_adjusting_volume = False
#         self.current_volume = 1.0  # Current volume level

#     def __del__(self):
#         self.endSession()

#     def setMedia(self, mediaObject):
#         if self.isPlaying:
#             self.stopMedia()
    
#         self.media = mediaObject
#         if self.debug:
#             warn("Octave Engine", "Media Playback", f"Media Playing Now '{self.media.title}' By {self.media.artist}")

#         self.current_position = 0
#         self.load_audio()


#     def load_audio(self):
#         self.audio_segment = AudioSegment.from_file(self.media.filePath)

#         self.samplerate = self.audio_segment.frame_rate
#         self.channels = self.audio_segment.channels
        
#         # Raw audio data
#         self.data = np.array(self.audio_segment.get_array_of_samples())
        
#         # reshaping data into 2D array of audio samples for each channel
#         self.data = self.data.reshape(-1, self.channels)  

#         # Converting to float32 
#         self.data = self.data.astype(np.float32) 

#         #Normalization of audio to a range of [-1.0, 1.0]
#         self.data = self.data / np.max(np.abs(self.data))  # Normalize to [-1.0, 1.0]


#     def callback(self, outdata, frames, time, status):
#         if status:
#             print(status, flush=True)

#         start_index = int(self.frames_played)
#         end_index = start_index + frames

#         # Ensure we do not exceed data length
#         if end_index > len(self.data):
#             end_index = len(self.data)
        
#         # Slice data to match the output buffer size
#         audio_chunk = self.data[start_index:end_index]

#         # Ensure audio_chunk has the right shape for outdata
#         if audio_chunk.shape[0] < frames:

#             # Padding audio_chunk with zeros if it's smaller than frames (usually occurs at End of data)
#             padding = frames - audio_chunk.shape[0]
#             audio_chunk = np.vstack([audio_chunk, np.zeros((padding, self.channels), dtype=np.float32)])
        
#         audio_chunk *= self.current_volume        
#         # with self.lock:
#             # outdata[:frames] = audio_chunk

#         outdata[:frames] = audio_chunk
#         self.frames_played += frames

#         # Stop playback if the stop event is set
#         if self.stop_event.is_set():
#             raise sd.CallbackStop

#         # Signal playback completion when data ends
#         if end_index >= len(self.data):
#             self.playback_complete.set()

#     def playMedia(self, progressBar=None):
#         if self.data is None:
#             self.load_audio()
#             if self.debug:
#                 warn("Octave Engine", "Media Playback", f"Media Playing Now '{self.media.title}' By {self.media.artist}")

#         # Reset playback state
#         self.frames_played = int((self.current_position / 1000) * self.samplerate)  # Seek to the current position
#         self.stop_event.clear()
#         self.playback_complete.clear()
#         self.isPlaying = True
#         self.set_volume(self.current_volume)
#         def play_audio():
#             try:
#                 self.player_obj = sd.OutputStream(
#                     samplerate=self.samplerate,
#                     channels=self.channels,
#                     callback=self.callback,
#                     blocksize=self.buffer_size
#                 )

#                 self.player_obj.start()
#                 self.position_thread = threading.Thread(target=self.update_position)
#                 self.position_thread.start()

#                 # Wait for playback to finish or be 
#                 while not self.playback_complete.is_set() and not self.stop_event.is_set():
#                     time.sleep(0.01)  # Short sleep to avoid busy-waiting

#                 # Ensure the update thread stops
#                 self.stop_event.set()
#                 self.position_thread.join(timeout=1)  
                
                
#             except Exception as e:
#                 print(f"Error during playback: {e}")
#             finally:
#                 self.isPlaying = False

#         # Start playback in a new thread
#         self.play_thread = threading.Thread(target=play_audio)
#         self.play_thread.start()

#     def pauseMedia(self):
#         if self.player_obj is not None:
#             self.stop_event.set()  # Signal the callback to stop playback
#             self.player_obj.stop()  # Stop playback
        
#             with self.lock:
#                 self.current_position = (self.frames_played / self.samplerate) * 1000  # Convert to milliseconds
        
#             self.set_position_callback(None)

#             if self.debug:
#                 print(f"Media Paused at {self.format_time(self.current_position)}")

#         self.isPlaying = False

#     def stopMedia(self):
#         if self.player_obj is not None:
#             self.stop_event.set()  # Signal the callback to stop playback
#             self.player_obj.stop()  # Stop playback
#             if self.debug:
#                 warn("Octave Engine", "Media Playback", f"Media Stopped.")

#         self.current_position = 0
#         self.isPlaying = False

#     def resumeMedia(self):
#         if self.data is not None:
#             if not self.isPlaying:
#                 if self.debug:
#                     print(f"Media Resumed from {self.format_time(self.current_position)}")
#                 # Restart playback with the updated position
#                 self.playMedia()
#                 self.isPlaying = True
#                 # Set up the position callback to update the UI
#                 self.set_position_callback(self.update_ui_position)

#     def update_ui_position(self, position_ms):
#         # Use the UI instance to update the progress slider
#         if self.ui:
#             self.ui.update_slider_position(position_ms)

# #     def seekMedia(self, position_ms):
# #         # if self.audio_segment is None:
# #         #     self.load_audio()  # Ensure audio is loaded before seeking

# #         # if self.isPlaying:
# #         #     self.stop_event.set()  # Stop current playback
# #         #     self.player_obj.stop()
# #         #     self.isPlaying = False

# #         # if position_ms < 0 or position_ms > len(self.audio_segment):
# #         #     raise ValueError("Seek position out of range")

# #         # # Update current position and reset frames played
# #         # self.current_position = position_ms
# #         # if self.debug:
# #         #     warn("Media playback", f"Media Seeked to {self.format_time(self.current_position)}")
# #         # self.frames_played = int((self.current_position / 1000) * self.samplerate)

# #         # self.playMedia()  # Restart playback from the new position
# # # Ensure audio is loaded
# #         if self.audio_segment is None:
# #             self.load_audio()

# #         # Check if the position is within valid range
# #         if position_ms < 0 or position_ms > len(self.audio_segment):
# #             raise ValueError("Seek position out of range")

# #         # Stop current playback if it's playing
# #         if self.isPlaying:
# #             self.stop_event.set()
# #             self.player_obj.stop()
# #             self.isPlaying = False

# #         # Update the current position
# #         self.current_position = position_ms

# #         # Calculate the number of frames to skip
# #         self.frames_played = int((self.current_position / 1000) * self.samplerate)

# #         # Restart playback from the new position
# #         self.playMedia()

# #         # Update the UI slider to reflect the new position
# #         if self.position_callback:
# #             self.position_callback(self.current_position)

# #         if self.debug:
# #             print(f"Media Seeked to {self.format_time(self.current_position)}")
            

#     def seekMedia(self, position_ms):
#         # Ensure audio is loaded
#         if self.audio_segment is None:
#             self.load_audio()

#         # Check if the position is within valid range
#         if position_ms < 0 or position_ms > len(self.audio_segment):
#             raise ValueError("Seek position out of range")

#         # Stop current playback if it's playing
#         if self.isPlaying:
#             self.stop_event.set()
#             self.player_obj.stop()
#             self.isPlaying = False

#         # Update the current position
#         self.current_position = position_ms

#         # Recalculate frames_played based on the new position
#         self.frames_played = int((self.current_position / 1000) * self.samplerate)
#         # Update the UI slider to reflect the new position immediately
#         if self.position_callback:
#             self.position_callback(self.current_position)
#         if self.ui:
#             self.ui.update_slider_position(position_ms)

#         # Restart playback from the new position
#         # self.resumeMedia()

#         if self.debug:
#             print(f"Media Seeked to {self.format_time(self.current_position)}")


#     def format_time(self, ms):
#         # returns formatted time
#         minutes = int(ms // 60000)
#         seconds = int((ms % 60000) // 1000)
#         return f"{minutes:02}:{seconds:02}"

#     def endSession(self):
#         if self.player_obj is not None:
#             self.stop_event.set()
#             self.player_obj.stop()
#             self.player_obj.close()
#             if self.debug:
#                 warn("Octave Engine", "Media Playback", f"Media Playback Session Ended.")

#             self.current_position = 0
#             self.isPlaying = False

#         if self.play_thread is not None:
#             self.play_thread.join(timeout=1)  # Wait for the thread to terminate

#         if self.position_thread is not None:
#             self.position_thread.join(timeout=1)


#     # def update_position(self):
#     #     while self.isPlaying and not self.stop_event.is_set():
#     #         with self.lock:
#     #             self.current_position = (self.frames_played / self.samplerate) * 1000
#     #             formatted_time = self.format_time(self.current_position)
#     #             if self.debug:
#     #                 print(Back.BLUE + f"Current Position: " + Back.LIGHTBLUE_EX + f"{formatted_time}" + Back.RESET, end='\r')  # Update position on the same line
#     #         time.sleep(0.1)  # Adjust the sleep time for your needs

#     def update_position(self):
#         last_update_time = time.perf_counter()
        
#         while self.isPlaying and not self.stop_event.is_set():
#             current_time = time.perf_counter()
#             elapsed_time = current_time - last_update_time
#             if elapsed_time >= 0.01:
#                 with self.lock:
#                     current_position = (self.frames_played / self.samplerate) * 1000  # Convert to milliseconds
#                     formatted_time = self.format_time(current_position)
#                     if self.debug : print(Back.BLUE + f"Current Position: " + Back.LIGHTBLUE_EX + f"{formatted_time}" + Back.RESET, end='\r')  # Update position on the same line
                
#                 if self.position_callback:
#                     self.position_callback(current_position)

#                 last_update_time = current_time
#             # time.sleep(0.01)/

#     def set_position_callback(self, callback):
#         self.position_callback = callback


#     def set_volume(self, volume_level):
#         self.target_volume = volume_level

#         if self.target_volume < 0.0:
#             self.target_volume = 0.0
#         elif self.target_volume > 1.0:
#             self.target_volume = 1.0
        
#         if not self.is_adjusting_volume:
#             self.is_adjusting_volume = True
#             self.volume_adjust_thread = threading.Thread(target=self.adjust_volume)
#             self.volume_adjust_thread.start()

#     def adjust_volume(self):
#         while self.is_adjusting_volume:
#             if abs(self.target_volume - self.current_volume) < self.volume_step:
#                 self.current_volume = self.target_volume
#                 self.is_adjusting_volume = False
#             else:
#                 if self.target_volume > self.current_volume:
#                     self.current_volume += self.volume_step
#                     if self.current_volume > self.target_volume:
#                         self.current_volume = self.target_volume
#                 else:
#                     self.current_volume -= self.volume_step
#                     if self.current_volume < self.target_volume:
#                         self.current_volume = self.target_volume

#             time.sleep(self.volume_change_interval)



# # class StreamMediaControl:
# #     def __init__(self, ui=None, debug=True):
# #         self.ui = ui if ui else None
# #         self.debug = debug
# #         self.current_media = None
# #         self.current_position = 0
# #         self.player = None
# #         self.isPlaying = False
# #         self.paused = False
# #         self.current_thread = None
# #         self.volume_level = 1.0
# #         self.stop_flag = False

    
# #     def saveToRecents(self):pass

# #     def update_slider(self, current_position):
# #         """Update the QSlider based on the current playback position."""
# #         # Fetch the total duration of the media (this could be from metadata if available)
# #         if self.duration == 0:
# #             self.duration = self.player.get_metadata()['duration']
# #             self.ui.progress.setRange(0, int(self.duration))  # Set slider range to media duration

# #         # Update slider with the current playback position
# #         self.ui.progress.setValue(int(current_position))
        
# #     async def fetchQuery(self, query, results=6, codec=OctaveStreamSupportedCodec.m4a, quality=OctaveStreamAudioQuality.STANDARD):
# #         results = self.__search(query=query, fetch=results)
# #         # results = youtube_search(query, fetch=results)
# #         result_infos = []
        
# #         # for i in results:
# #         #     print(i)
        
# #         fetched = await self.getfetchVideoData(results, codec, quality)
# #         # fetched = self.fe(i, codec, quality)
# #         for r in fetched:
# #             result_infos.append(StreamMedia(r))

# #         return result_infos

# #     def setMedia(self, StreamMediaObject) :
# #         self.media = StreamMediaObject
# #         self.player = MediaPlayer(self.media.stream_url,  ff_opts={'sync': 'audio'})
# #         self.player.set_volume(self.volume_level)

# #     def __search(self, query, fetch=5):
# #         response = Search(query)
# #         results = []
# #         for i in range(fetch):
# #             results.append(response.videos[i].watch_url)
            
# #         return results
    

# #     async def __fetch_video_data_(self, url, codec, quality):
# #         loop = asyncio.get_event_loop()
# #         info = await loop.run_in_executor(None, self.fetch_info, url, codec, quality)
# #         return info

# #     async def getfetchVideoData(self, urls, codec, quality):
# #         tasks = [self.__fetch_video_data_(url, codec, quality) for url in urls]
# #         results = await asyncio.gather(*tasks)
# #         return results


# #     def fetch_info(self, url, codec=OctaveStreamSupportedCodec.m4a, quality=OctaveStreamAudioQuality.STANDARD):
# #         ydl_opts = {
# #             'format': 'bestaudio/best',
# #             'noplaylist': True,
# #             'quiet': True,
# #             'extract_flat':True,
# #             # 'outtmpl': '%(title)s.%(ext)s',
# #             'postprocessors': [{
# #                 'key': 'FFmpegExtractAudio',
# #                 'preferredcodec': f'{codec}',
# #                 'preferredquality': f'{quality.value}',
# #             }],
# #         }

# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=False)
# #             audio_url = info['url']

# #             title = info.get('title', 'Unkown Title')
# #             channel = info.get('channel', 'Unkown Channel')
# #             duration = info.get('duration', 'Unknown')
# #             artist = info.get('creator', 'Unknown Artist')
# #             release_date = info.get('release_date', None)
# #             thumbnail_url = info.get('thumbnail', None) 

# #             response = requests.get(thumbnail_url)
# #             thumbnail_bytes = response.content


# #             watch_url = url
# #             all_info = {'title':title, 'channel':channel, 'duration':duration, 'thumbnail_url':thumbnail_url, 'thumbnail_bytes':thumbnail_bytes,'stream_url':audio_url, 'watch_url':watch_url, 'duration':duration, 'artist':artist, 'release_date': release_date}
            
# #             return all_info
        
# #     def playMedia(self):
# #         self.isPlaying = True
# #         self.paused = False
# #         self.stop_flag = False

# #         # Start playback in a separate thread
# #         self.current_thread = threading.Thread(target=self._play_audio, daemon=True)
# #         self.current_thread.start()

# #     def _play_audio(self):
# #         while self.isPlaying:
# #             if not self.paused:
# #                 val, frame = self.player.get_frame()

# #                 if val == 'eof' or self.stop_flag:
# #                     print("End of stream reached.")
# #                     self.stop()
# #                     break
# y
# #                 if isinstance(frame, dict) and 'audio' in frame:
# #                     audio_frame, pts = frame['audio']
# #                     if audio_frame is not None:
# #                         current_position = self.player.get_pts()
# #                         if self.ui:
# #                             self.update_slider(current_position)

# #                 time.sleep(0.01)  # Prevent CPU hogging

# #             time.sleep(0.01)  # Prevent CPU hogging

# #     def pauseMedia(self):
# #         if self.isPlaying and not self.paused:
# #             self.paused = True
# #             self.player.set_pause(True)
# #             print("Paused playback.")

# #     def resumeMedia(self):
# #         if self.isPlaying and self.paused:
# #             self.paused = False
# #             self.player.set_pause(False)
# #             print("Resumed playback.")

# #     def stopMedia(self):
# #         if self.isPlaying:
# #             self.isPlaying = False
# #             self.stop_flag = True
# #             if self.current_thread:
# #                 self.current_thread.join()
# #             print("Stopped playback.")

# #     def seekMedia(self, seconds):
# #         if self.isPlaying:
# #             print(f"Seeking to {seconds} seconds...")
# #             self.player.seek(seconds, relative=False)

# #     def end_session(self):
# #         self.stop()
# #         print("Session ended. Cleaned up.")

# #     def set_volume(self, volume_level):
# #         if 0.0 <= volume_level <= 1.0:
# #             self.volume_level = volume_level
# #             if self.player is not None:
# #                 self.player.set_volume(volume_level)
# #                 print(f"Volume set to {volume_level * 100}%.")

# #         else:
# #             print("Volume should be between 0.0 and 1.0.")

# class CoverArt:
#     def __init__(self, coverArtData) -> None:
#         self.DEFAULT_ART = "resources\i.png"
#         self.coverArtData = coverArtData if coverArtData else None

#         self.quality_levels=[100, 85, 70, 50, 30]
        
#     def save(self, name,quality=100, path=None):
#         if self.coverArtData:
#             image = Image.open(io.BytesIO(self.coverArtData))
#             output_filename = f'{name}.jpg'
#             if path:
#                 output_filepath = Path.joinpath(Path(path), output_filename)
#             else:
#                 output_filepath = output_filename
#             if quality in self.quality_levels:
#                 image.save(output_filepath, format='JPEG', quality=quality)

#     def return_coverArtAsBytes(self):
#         return self.coverArtData if self.coverArtData else None
    
#     def return_designed_pixmap(self, size=50, radius=25):
#         if self.coverArtData:
#             pixmap = QPixmap()
#             pixmap.loadFromData(self.coverArtData) 
#         else:
#             pixmap = QPixmap(self.DEFAULT_ART)
#         # Step 1: Resize the pixmap to 50x50
#         resized_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

#         # Step 2: Create a mask for rounded corners
#         rounded_pixmap = QPixmap(size, size)
#         rounded_pixmap.fill(Qt.transparent)  # Make background transparent

#         painter = QPainter(rounded_pixmap)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Draw a rounded rectangle (the mask)
#         painter.setBrush(QBrush(Qt.black))
#         painter.drawRoundedRect(QRect(0, 0, size, size), radius, radius)

#         # Set the mask to the resized pixmap
#         painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
#         painter.drawPixmap(0, 0, resized_pixmap)
#         painter.end()

#         return rounded_pixmap
        
# class ExtMetadata:
#     def __init__(self):
#         self.match  = None
#         self.external_metadata_path = os.path.join(os.getcwd(), "OctaveEngine/Data/external_metadata.json")        
#         self.current_metadata = self.load_external_metadata()
        
#     def getMetadatafromData(self, data):
#         if self.current_metadata['mediaData'] != []:
#             for i, element in enumerate(self.current_metadata['mediaData']):
#                 if element['title'] == data.title and element['fpath'] == data.filePath and element['artist'] == data.artist:
#                     self.match = (i, element)
#                 else:
#                     self.match = None
#                     self.commit_external_metadata(data)
#         else:
#             self.commit_external_metadata(data)

#         return self.match
        
#     def load_external_metadata(self):
#         obj = None
#         if os.path.exists(self.external_metadata_path):
#             try:
#                 with open(self.external_metadata_path, "r") as f:
#                     obj = json.load(f)
                
#                 return obj
#             except JSONDecodeError as e:
#                 os.remove(self.external_metadata_path)
#                 self.create_external_metadata()
#                 self.load_external_metadata()
#         else:
#             self.create_external_metadata()
#             self.load_external_metadata()

#     def commit_external_metadata(self, data):
#         if self.match == None:
#             self.current_metadata['mediaData'].append({'title':data.title, 'fpath':data.filePath, 'artist':data.artist, 'isLiked':data.isLiked})
#         else:
#             self.current_metadata['mediaData'][self.match[0]]['isLiked'] = data.isLiked

#         with open(self.external_metadata_path, "w") as jb:
#             json.dump(self.current_metadata, jb, indent=4)

#     def change_metadata(self, new):
#         if self.current_metadata['mediaData'] != []:
#             for i, element in enumerate(self.current_metadata['mediaData']):
#                 if element['title'] == new.title and element['fpath'] == new.filePath and element['artist'] == new.artist:
#                     self.match = (i, element)
#                 else:
#                     self.match = None
        
#         self.match['isLiked'] = new.isLiked
#         self.commit_external_metadata()
        
#     def create_external_metadata(self):
#         with open(self.external_metadata_path, "w") as j:
#             temp= {"mediaData" : []}
#             json.dump(temp, j, indent=4)


# class StreamMedia:
#     def __init__(self, mediaMetadata:dict) -> None:
#         self.stream_url=None
#         self.watch_url=None
#         self.coverArt = None
#         self.title = None
#         self.artist = None
#         self.duration = None
#         self.duration_formatted = None
#         self.mimeType = None
#         self.encoding = None
#         self.mimeType = None
#         self.isLiked = False
#         self.thumbnail_url = None
#         self.isStreamable = True

#         self.mediaMetadata = mediaMetadata if mediaMetadata else None
        
#         if self.mediaMetadata:
#             self.watch_url=self.mediaMetadata.get('watch_url')
#             self.coverArt=self.mediaMetadata.get('thumbnail_bytes')
#             self.coverArt = CoverArt(self.coverArt)
#             self.thumbnail_url=self.mediaMetadata.get('thumbnail_url')
#             self.title=self.mediaMetadata.get('title')
#             self.artist=self.mediaMetadata.get('channel')
#             self.duration=self.mediaMetadata.get('duration')
#             self.mimeType=self.mediaMetadata.get('format')
#             self.encoding=self.mediaMetadata.get('codec')
#             self.stream_url=self.mediaMetadata.get('stream_url')
        
# class LocalMedia:
#     def __init__(self, fpath=None) -> None:
#         self.filePath = fpath
#         self.coverArt = None
#         self.title = None
#         self.artist = None
#         self.duration = None
#         self.duration_formatted = None
#         self.mimeType = None
#         self.encoding = None
#         self.mimeType =filetype.guess(self.filePath).mime
#         self.isLiked = False
#         self.isStreamable = False
#         # self.external_metadata_ctx = ExtMetadata()
#         # self.ext_metadata = self.external_metadata_ctx.getMetadatafromData(self)
#         # print(self.ext_metadata)
        
      
#         print(self.mimeType)
        
#         self.extractMetadata()
#         # print('title ', self.title, '\nalbum ', self.album, '\nartist', self.artist,'\nmimeType ',  self.mimeType)

#         if self.coverArt:
#             self.coverArt.save('cover_art_30', quality=30)

    

#     def __repr__(self):
#         return (f"Octave Engine:Media Object -> title={self.title!r}, artist={self.artist!r}, "f"duration={self.duration_formatted!r}, mimeType={self.mimeType!r}, "f"filePath={self.filePath!r})")

#     def extractMetadata(self):
#         mutObj = File(self.filePath)
#         if mutObj is None:
#             raise FileFormatNotSupported(self.mimeType, 'Could not load this file or unsupported format.')
        
#         # try:
#             # if self.mimeType == 'mp3':
#             #     # Handle MP3 files
#             #     audio = MP3(self.filePath, ID3=ID3)
#             #     self.title = audio.tags.get('TIT2') or audio.tags.get('\xa9nam')
#             #     self.artist = audio.tags.get('TPE1') or audio.tags.get('\xa9ART')
#             #     self.album = audio.tags.get('TALB') or audio.tags.get('\xa9alb')
#             #     self.duration = audio.info.length
            
#             # elif self.mimeType == 'm4a':
#             #     # Handle M4A files
#             #     audio = MP4(self.filePath)
#             #     self.title = audio.tags.get('\xa9nam') or audio.tags.get('title')
#             #     self.artist = audio.tags.get('\xa9ART') or audio.tags.get('artist')
#             #     self.album = audio.tags.get('\xa9alb') or audio.tags.get('album')
#             #     self.duration = audio.info.length
            
#             # elif self.mimeType == 'flac':
#             #     # Handle FLAC files
#             #     audio = FLAC(self.filePath)
#             #     self.title = audio.tags.get('title')
#             #     self.artist = audio.tags.get('artist')
#             #     self.album = audio.tags.get('album')
#             #     self.duration = audio.info.length
            
#             # elif self.mimeType == 'wav':
#             #     # Handle WAV files
#             #     audio = WAVE(self.filePath)
#             #     self.title = audio.tags.get('title')
#             #     self.artist = audio.tags.get('artist')
#             #     self.album = audio.tags.get('album')
#             #     self.duration = audio.info.length
            
#             # elif self.mimeType == 'opus':
#             #     # Handle OPUS files (may need additional libraries)
#             #     raise NotImplementedError("OPUS files are not natively supported..")
#         warn("MIME TYPE", "MIME TYPE IS", self.mimeType)
#         if self.mimeType == 'audio/ogg' or self.mimeType == 'audio/opus':

#             tag = tinytag.TinyTag.get(self.filePath)
#             # image_data = tag.get_image()

#             self.title = tag.title
#             self.artist = tag.artist
#             self.album = tag.album
#             self.duration = tag.duration
            
#         elif self.mimeType == 'audio/mpeg':
#             # MP3 file
#             audio = MP3(self.filePath, ID3=ID3)
#             self.title = audio.tags.get('TIT2') or audio.tags.get('\xa9nam')
#             self.artist = audio.tags.get('TPE1') or audio.tags.get('\xa9ART')
#             self.album = audio.tags.get('TALB') or audio.tags.get('\xa9alb')
#             self.duration = audio.info.length
            

#         elif self.mimeType in ['audio/mp4', 'audio/m4a', 'video/m4a', 'video/mp4']:
#             # M4A/MP4 file
#             audio = MP4(self.filePath)
#             self.title = audio.tags.get('\xa9nam') or audio.tags.get('title')
#             self.artist = audio.tags.get('\xa9ART') or audio.tags.get('artist')
#             self.album = audio.tags.get('\xa9alb') or audio.tags.get('album')
#             self.duration = audio.info.length

#         elif self.mimeType == 'audio/flac':
#             # FLAC file
#             audio = FLAC(self.filePath)
#             self.title = audio.tags.get('title')
#             self.artist = audio.tags.get('artist')
#             self.album = audio.tags.get('album')
#             self.duration = audio.info.length

#         elif self.mimeType == 'audio/wav':
#             # WAV file
#             audio = WAVE(self.filePath)
#             self.title = audio.tags.get('title')
#             self.artist = audio.tags.get('artist')
#             self.album = audio.tags.get('album')
#             self.duration = audio.info.length

#         else:
#             raise Exception("Unsupported file format")

        
#         if self.duration is not None:
#             minutes = int(self.duration // 60)
#             seconds = int(self.duration % 60)
#             self.duration_formatted = f"{minutes}:{seconds:02}"
#         else:
#             self.duration_formatted = "Unknown"


#         self.title = self.title[0] if self.title else Path(self.filePath).stem
#         self.artist = self.artist[0] if self.artist else "Unknown Artist"
#         self.album = self.album[0] if self.album else "Unknown Album"
        
#         # except MutagenError as e:
#         #     print(f"Mutagen error: {e}")
#         #     raise
#         # except Exception as e:
#         #     print(f"Error extracting metadata: {e}")
#         #     raise


#         # self.title = mutObj.get('\xa9nam') or mutObj.get('TIT2')  # Title (for MP4 and MP3)
#         # print(self.title)
#         # self.title = self.title[0]
#         # self.artist = mutObj.get('\xa9ART') or mutObj.get('TPE1')  # Artist
#         # self.artist = self.artist[0]
#         # self.album = mutObj.get('\xa9alb') or mutObj.get('TALB')  # Album
#         # self.album = self.album[0]

#         # self.duration = mutObj.info.length
#         # minutes = int(self.duration // 60)
#         # seconds = int(self.duration % 60)
#         # self.duration_formatted = f"{minutes}:{seconds}"


#         cvrData = None
#         try:
#             mutObj = File(self.filePath)
            
#             if mutObj is None:
#                 raise FileFormatNotSupported(self.mimeType, 'Could not load this file or unsupported format.')
            
#             elif self.mimeType == 'audio/mpeg':
#                 if 'APIC:' in mutObj.tags:
#                     # MP3
#                     cvrData = mutObj.tags['APIC:'].data
            
#             elif self.mimeType in ['audio/mp4', 'audio/m4a']:
#                 if 'covr' in mutObj:
#                     # M4A/MP4
#                     cvrData = mutObj['covr'][0]
            
#             elif self.mimeType == 'audio/flac':
#                 if 'metadata_block_picture' in mutObj:
#                     # FLAC
#                     import base64
#                     from mutagen.flac import Picture
#                     pic_data = base64.b64decode(mutObj['metadata_block_picture'][0])
#                     picture = Picture()
#                     picture.parse(pic_data)
#                     cvrData = picture.data
            
#             elif self.mimeType == 'audio/wav':
#                 tag = tinytag.TinyTag.get(self.filePath, image=True)           
#                 cvrData = tag.get_image()
            
#             elif self.mimeType == 'audio/ogg' or self.mimeType == 'audio/opus':
#                 tag = tinytag.TinyTag.get(self.filePath, image=True)           
#                 cvrData = tag.get_image()
            
#             else:
#                 raise NotImplementedError(f"File format '{self.mimeType}' not supported for cover art extraction.")
        
#         except Exception as e:
#             print(f"Error extracting cover art: {e}")

    
#         self.coverArt = CoverArt(cvrData)



#         # cvrData = None
#         # # Extract cover art
#         # if 'APIC:' in mutObj.tags:
#         #     # MP3
#         #     cvrData = mutObj.tags['APIC:'].data
#         # elif 'covr' in mutObj:
#         #     # M4A/MP4
#         #     cvrData = mutObj['covr'][0]

#         # elif 'metadata_block_picture' in mutObj:
#         #     # FLAC
#         #     import base64
#         #     from mutagen.flac import Picture
            
#         #     pic_data = base64.b64decode(mutObj['metadata_block_picture'][0])
#         #     picture = Picture()
#         #     picture.parse(pic_data)
#         #     cvrData = picture.data

#         # elif 'artwork' in mutObj:
#         #     # OGG Vorbis (some variations)
#         #     cvrData = mutObj['artwork'][0]
#         # else:
#         #     warn("Octave Engine - Media Framework", "Cover Art Missing", f"Cover Art data not found in {self.filePath}")

#         # if cvrData:
#         #     self.coverAr  t = CoverArt(cvrData)
#         # else: self.coverArt = None



# # media = Media('C:/Users/Aditya/Projects/OctaveMusic/Iraaday.m4a')
# # player = MediaControl()
# # # player.setMedia(media)
# # # time.sleep(5)
# # # player.seekMedia(30000)
# # # time.sleep(5)
# # media2 = Media('C:/Users/Aditya/Projects/OctaveMusic/leanonyou.m4a')
# # player.setMedia(media2)
# # player.playMedia()

# # import time
# # audio_player = StreamMediaControl()
# # queries = audio_player.fetchQuery('starboy the weeknd', results=1)
# # audio_player.setMedia(queries[0])
# # print(audio_player.media.stream_url)
# # i = Image.open(BytesIO(audio_player.media.coverArt))
# # i.show()

# # audio_player.playMedia()

# # try:
# #     # Simulating user actions
# #     time.sleep(10)

# # except KeyboardInterrupt:
# #     audio_player.stopMedia()
# #     print("Stopped isPlaying.")