# import yt_dlp
# import json
# from PIL import Image
# import requests
# from io import BytesIO
# from pydub import AudioSegment
# from pydub.playback import play
# import re, requests, subprocess, urllib.parse, urllib.request
# from bs4 import BeautifulSoup

# def search_from_query(query, fetch=1):
#     query_string = urllib.parse.urlencode({"search_query": query})
#     formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
#     search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
#     clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
#     clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

#     inspect = BeautifulSoup(clip.content, "html.parser")
#     yt_title = inspect.find_all("meta", property="og:title")

#     for concatMusic1 in yt_title:
#         pass

#     # print((concatMusic1['content']))
#     return clip2

# def stream_audio_from_youtube_music(url):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'noplaylist': True,
#         'quiet': True,
#         'outtmpl': '%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'm4a',
#             'preferredquality': '320',
#         }],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         audio_url = info['url']
#         title = info['title']
#         thumbnail_url = info.get('thumbnail')  # This fetches the thumbnail
#         return audio_url, title, thumbnail_url

# def display_thumbnail(thumbnail_url):
#     response = requests.get(thumbnail_url)
#     img = Image.open(BytesIO(response.content))
#     img.show()  # Displays the thumbnail image

# # response = requests.get(stream_url, stream=True)
# # # print(response)
# # with io.BytesIO() as buffer:
# #     for chunk in response.iter_content(chunk_size=1024):
# #         buffer.write(chunk)
# #         buffer.seek(0)
# #         audio_segment = AudioSegment.from_file(buffer)
# #         play(audio_segment)
# #         # buffer.close()

# import requests
# import numpy as np
# import sounddevice as sd
# from pydub import AudioSegment
# import io


# def stream_audio(stream_url):
#     try:
        
#         response = requests.get(stream_url, stream=True)
#         response.raise_for_status()  # Check for request errors

#         # Buffer the audio data
#         audio_data = io.BytesIO()
#         print("stream[writing chunks]")
#         for chunk in response.iter_content(chunk_size=4096):
#             audio_data.write(chunk)
#         print("stream[writing chunks: DONE]")
#         print("stream[playing: NOW]")
#         audio_data.seek(0)  # Reset to the beginning of the buffer

#         # Load the audio segment
#         audio_segment = AudioSegment.from_file(audio_data, format='webm')  # Adjust format as needed

#         # Debug prints
#         print("Duration:", audio_segment.duration_seconds)
#         print("Channels:", audio_segment.channels)
#         print("Sample Rate:", audio_segment.frame_rate)

#         # Convert to numpy array
#         samples = np.array(audio_segment.get_array_of_samples())

#         # Normalize samples
#         if audio_segment.channels == 2:
#             samples = samples.reshape((-1, 2))  # Reshape for stereo audio
#         samples = samples / np.max(np.abs(samples))  # Normalize

#         # Play the audio
#         sd.play(samples, samplerate=audio_segment.frame_rate)
#         sd.wait()  # Wait until the audio is done playing

#     except Exception as e:
#         print("Error playing audio:", e)

# # def stream_audio_without_buffer(stream_url):
# #     response = requests.get(stream_url, stream=True)

# #     # Set up the audio stream parameters
# #     sample_rate = 44100  # Standard sample rate
# #     channels = 2  # Change based on your audio stream (1 for mono, 2 for stereo)

# #     # Create a RawOutputStream for playback
# #     with sd.RawOutputStream(samplerate=sample_rate, channels=channels, dtype='float32') as stream:
# #         # Read and write audio data in chunks
# #         for chunk in response.iter_content(chunk_size=4096):
# #             if chunk:
# #                 # Convert chunk to the appropriate format
# #                 audio_data = np.frombuffer(chunk, dtype='float32')  # Adjust dtype as needed
# #                 stream.write(audio_data)



