"""
QueueObj (queue) -> isshuffle, next, prev, current
PlayerObj  (SongObj) -> Playback
CurrentSongObj (file_path) -> (is_liked, coverArt, title, artist, songLen, in_album )

"""

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

# from OctaveEngine.errors import *
# from OctaveEngine.audioClient import *

from OctaveEngine.errors import *
# from errors import *
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

from ffpyplayer.player import MediaPlayer

import yt_dlp
import json
from PIL import Image
import requests
from io import BytesIO

import pickle, os
from OctaveEngine import *