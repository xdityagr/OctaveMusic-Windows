from pickletools import read_uint1
from pytubefix import YouTube, Search, exceptions
from pytubefix.exceptions import RegexMatchError, PytubeFixError
import json
import time

_default_clients = {
    'WEB': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'WEB',
                    'osName': 'Windows',
                    'osVersion': '10.0',
                    'clientVersion': '2.20240709.01.00',
                    'platform': 'DESKTOP'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '1',
            'X-Youtube-Client-Version': '2.20240709.01.00'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'WEB_EMBED': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'WEB_EMBEDDED_PLAYER',
                    'osName': 'Windows',
                    'osVersion': '10.0',
                    'clientVersion': '2.20240530.02.00',
                    'clientScreen': 'EMBED'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '56'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'WEB_MUSIC': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'WEB_REMIX',
                    'clientVersion': '1.20240403.01.00'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '67'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'WEB_CREATOR': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'WEB_CREATOR',
                    'clientVersion': '1.20220726.00.00'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '62'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'WEB_SAFARI': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'WEB',
                    'clientVersion': '2.20240726.00.00',
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15,gzip(gfe)',
            'X-Youtube-Client-Name': '1'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'MWEB': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'MWEB',
                    'clientVersion': '2.20240726.01.00'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'X-Youtube-Client-Name': '2'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'ANDROID': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID',
                    'clientVersion': '19.29.37',
                    'platform': 'MOBILE',
                    'osName': 'Android',
                    'osVersion': '14',
                    'androidSdkVersion': '34'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.youtube/',
            'X-Youtube-Client-Name': '3'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    # Deprecated
    #   'ANDROID_EMBED': {
    #     'innertube_context': {
    #         'context': {
    #             'client': {
    #                 'clientName': 'ANDROID_EMBEDDED_PLAYER',
    #                 'clientVersion': '19.13.36',
    #                 'clientScreen': 'EMBED',
    #                 'androidSdkVersion': '30'
    #             }
    #         }
    #     },
    #     'header': {
    #         'User-Agent': 'com.google.android.youtube/',
    #         'X-Youtube-Client-Name': '55',
    #         'X-Youtube-Client-Version': '19.13.36'
    #     },
    #     'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    #     'require_js_player': False
    # },

    'ANDROID_VR': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID_VR',
                    'clientVersion': '1.57.29',
                    'deviceMake': 'Oculus',
                    'deviceModel': 'Quest 3',
                    'osName': 'Android',
                    'osVersion': '12L',
                    'androidSdkVersion': '32'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.vr.oculus/1.57.29 (Linux; U; Android 12L; eureka-user Build/SQ3A.220605.009.A1) gzip',
            'X-Youtube-Client-Name': '28'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'ANDROID_MUSIC': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID_MUSIC',
                    'clientVersion': '7.11.50',
                    'androidSdkVersion': '30',
                    'osName': 'Android',
                    'osVersion': '11'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.music/7.11.50 (Linux; U; Android 11) gzip',
            'X-Youtube-Client-Name': '21'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'ANDROID_CREATOR': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID_CREATOR',
                    'clientVersion': '24.30.100',
                    'androidSdkVersion': '30',
                    'osName': 'Android',
                    'osVersion': '11'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.creator/24.30.100 (Linux; U; Android 11) gzip',
            'X-Youtube-Client-Name': '14'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'ANDROID_TESTSUITE': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID_TESTSUITE',
                    'clientVersion': '1.9',
                    'platform': 'MOBILE',
                    'osName': 'Android',
                    'osVersion': '14',
                    'androidSdkVersion': '34'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.youtube/',
            'X-Youtube-Client-Name': '30',
            'X-Youtube-Client-Version': '1.9'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'ANDROID_PRODUCER': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'ANDROID_PRODUCER',
                    'clientVersion': '0.111.1',
                    'androidSdkVersion': '30',
                    'osName': 'Android',
                    'osVersion': '11'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.producer/0.111.1 (Linux; U; Android 11) gzip',
            'X-Youtube-Client-Name': '91'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'IOS': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'IOS',
                    'clientVersion': '19.29.1',
                    'deviceMake': 'Apple',
                    'platform': 'MOBILE',
                    'osName': 'iPhone',
                    'osVersion': '17.5.1.21F90',
                    'deviceModel': 'iPhone16,2'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.youtube/19.29.1 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
            'X-Youtube-Client-Name': '5'
        },
        'api_key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        'require_js_player': False
    },

    # Deprecated
    # 'IOS_EMBED': {
    #     'innertube_context': {
    #         'context': {
    #             'client': {
    #                 'clientName': 'IOS_MESSAGES_EXTENSION',
    #                 'clientVersion': '19.16.3',
    #                 'deviceMake': 'Apple',
    #                 'platform': 'MOBILE',
    #                 'osName': 'iOS',
    #                 'osVersion': '17.4.1.21E237',
    #                 'deviceModel': 'iPhone15,5'
    #             }
    #         }
    #     },
    #     'header': {
    #         'User-Agent': 'com.google.ios.youtube/',
    #         'X-Youtube-Client-Name': '66'
    #     },
    #     'api_key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    #     'require_js_player': False
    # },

    'IOS_MUSIC': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'IOS_MUSIC',
                    'clientVersion': '7.08.2',
                    'deviceMake': 'Apple',
                    'platform': 'MOBILE',
                    'osName': 'iPhone',
                    'osVersion': '17.5.1.21F90',
                    'deviceModel': 'iPhone16,2'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.youtubemusic/7.08.2 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
            'X-Youtube-Client-Name': '26'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'IOS_CREATOR': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'IOS_CREATOR',
                    'clientVersion': '24.30.100',
                    'deviceMake': 'Apple',
                    'deviceModel': 'iPhone16,2',
                    'osName': 'iPhone',
                    'osVersion': '17.5.1.21F90'
                }
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.ytcreator/24.30.100 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
            'X-Youtube-Client-Name': '15'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    },

    'TV_EMBED': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'TVHTML5_SIMPLY_EMBEDDED_PLAYER',
                    'clientVersion': '2.0',
                    'clientScreen': 'EMBED',
                    'platform': 'TV'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '85'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': True
    },

    'MEDIA_CONNECT': {
        'innertube_context': {
            'context': {
                'client': {
                    'clientName': 'MEDIA_CONNECT_FRONTEND',
                    'clientVersion': '0.1'
                }
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0',
            'X-Youtube-Client-Name': '95'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'require_js_player': False
    }
}


def debug_and_fix_clients():
    video_url ="https://music.youtube.com/watch?v=yo01OWS4NlA"
    clients = {'Best':'', 'Working':{}, 'Not Working': {}}
    working = clients['Working']
    not_working = clients['Not Working']
    
    for client in _default_clients.keys():
        print(f"Running for {client} ... ")
        try:
            start = time.time()

            yt = YouTube(video_url, client=client)
        
            audio_stream = yt.streams.filter(only_audio=True).order_by('bitrate').last()
            audio_url = audio_stream.url if audio_stream else None


            if audio_stream != None and audio_url != None:
                end = time.time()
                total_time_taken = round(end-start, 5)

                working[client] = total_time_taken

            else:
                not_working[client] = 'NOT Working, either audio_stream or audio_url is NONE.'

        except exceptions.VideoUnavailable:
            not_working[client] = f'NOT Working, Returns -> Video {video_url} is unavailable.'

        except AttributeError as e:
            not_working[client] = f'NOT Working, Returns -> AttributeError : INFO {e}'
        
        except RegexMatchError  as e:
            not_working[client] = f'NOT Working, Returns -> RegexMatchError : INFO {e}.'
        
        except PytubeFixError as e:
            not_working[client] = f'NOT Working, Returns -> PytubeFixError : INFO {e}.'
        
        except Exception  as e:
            not_working[client] = f'NOT Working, Returns -> Error : INFO {e}.'

        print(f"Done for {client}. ")
    
    best = (None, 100)
    for i in working.items():
        if i[1] <= best[1]:
            best = (i[0], i[1])
        
    clients['Best'] = best 
    clients['Working'] = sorted(working)
    
    print(f"All done. check file.")
    with open('working_clients.json', 'w') as f: pass
    with open('working_clients.json', 'w') as fp: json.dump(clients, fp, indent=4)

    return best, working, not_working

WORKING_CLIENTS = None
BEST_CLIENT = None

class ClientNotWorkingError(Exception):
    """Exception raised when a client is not functioning properly."""
    def __init__(self, title='Client Not Working Error', details="The client is not working as expected, Please run 'Debug & Fix' from settings. Check Details in Logs."):
        self.title = title
        self.details = details
        super().__init__(f"{self.title}: {self.details}")


with open('working_clients.json', 'r') as read: 
    clients_info = json.load(read)

    WORKING_CLIENTS = clients_info['Working']
    BEST_CLIENT = clients_info['Best']


    
def fetch_stream_url(video_url):
    try:

        yt = YouTube(video_url, client=str(BEST_CLIENT[0]))

        title = yt.title
        author = yt.author
        audio_stream = yt.streams.filter(only_audio=True).order_by('bitrate').last()
        audio_url = audio_stream.url if audio_stream else None

        return audio_url
    
    except exceptions.VideoUnavailable:
        print(f"Video {video_url} is unavailable.")
        return ClientNotWorkingError
    
    except exceptions.PytubeFixError as e:
        print(f"An error occurred: {e}")
        return ClientNotWorkingError
    
    except exceptions.VideoUnavailable:
        print(f'NOT Working, Returns -> Video {video_url} is unavailable.')

    except AttributeError as e:
        print(f'NOT Working, Returns -> AttributeError : INFO {e}')
        raise ClientNotWorkingError
    
    except RegexMatchError  as e:
        print(f'NOT Working, Returns -> RegexMatchError : INFO {e}.')
        raise ClientNotWorkingError
    
    except PytubeFixError as e:
        print(f'NOT Working, Returns -> PytubeFixError : INFO {e}.')
        raise ClientNotWorkingError
    except Exception  as e:
        print(f'NOT Working, Returns -> Error : INFO {e}.')
        raise ClientNotWorkingError

def fetch_video_data(video_url):
    """Fetch video details from a given YouTube video URL."""
    try:
        print("TYPE -> ", type(video_url))
        yt = YouTube(video_url, client='ANDROID_VR')
        title = yt.title
        author = yt.author
        audio_stream = yt.streams.filter(only_audio=True).order_by('bitrate').last()
        audio_url = audio_stream.url if audio_stream else None

        video_info = {
            'title': title,
            'author': author,
            'stream_url': audio_url,
            'thumbnail_url': yt.thumbnail_url,
            'duration':yt.length,
            'release_date':yt.publish_date
        }

        return video_info
    
    except exceptions.VideoUnavailable:
        print(f"Video {video_url} is unavailable.")
        raise ClientNotWorkingError
    except exceptions.PytubeFixError as e:
        print(f"An error occurred: {e}")
        raise ClientNotWorkingError
    
    except exceptions.VideoUnavailable:
        print(f'NOT Working, Returns -> Video {video_url} is unavailable.')
        raise ClientNotWorkingError
    
    except AttributeError as e:
        print(f'NOT Working, Returns -> AttributeError : INFO {e}')
        raise ClientNotWorkingError
    
    except RegexMatchError  as e:
        print(f'NOT Working, Returns -> RegexMatchError : INFO {e}.')
        raise ClientNotWorkingError
    
    except PytubeFixError as e:
        print(f'NOT Working, Returns -> PytubeFixError : INFO {e}.')
        raise ClientNotWorkingError
    
    except Exception  as e:
        print(f'NOT Working, Returns -> Error : INFO {e}.')
        raise ClientNotWorkingError

def youtube_search(query, fetch=5):
    """Search YouTube and return the list of video URLs."""
    try:
        response = Search(query)
        video_urls = [response.videos[i].watch_url for i in range(fetch)]
        return video_urls
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return []

def fetch_videos_from_search(query, fetch=5):
    """Search YouTube and fetch video details for the results."""
    video_urls = youtube_search(query, fetch)
    video_data = []
    for video_url in video_urls:
        try :
            video_info = fetch_video_data(video_url)
            if video_info:
                video_data.append(video_info)
        except ClientNotWorkingError as e:
            return -1, ClientNotWorkingError
        
 
    
    return video_data

# Example usage:
if __name__ == "__main__":
    # debug_and_fix_clients()
    query = str(input("Enter a video to search : "))
    st = time.time()
    results = fetch_videos_from_search(query, fetch=5)
    end = time.time()
    total_time = end-st
    
    """
    Attempt - 1 (6 results):  
        #25.270720958709717 -> pytubefix
        #23.81370520591736 -> ytdl
    
    Attempt - 2 (10 results):
        #41.72901630401611 -> pytubefix
        #35.51675200462341 -> ytdl

    ------- with async 

    Attempt - 3 (5 results):
    #13.488770008087158 -> pytubefix
    #5.729563236236572 -> ytdl
    
    Attempt - 4 (10 results):
    #30.548617362976074 -> pytubefix
    #11.497152090072632 -> ytdl
    
    """
    

    # q = "https://music.youtube.com/watch?v=yo01OWS4NlA&list=RDAMVMuY-syOaUziU"
    # print(fetch_video_data(q))

    print(f"RESULTS ({total_time}) : \n" )
    if results[0] != -1:
        for result in results:
            print("Title:", result['title'])
            print("Author:", result['author'])

            print("Stream URL:", result['stream_url'], end='\n')

            print("Thumbnail URL:", result['thumbnail_url'])
            print("-------------------")
    else: print("None")

"https://lh3.googleusercontent.com/ROOT6ox5RPjMqCLSbw1VtK8xYfr2mBKZaG6o7_HSMvGTIAJsUDkYYcI-RRXoyC7XdUeqh4QgqyAvUmOmKQ=w60-h60-l90-rj"

# def get_custom_thumbnail(base_url, width, height):
#     """Return a YouTube Music thumbnail with custom dimensions."""
#     return f"{base_url}=w{width}-h{height}-rj"

# # Example usage
# thumbnail_url = get_custom_thumbnail(
#     "https://lh3.googleusercontent.com/ROOT6ox5RPjMqCLSbw1VtK8xYfr2mBKZaG6o7_HSMvGTIAJsUDkYYcI-RRXoyC7XdUeqh4QgqyAvUmOmKQ",
#     200, 200
# )
# print(thumbnail_url)

