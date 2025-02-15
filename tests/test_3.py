"""
    IMPLEMENT THIS.
"""

import multiprocessing as mp
import time
from ffpyplayer.player import MediaPlayer
from OctaveEngine.MediaControls import OctaveFetch
import asyncio

# Initialize OctaveFetch instance
ocf = OctaveFetch()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Fetch audio streams asynchronously
results = []
try:
    result1 = loop.run_until_complete(ocf.fetchQuery("the weeknd, starboy kygo remix", results=1))
    result2 = loop.run_until_complete(ocf.fetchQuery("the weeknd, often kygo remix", results=1))
finally:
    loop.close()

results.extend(result1)
results.extend(result2)
import threading

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
        self.is_playing = False
        self.playback_start_time = 0  # Track the start time for playback
        self.total_elapsed_time = 0  # Total elapsed time during playback

    def _player_worker(self, stream_url, control_queue, volume, update_callback):
        """Worker function running the MediaPlayer in a separate process."""
        print(f"Starting player with stream: {stream_url}")
        try:
            player = MediaPlayer(stream_url, ff_opts={'sync': 'audio', 'buffer_size': 2048}, timeout=30)
            player.set_volume(volume)

            self.playback_start_time = time.time()  # Start tracking time
            self.is_playing = True

            update_interval = 0.1

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
                        self.is_playing = False  # Update playback state
                    elif command == "RESUME":
                        print("Resuming player...")
                        player.set_pause(False)
                        self.is_playing = True  # Update playback state
                        self.playback_start_time = time.time()  # Reset start time
                    elif isinstance(command, tuple):
                        if command[0] == "VOLUME":
                            new_volume = command[1]
                            print(f"Setting volume to {new_volume}")
                            player.set_volume(new_volume)
                        elif command[0] == "SEEK":
                            seek_position = command[1]
                            print(f"Seeking to {seek_position} seconds...")
                            player.seek(seek_position)
                            self.playback_start_time = time.time()  # Reset start time after seeking

                if self.is_playing:
                    pts = player.get_pts()  # Get current playback position in seconds
                    if pts is not None:
                        current_position_ms = int(pts * 1000)  # Convert to milliseconds
                        update_callback(current_position_ms)

                time.sleep(1)  # Prevent busy-wait

            self.is_playing = False  # Mark as not playing when done

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

# Example usage
def update_slider(position):
    """Callback function to update the slider with the current position."""
    print(f"Current position: {position//1000} ms")


# Example usage
if __name__ == "__main__":
    player = MASS()

    # Load and play the first stream
    player.load_stream(results[0].stream_url, volume=0.5, update_callback=update_slider)
    time.sleep(20)
    player.stop()
    player.load_stream(results[1].stream_url, volume=0.5, update_callback=update_slider)
    time.sleep(20)
    player.stop()