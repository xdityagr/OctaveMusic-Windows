# import vlc
import yt_dlp
import ctypes
import time
import threading
import signal
import sys
import os

from colorama import Fore, Back, Style


""" Setup VLC """
dirname = os.path.dirname(__file__)
#with that I made the relative path into an absolute path
vlc_path = os.path.join(dirname,'vlc_dlls')
#the plugins folder, libvlc.dll and libvlccore.dll is in the folder named vlc_folder which is in my project folder
os.environ['PATH'] += ';' + vlc_path

import vlc 


def get_fetch_ytInfo(youtube_url):
    """Fetch the direct stream URL from a YouTube link using yt-dlp."""
    ydl_opts = {'format': 'bestaudio/best', 'quiet': True, 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)

        return {'title':info['title'], 'channel': info.get('channel', 'Unkown') ,'stream_url': info['url']}

def signal_handler(sig, frame):
    """Handle Ctrl+C to exit gracefully."""
    print("\nExiting...")
    sys.exit(0)

def update_slider(player, stop_event):
    """Callback to print the current playback time every second."""
    while not stop_event.is_set():
        if player.is_playing():
            current_time = player.get_time() // 1000  # Get current time in seconds
            print(f"Current Playback Time: {current_time}s", end='\r', flush=True)

        time.sleep(1)

class VLCService:
    """A class to manage VLC playback with play, pause, and seek controls."""
    def __init__(self, debug=True, callback=None):
        # self.mediaObject = mediaObject
        # if self.mediaObject.isStreamable : 
        # self.media = vlc.Media(self.currentMediaObject['stream_url'])

        # self.media.add_options("network-caching=300")  # Faster playback
        self.player = vlc.MediaPlayer()
        self.currentMediaObject = None
        self.callback_thread = threading.Event()  # Event to control the slider thread
        self.debug = debug
        self.callback = callback
        print(f"CALLBACK is {self.callback}")
        

    def set_media(self, mediaObject):
        self.currentMediaObject = mediaObject
        if self.player.is_playing():
            self.player.stop()
            
        if self.currentMediaObject.isStreamable:
            self.media = vlc.Media(self.currentMediaObject.stream_url)
            self.media.add_options("network-caching=300")  # Faster playback
        else:
            self.media = vlc.Media(self.currentMediaObject.filePath)

        self.player.set_media(self.media)

        if self.debug: 
            print(Fore.BLUE + f"Media changed to {self.currentMediaObject.title}" + Fore.RESET)

        self.play()
        self.callback_thread.clear()  

        if self.callback is not None:
            threading.Thread(target=self.callback, args=(self.player, self.callback_thread), daemon=True).start()


    def play(self):
        """Start playback."""
        print('VLC PLAYBACK')
        if self.player.play() == -1:
            if self.debug:
                print(Fore.RED + "ERROR : Unable to play media." + Fore.RESET)
            return
        
        if self.debug:
            print(Fore.BLUE + f"Now Playing : " + Fore.RESET + f"{self.currentMediaObject.title} by {self.currentMediaObject.artist}")

    def wait_for_playback(self, timeout=10):
        """Wait for VLC to start playback within a timeout."""
        try:
            # start = time.time()
            for _ in range(timeout):
                if self.player.is_playing():
                    # end = time.time()
                    # print(f"Playback started, took {end - start:.2f} seconds.")
                    if self.callback is not None:
                        print('callback is present.')
                        self.callback_thread.clear()  # Clear the stop event
                        threading.Thread(target=self.callback, args=(self.player, self.callback_thread), daemon=True).start()
                    return True
                
                time.sleep(1)  # Wait before re-checking

            if self.debug:
                print(Fore.RED + "ERROR : Playback did not start in time." + Fore.RESET)
            
        except Exception as e:
            if self.debug:
                print(Fore.RED + f"ERROR : {e}" + Fore.RESET)
            
        return False

    def pause(self):
        """Pause playback."""
        self.player.pause()
        if self.debug:
            print(Fore.BLUE + f"Media Paused at {self.player.get_time() // 1000}s" + Fore.RESET)
        self.callback_thread.set()  # Stop the slider thread while paused

    def set_volume(self, volume=100):
        self.player.audio_set_volume(volume)
        if self.debug:
            print(Fore.BLUE + f"Volume set to {volume}%" + Fore.RESET)

    def get_volume(self):
        return self.player.audio_get_volume()
    
    def resume(self):
        """Resume playback."""
        self.player.play()
        if self.debug:
            print(Fore.BLUE + f"Media Resumed from {self.player.get_time() // 1000}s" + Fore.RESET)

        if self.callback is not None:
            self.callback_thread.clear()  # Allow the slider thread to run again
            threading.Thread(target=self.callback, args=(self.player, self.callback_thread), daemon=True).start()

    def seek(self, seconds):
        """Seek to a specific position (in seconds)."""
        self.player.set_time(seconds * 1000)  # VLC uses milliseconds
        if self.debug:
            print(Fore.BLUE + f"Media seeking to {seconds}s" + Fore.RESET)


    def stop(self):
        """Stop playback."""
        self.player.stop()
        if self.debug:
            print(Fore.BLUE + f"Media Stopped." + Fore.RESET)
        self.callback_thread.set()  # Stop the slider thread

    def set_callback(self, callback_function):
        self.callback = callback_function
        self.callback_thread.clear()  # Allow the slider thread to run again
        threading.Thread(target=self.callback, args=(self.player, self.callback_thread), daemon=True).start()

    # def on_media_end(event):
    #     print("Playlist finished!")

    #     event_manager = player.get_media_player().event_manager()
    #     event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, on_media_end)



