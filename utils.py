import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
from plotly import tools
from plotly.subplots import make_subplots
import requests

import pandas as pd
import numpy as np
import requests

from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.twitch


def game_info(game):
    df = pd.DataFrame(list(db.continuous_games.find({'game_name':game})))
    total_viewers = df.viewer_count.sum()
    total_streamers = df.user_login.nunique()
    average_viewers = round(total_viewers/12)
    average_streamers = round(total_streamers/12)
    st.sidebar.write('The total number of viewers is:' , total_viewers)
    st.sidebar.write('The total number of streamers is:', total_streamers)
    st.sidebar.write('The average number of viewers is: ', average_viewers)
    st.sidebar.write('The average number of streamers is: ', average_streamers)
    #return viewers, streamers


def viewer_record(game):
    largedf = pd.DataFrame(list(db.continuous_games.find({})))
    largedf.started_at = pd.to_datetime(largedf.started_at)
    largedf['hour'] = largedf.started_at.dt.hour
    temp = largedf[largedf.game_name == game]
    new = temp.groupby(['hour'])[['viewer_count']].sum().reset_index()
    #print(temp.head())
    line_fig = go.Figure(
        data=go.Scatter(
            x=new.hour,
            y=new.viewer_count,
            #title = 'Viewer History'
        )
    )
    return st.plotly_chart(line_fig)