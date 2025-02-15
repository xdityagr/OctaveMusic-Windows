
from OctaveEngine.grepFetch import OctaveFetch
import time, json
from colorama import Fore, Back

from grepFetch import GrapeFetcher

OCF = OctaveFetch(cachingEnabled=False, loggingEnabled=True)
OCF.grapeDeepSearchEnabled = True

import asyncio

fetcher = GrapeFetcher(deepSearchEnabled=True)
print(Back.WHITE + Fore.RED + 'Internal tests for GRAPEFETCHER[V1.0] & ASYNCGRAPEFETCHER[V2.0]' + Fore.RESET + Back.RESET + '\n')

running = True
while running:
    i = input('...')
    if i.lower() == 'q': break

    increment = 1
    song_queries = [
    "Blinding Lights",
    "Shape of You",
    "Bohemian Rhapsody",
    "Hotel California",
    "Rolling in the Deep",
    "Stairway to Heaven",
    "Smells Like Teen Spirit",
    "Someone Like You",
    "Sweet Child O' Mine",
    "Let It Be",
    "Thinking Out Loud",
    "Billie Jean",
    "Lose Yourself",
    "Wonderwall",
    "Chandelier",
    "Bad Guy",
    "Imagine",
    "Perfect",
    "Fix You",
    "Hey Jude",
    "Take Me Home, Country Roads",
    "Halo",
    "Closer",
    "All of Me",
    "Shallow",
    "Faded",
    "Despacito",
    "Uptown Funk",
    "Old Town Road",
    "Call Me Maybe",
    "Can't Stop the Feeling",
    "Stay",
    "Levitating",
    "Save Your Tears",
    "Sunflower",
    "Circles",
    "Senorita",
    "Believer",
    "Radioactive",
    "Demons",
    "Somebody That I Used to Know",
    "Happy",
    "Toxic",
    "No Tears Left to Cry",
    "Driver's License",
    "Good 4 U",
    "Positions",
    "Memories",
    "Counting Stars",
    "Wake Me Up"
]
    curr = 0
    print(Fore.RED + f"Starting tests ... "+ Fore.RESET)
    limit = 20

    for i, query in enumerate(song_queries):  
        
        g1= time.time()
        r1 =OCF.grape_fetch(query, limit=limit)
        g2 = time.time()

        print(Fore.RED + f"\r Pass {i+1}/{len(song_queries)}, current limit = {limit}"+ Fore.RESET, )

        o1 = time.time()
        r2 = asyncio.run(fetcher.grape_fetch(query, limit))
        o2 = time.time()

        pass_result = f"""PASS ({i+1}/{len(song_queries)}) : Query : {query}, Limit : {limit}, Time taken : {g2-g1:.2f}s (Grape Fetch V1), {o2-o1:.2f}s (Grape Fetch V2)"""
        with open('frequency_test_results.txt', 'a') as f:
            f.write(pass_result + '\n')

        with open('search_test_details.txt', 'a', encoding="utf-8") as r:

            lines = [f'\nPASS ({i+1}/{len(song_queries)})\nGRAPE FETCHER v1: \n']
            n_lines = [f"{str(k['title'])} by '{str(k['artist'])} : {str(k['streamUrls'][0]['url'])}\n" for k in r1 ]
            lines.extend(n_lines)
            lines_2 = ['\GRAPE FETCHER v2: \n']
            n_lines_2 = []
            for i, j in enumerate(r2):
                print(Fore.RED + f"Available Stream Urls : {len(j['streamUrls'])}"+ Fore.RESET)
                if len(j['streamUrls']) == 0:
                    ln = f"NO STREAM URLS FOR [{i}] {str(j['title'])} by '{str(j['artist'])}\n"
                    print(Fore.RED + f"NO STREAM URLS FOR [{i}] {str(j['title'])} by '{str(j['artist'])}"+ Fore.RESET)
                else:
                    ln = f"{str(j['title'])} by '{str(j['artist'])} : {str(j['streamUrls'][0]['url'])}\n"
                    
                n_lines_2.append(ln)    

            lines.extend(lines_2)
            lines.extend(n_lines_2)
            try :
                r.writelines(lines)
            except (UnicodeEncodeError, UnicodeDecodeError) as e:
                print(Fore.RED + f'Error : {e}' + Fore.RESET)
        
        limit += 1