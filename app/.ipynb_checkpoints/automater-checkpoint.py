import numpy as np
import pandas as pd
import requests
import os

from pymongo import MongoClient
from pprint import pprint

import config




# client_id = 'tn9oskedgjzumaz7seved6dl8z642j'
# client_secret = '5bbdqqsykhqu6t4fhroopms0hcvy6w'



# access_code = requests.post('https://id.twitch.tv/oauth2/token?client_id='+client_id+\
#                             '&client_secret='+client_secret+\
#                             '&grant_type=client_credentials')

# access_token = access_code.json()['access_token']


# headers = {
#     'Client-ID' : client_id,
#     'Authorization' : 'Bearer '+access_token
# }


top_streams_pull = requests.get('https://api.twitch.tv/helix/streams?first=100', headers=config.headers)



client = MongoClient()

db = client.twitch

streams_text = top_streams_pull.json()['data']

db.continuous_streams.insert_many(streams_text)




top_games_pull = (requests.get('https://api.twitch.tv/helix/games/top?first=100', headers=config.headers)).json()['data']

id_list = []
for games in top_games_pull:
    id_list.append(games['id'])
    
    
for games in id_list:
    games_text = (requests.get('https://api.twitch.tv/helix/streams?first=100&game_id='+games, headers=config.headers)).json()['data']
    db.continuous_games.insert_many(games_text)