# # query = input("> Enter Your Query: ")
# # url  = search_from_query(query)
# # audio_url, title, thumbnail_url = stream_audio_from_youtube_music(url)
# # print("Found match : ",title, " With URL : ", url)
# # print("fetch audio_stream_url , ", audio_url)
# # print("displaying thumbnail .. ")
# # display_thumbnail(thumbnail_url)
# # print("streaming start now... ")
# # url = "https://rr4---sn-ci5gup-qxaed.googlevideo.com/videoplayback?expire=1727056389&ei=pXXwZtW6FozJ9fwPttqIuQs&ip=2401%3A4900%3A1f30%3A15b%3A1892%3Ac84a%3Ae398%3Aba12&id=o-ADxYKiqb6Omw2in8FwZvZZCZwFCpINHQcnVHb_BqXz5-&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C26&mn=sn-ci5gup-qxaed%2Csn-cvh76ney&ms=au%2Conr&mv=m&mvi=4&pl=52&gcr=in&initcwndbps=1752500&vprv=1&svpuc=1&mime=audio%2Fwebm&rqh=1&gir=yes&clen=3813544&dur=218.701&lmt=1714669829104505&mt=1727034299&fvip=1&keepalive=yes&c=IOS&txp=4502434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cgcr%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAJCy_PtuhgPPNeO8S3zyhm5sUInbRB2-kMkblkwTDzRBAiBkJwtmAT0R7zN09YI7sDZlai1NSuilQjhnEwZJOPvKmQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ABPmVW0wRQIhAJr84VfszUc2ZCfrGojID_v2bWWpgPX8g3y9bx6OcpVkAiAvLobOMiTTAqJewWsLLYsYh3FmZdMnDxjW-70Nmr4i9Q%3D%3D"
# # stream_audio(url)

# import time
# from pytubefix import Search
# from yt_dlp import YoutubeDL
# import urllib.parse
# import urllib.request
# import re
# import requests
# from bs4 import BeautifulSoup

# def search_1(query):
#     results = Search(query)
#     # for i in range(5):
#     url = results.videos[0].watch_url

# def search_2(query):
#     query_string = urllib.parse.urlencode({"search_query": query})
#     response = requests.get(f"https://www.youtube.com/results?{query_string}")
#     search_results = re.findall(r"watch\?v=(\S{11})", response.text)

#     search_results_links = []
#     temp = "https://www.youtube.com/watch?v="
#     for result in range(10):
#         temp += search_results[result]
#         print(temp)
#         # clip = f"https://www.youtube.com/watch?v={search_results[0]}" if search_results else None
#     # return clip
#     # inspect = BeautifulSoup(clip.content, "html.parser")
#     # yt_title = inspect.find_all("meta", property="og:title"

# # import timeit
# # # Timing search_1
# # start_time = time.time()
# # for i in range(10):
# #     search_1("Python programming")
# # time_search_1 = time.time() - start_time

# # # Timing search_2
# # start_time = time.time()
# # for i in range(10):
# #     search_2("Python programming")
# # time_search_2 = time.time() - start_time
# import timeit
# time_search_1 = timeit.timeit(lambda: search_1("Python programming"), number=20)
# time_search_2 = timeit.timeit(lambda: search_2("Python programming"), number=20)

# print("Time for search_1:", time_search_1)
# print("Time for search_2:", time_search_2)

#     # url = search_from_query(query)
#     # ys = results.videos[0].streams.get_audio_only()
#     # ys.download(mp3=True)


# # from pytubefix import Search

# # def ytdl_v(query):
# #     results = Search(query)
# #     # url = results.videos[0].watch_url
# #     # url = search_from_query(query)
# #     ys = results.videos[0].streams.get_audio_only()
# #     ys.download(mp3=True)
    
# #     # ydl_opts = {
# #     #     'format': 'bestaudio/best',
# #     #     'noplaylist': True,
# #     #     'quiet': True,
# #     #     'outtmpl': '%(title)s.%(ext)s',
# #     #     'postprocessors': [{
# #     #         'key': 'FFmpegExtractAudio',
# #     #         'preferredcodec': 'mp3',
# #     #         'preferredquality': '320',
# #     #     }],
# #     # }

# #     # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #     #     info = ydl.extract_info(url, download=True)
# #     #     audio_url = info['url']
# #     #     title = info['title']
# #     #     thumbnail_url = info.get('thumbnail')  # This fetches the thumbnail
# #     #     return audio_url, title, thumbnail_url
    

# # # import time
# # # start = time.time()
# # # ytdl_v("popular, the weeknd")
# # # endt = time.time()
# # # prin?t(endt
# # # 
# # # 
# # # -start)

# # import subprocess
# # from pydub import AudioSegment
# # from pydub.utils import mediainfo

# # # Example usage
# # audio_file = "C://Users//Aditya//Projects//OctaveMusic//The Weeknd - The Hills.mp3"
# # # sound = AudioSegment.from_file(
# # print(mediainfo(audio_file)['bit_rate'])
# # # -23.796528577804565 (ytd + pytubefix search) -> 320
# # # 4.868684768676758 (pytubefix only)
# # # 18.506396532058716 (yts + pytubefix search) -> 160
# # # 15.707344770431519(yts + pytubefix search) -> 32