
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

    query = str(input('Enter a search query > ')).strip()
    limit =  str(input('Enter number of results [*Time dependent] > '))
    if not limit.isdigit(): limit = 10
    else: limit = int(limit)


    print(Fore.RED + f"Starting tests for query '{query}' ... "+ Fore.RESET)

    g1= time.time()
    r1 =OCF.grape_fetch(query, limit=limit)
    g2 = time.time()

    print(Fore.RED + f"> Test done for Grape fetch [✓]"+ Fore.RESET)

    o1 = time.time()
    r2 = asyncio.run(fetcher.grape_fetch(query, limit))
    o2 = time.time()

    # print(Fore.RED + f"> Test done for Internal fetch [✓]"+ Fore.RESET)
    print(Fore.YELLOW + f"RESULTS : "+ Fore.RESET)

    print(Fore.YELLOW + f"  • Grape Fetch V1 took {g2-g1}s to finish. "+ Fore.RESET)
    print(Fore.YELLOW + f"  • Grape Fetch V2 took {o2-o1}s to finish. "+ Fore.RESET)
    print(Fore.YELLOW + f"  • Check search_test_results.text for detailed results & result health."+ Fore.RESET)

    with open('search_test_details.txt', 'w', encoding="utf-8") as r:
        lines = ['GRAPE FETCHER v1: \n']
        n_lines = [f"{str(k['title'])} by '{str(k['artist'])} : {str(k['streamUrls'][0]['url'])}\n" for k in r1 ]
        lines.extend(n_lines)
        lines_2 = ['\GRAPE FETCHER v2: \n']
        n_lines_2 = [f"{str(j['title'])} by '{str(j['artist'])} : {str(j['streamUrls'][0]['url'])}\n" for j in r2 ]

        # n_lines_2  = [f"{str(j['title'])} by '{str(j['artist'])} : {str(j['id'])}\n" for j in r2 ]
        lines.extend(lines_2)
        lines.extend(n_lines_2)
        try :
            r.writelines(lines)
        except (UnicodeEncodeError, UnicodeDecodeError) as e:
            print(Fore.RED + f'Error : {e}' + Fore.RESET)
