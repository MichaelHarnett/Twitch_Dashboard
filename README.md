# Twitch_Dashboard
<hr>
A Data Engineering focused project from Metis


# Notebook Descripitons 
<hr>
<b>twitch_prelim</b> This notebook was used to learn the intricacies of the Twitch Developers API, finding the right way to retrieve the data needed
<br>
<b>mongo_prelim</b> Used to learn how to connect the information pulled from the API into a database
<br>
<b>plotly_prelim</b> Used to create different graphs and visualizations, and test different aggregations
<br>
<b>automater.py</b> Python script used in conjunction with crontab to automate pulling of information every hour, and storing the pull into my database
<br>
<b>app.py</b> Streamlit app code used to connect everything in a web-based dashboard
<b>utils.py</b>Different functions I created to be called in app.py


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
