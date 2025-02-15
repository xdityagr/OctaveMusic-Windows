# import requests

# import re
# import json

# video_url = "https://www.youtube.com/watch?v=JPIhUaONiLU"
# response = requests.get(video_url)

# # Extract the player response JSON
# pattern = r'"streamingData":(\{.*?\})'
# match = re.search(pattern, response.text)
# if match:
#     streaming_data = json.loads(match.group(1))
#     for format in streaming_data.get("formats", []):
#         print(f"Format: {format['qualityLabel']}, URL: {format['url']}")

from _innertube import InnerTube


def print_results(search_data) -> str:
    """Print search results, then return the continuation token"""

    if "contents" in search_data:
        # This is the first batch of results
        item_section, continuation_item = search_data["contents"][
            "twoColumnSearchResultsRenderer"
        ]["primaryContents"]["sectionListRenderer"]["contents"]
    elif "onResponseReceivedCommands" in search_data:
        # This is a continuation
        item_section, continuation_item = search_data["onResponseReceivedCommands"][0][
            "appendContinuationItemsAction"
        ]["continuationItems"]
    else:
        raise Exception("Failed to parse search data")

    results = item_section["itemSectionRenderer"]["contents"]
    length = len(results)
    for result in results:
        result_type = next(iter(result))
        result_data = result[result_type]

        if result_type == "channelRenderer":
            print("Channel -", result_data["title"]["simpleText"])
        elif result_type == "playlistRenderer":
            print("Playlist -", result_data["title"]["simpleText"])
        elif result_type == "radioRenderer":
            print("Radio -", result_data["title"]["simpleText"])
        elif result_type == "reelShelfRenderer":
            print("Reel Shelf -", result_data["title"]["simpleText"])
        elif result_type == "shelfRenderer":
            print("Shelf -", result_data["title"]["simpleText"])
        elif result_type == "videoRenderer":
            print("Video -", result_data["title"]["runs"][0]["text"])
        else:
            print(f"{result_type} - ???")

    continuation_token = continuation_item["continuationItemRenderer"][
        "continuationEndpoint"
    ]["continuationCommand"]["token"]

    return continuation_token, length


import time
client = InnerTube("WEB", "2.20240812.00.00")

while True : 
    i = input('...')
    if i.lower() == 'q': break
    query = input('Enter a search query > ')
    length =input('Enter number of results [*Time dependent] > ')
    start = time.time()

    if length.isdigit(): length = int(length)
    else: length = 10
    
    net_results = []

    results1 = client.search(query)
    continuation_token, l1 = print_results(results1)
    if l1 >= length:
        print(f"Found {l1} results, stopping search")
        continue
    else:
        result_len = l1
        cont_tkn = continuation_token

        while result_len < length:
            print('Continuing search...')
            data_more = client.search(continuation=cont_tkn)
            cont_tkn, n_len = print_results(data_more)
            result_len += n_len
            if n_len == 0:
                print("No more results")
                break
        
    end = time.time()   
    print(f'Total {result_len} results fetched, Time taken = {end-start:.2f}s')

    # continuation_token, length1 = print_results(data)

    

# data = client.search("arctic monkeys")
# print('Continuing search...')

# # "Continue" the search results using the continuation token
# data2 = client.search(continuation=continuation_token)
# continuation_token2, length2 = print_results(data2)

# print()
