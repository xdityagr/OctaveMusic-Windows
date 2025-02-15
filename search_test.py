
from OctaveEngine.octaveFetch import OctaveFetch
import time, json
from colorama import Fore, Back

OCF = OctaveFetch(cachingEnabled=False, loggingEnabled=True)
OCF.grapeDeepSearchEnabled = True

print(Back.WHITE + Fore.RED + 'Internal tests for GRAPEFETCHER & Internal Fetcher' + Fore.RESET + Back.RESET + '\n')

running = True
while running:
    i = input('...')
    if i.lower() == 'q': break

    query = str(input('Enter a search query > ')).strip()
    results =  str(input('Enter number of results [*Time dependent] > '))
    if not results.isdigit(): results = 10
    else: results = int(results)

    print(Fore.RED + f"Starting tests for query '{query}' ... "+ Fore.RESET)

    g1= time.time()
    r1 =OCF.grape_fetch(query)
    g2 = time.time()

    print(Fore.RED + f"> Test done for Grape fetch [✓]"+ Fore.RESET)

    o1 = time.time()
    r2 = OCF.fetch(query, limit=results, auto_next=True)
    o2 = time.time()

    print(Fore.RED + f"> Test done for Internal fetch [✓]"+ Fore.RESET)
    print(Fore.YELLOW + f"RESULTS : "+ Fore.RESET)

    print(Fore.YELLOW + f"  • Grape Fetch took {g2-g1}s to finish. "+ Fore.RESET)
    print(Fore.YELLOW + f"  • Internal Fetch took {o2-o1}s to finish. "+ Fore.RESET)
    print(Fore.YELLOW + f"  • Check search_test_results.text for detailed results & result health."+ Fore.RESET)

    with open('search_test_details.txt', 'w', encoding="utf-8") as r:
        lines = ['GRAPE FETCHER : \n']
        n_lines = [f"{str(k['title'])} by '{str(k['artist'])} : {str(k['streamUrls'][0]['url'])}\n" for k in r1 ]
        lines.extend(n_lines)
        lines_2 = ['\nOCTAVE FETCHER : \n']
        n_lines_2  = [f"{str(j['title'])} by '{str(j['artist'])} : {str(j['id'])}\n" for j in r2 ]
        lines.extend(lines_2)
        lines.extend(n_lines_2)
        try :
            r.writelines(lines)
        except (UnicodeEncodeError, UnicodeDecodeError) as e:
            print(Fore.RED + f'Error : {e}' + Fore.RESET)
