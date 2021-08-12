import numpy as np
import pandas as pd
import requests
import os

from pymongo import MongoClient
from pprint import pprint

import config





top_streams_pull = requests.get('https://api.twitch.tv/helix/streams?first=100', headers=config.headers)



client = MongoClient(config.server)

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