def run_externally():
    """Main function to handle user input and manage VLC playback."""
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C

    print(Fore.BLUE + f"\nWelcome to OctaveEngine[vlc]\n" + Fore.LIGHTWHITE_EX + f"(Based on VLC Media Player [Version {vlc.__version__}], made for OctaveMusic.)\n" + Fore.RESET)
    print(Fore.BLUE + "Options: " + Fore.YELLOW + "(p)ause, (r)esume, (s)eek <seconds>, (q)uit or Ctrl+C to force exit.\n" + Fore.RESET)
        
    try:

        youtube_url = input("Enter the YouTube video URL > ")
        ytInfo = get_fetch_ytInfo(youtube_url)
        # Initialize VLC player
        vlc_player = VLCService(ytInfo)

        vlc_player.play()

        # Wait for playback to start
        if not vlc_player.wait_for_playback():
            return  # Exit if playback fails to start


        while True:
            
            user_input = input().strip()

            if user_input.lower() == 'p':
                vlc_player.pause()
            elif user_input.lower() == 'r':
                vlc_player.resume()
            elif user_input.lower().startswith('s'):
                try:
                    _, sec = user_input.split()
                    vlc_player.seek(int(sec))
                except ValueError:
                    print(Fore.RED + f"Invalid seek input. Usage: s <seconds>" + Fore.RESET)

            elif user_input.lower().startswith('c'):
                try:
                    _, url = user_input.split()
                    url = url.strip()
                    print(f"URLLL : {url}")
                    ytInfo = get_fetch_ytInfo(url)
                    vlc_player.set_media(ytInfo)

                except ValueError:
                    print(Fore.RED + f"Invalid seek input. Usage: s <seconds>" + Fore.RESET)

            elif user_input.lower().startswith('v'):
                try:
                    _, volume = user_input.split()
                    if volume:
                        volume = int(volume.strip())
                        vlc_player.set_volume(volume)
                    else:
                        print(f"Current Volume: {vlc_player.get_volume()}")
                except ValueError:
                    print(Fore.RED + f"Invalid seek input. Usage: s <seconds>" + Fore.RESET)

            elif user_input == 'q':
                vlc_player.stop()
                break
            
            else:
                print(Fore.YELLOW + f"Invalid seek input. Usage: s <seconds>" + Fore.RESET)
                
    except Exception as e:
        print(Fore.RED + f"ERROR: {e}" + Fore.RESET)
        

if __name__ == "__main__":
    run_externally()
