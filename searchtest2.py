from OctaveEngine import octaveFetch
import json

search = octaveFetch.OctaveFetch()
search.generate_client_file(force_new=True)