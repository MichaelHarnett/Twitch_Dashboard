import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots
import requests

from pymongo import MongoClient
from pprint import pprint

from utils import game_info, viewer_record

import streamlit as st


##twitch permissions

client_id = 'tn9oskedgjzumaz7seved6dl8z642j'
client_secret = '5bbdqqsykhqu6t4fhroopms0hcvy6w'

access_code = requests.post('https://id.twitch.tv/oauth2/token?client_id='+client_id+\
                            '&client_secret='+client_secret+\
                            '&grant_type=client_credentials')

access_token = access_code.json()['access_token']


headers = {
    'Client-ID' : client_id,
    'Authorization' : 'Bearer '+access_token
}


#df = pd.read_csv('streams.csv')

df = pd.DataFrame((requests.get('https://api.twitch.tv/helix/streams?first=100', headers=headers)).json()['data'])



st.title("Twitch Information Platform")
st.write('Current Top Streams')

viewer_count = df.groupby(['game_name'])[['viewer_count']].sum().reset_index()
streamer_count = df.groupby(['game_name'])[['user_login']].nunique().sort_values(['user_login']).reset_index()

#st.sidebar.info('More specific game information:')
st.sidebar.title('Specific Game Info:')
game = st.sidebar.selectbox(label = 'Choose a game', options = viewer_count.game_name)

st.sidebar.write(game_info(game))

## switched to updating infro from mongodb 


# # pie chart of the top streams, grouped by game, values as number of viewers
# fig1 = px.pie(
#     viewer_count,
#     values = viewer_count['viewer_count'],
#     names = viewer_count['game_name'],
#     title = 'games by viewer count',
#     height = 800,
#     width = 800,
#     hover_name = viewer_count['game_name']
# )

# #horizontal bar chart of the same games, but the number of streamers
# fig2 = px.bar(
#     streamer_count,
#     x = streamer_count.user_login,
#     y = streamer_count.game_name,
#     orientation = 'h',
#     height = 800,
#     width = 800
# )

# st.plotly_chart(fig1)
# st.plotly_chart(fig2)

# option = st.selectbox(label = 'Choose a game', options = viewer_count.game_name)


sub_fig = make_subplots(rows = 1, cols = 2, vertical_spacing = .9, specs=[[{'type':'pie'}, {'type':'bar'}]])
sub_fig.add_trace(go.Pie(
    values = viewer_count['viewer_count'],
    labels = viewer_count['game_name'],
    title = 'games by viewer count',
    textinfo = None,
    showlegend = False,
    #height = 800,
    #width = 800,
    #hover_name = viewer_count['game_name']
    ),row=1, col=1)
sub_fig.add_trace(go.Bar(
    x = streamer_count.user_login,
    y = streamer_count.game_name,
    orientation = 'h',
)
)
layout = go.Layout()
sub_fig.update_layout(height=1000, width = 1200, title = 'Current Top Streams')

sub_fig.update_traces(textposition='inside')
sub_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')#, title = ‘Total Payments by Nature of Payments in 2020’, title_x=0.5)
st.plotly_chart(sub_fig, use_containter_width = False)
viewer_record(game)
