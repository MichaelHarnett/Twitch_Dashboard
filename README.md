# Twitch Dashboard
<hr>
A Data Engineering focused project from Metis
<br><br>

This project was geared towards engineering an end to end daata pipeline. In keeping with the theme of most of my other projects, I chose to center this pipeline around video games. I decided to create a live updating dashboard based on information from Twitch. For those that don't know, Twich is one of the largest video game streaming sites. The idea was to create a dashboard for aspiring new streamers, that would show what the current top games are, the number of viewers watching theses games, and the number of streamers actively streaming the game. I accomplished this by pulling information from Twitch's Developer API and storing the information in a Mongo Atlas data base. I set up a recurring .py script using crontab that pulls the information once every hour, that allows for historical tracking. By storing the pulls in a database, I was able to also display more specific information for a specific game. Such as viewer counts from the last 24 hours, as well as average streamer and viewer count.
<br><br>
I displayed the results on a Streamlit Sharing app that is publicly available [here](https://share.streamlit.io/michaelharnett/twitch_dashboard/main/app/app.py)
<br>
This project was created as a 2 week project while at Metis. The app is functioning, but could use improvements, mostly with styling. Aditionally, the first iteration of this project lived natively on a regular Mongo data base on my computer. Moving the app to streamlit sharing caused me to re-build the database remotely with Mongo Atlas. Since this project was already completed, and will be used mainly for demonstrative purposes, the recurring script has been stopped, and the database is no longer growing. 
<br><br>


# Notebook Descripitons 
<hr>
<b>Prelim Code Folder:</b> This notebook holds all the notebooks I used to first poke around with the twitch API, MongoDB, and Plotly
<ul>
  <li><b>twitch_prelim</b> This notebook was used to learn the intricacies of the Twitch Developers API, finding the right way to retrieve the data needed</li>
  <li><b>mongo_prelim</b> Used to learn how to connect the information pulled from the API into a database</li>
  <li><b>plotly_prelim</b> Used to create different graphs and visualizations, and test different aggregations</li>
</ul>
<br><br>
<b>App Folder:</b> This folder contains all the code for the Streamlit Sharing app.
<ul>
  <li><b>app.py</b> - Streamlit app code used to connect everything in a web-based dashboard</li>
  <li><b>automater.py</b> - Python script used in conjunction with crontab to automate pulling of information every hour, and storing the pull into my database</li>
  <li><b>utils.py</b> - Different functions I created to be called in app.py</li>
</ul>
  

<br><br><br>




<hr>


# Data
<hr>
Data for this project was pulled from Twitch's Developer API. As opposed to other APIs I have worked with in the past, Twitch required registration, and OAuth for every data pull. After the data is retrieved from the API, it is stored into a Mongo DataBase for use. Some of the data and visualizations on my streamlit app are only possible becuse of the continuous storage of data. History of viewing/streaming information is not available through the API.


# Tools
<hr>
Python's requests library was used to connect to Twitch's API
Crontab was used to automate the request process every hour
MongoDB was used to store data
Plotly was used to visualize data
Streamlit was used to deploy visualizations



# Results and Future Work
<hr>
Learning how to engineer a data pipeline was challenging, but overall a success. I was able to automate a script that pulls information from my source every hour. The notebooks that visualize the data do not pull from the API, rather, they query and aggregate from the created database. This allows the results to change based on when the information is being viewed.
<br>
In the future, I would like to move this onto a cloud platform. The amount of data being collected will quickly be too much for my local machine, especially being a school project. 
<br>
I would also like to polish the look and feel of the app. While it is functional, it could be syled better. 
