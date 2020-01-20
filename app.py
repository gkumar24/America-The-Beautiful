from flask import Flask, render_template, redirect, url_for
from datetime import date
import pandas as pd

#Importing SqlAlchemy to use import DataFrame into Postgress.
import sqlalchemy
from config import password, username
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Exporting tranformed file to Postgres. Appending since table heads already exist in Postgres
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/NationalParkDB')

# Create an instance of our Flask app.
app = Flask(__name__)

# Set route
@app.route('/')
def index():
    return render_template("index.html")
# --- End of index route ----#

# Set route
@app.route('/timeline')
def timeline():
    
    # establish a connection
    connection = engine.connect()

    # Read title table into dataframe
    timeline_select = "SELECT park_name as name, cast(year_established as INTEGER) as year_established FROM timeline ORDER BY cast(year_established as INTEGER)"
    timeline_df = pd.read_sql(timeline_select, connection)

    # get national park list witht he timeline
    timeline_list = timeline_df.to_dict(orient='records')
    
    #get the first year the national park established 
    firstpark_data = timeline_list[0]
        
    #define the start and end of the decade
    decade_start = int(int(firstpark_data["year_established"])/10)*10
    decade_stop = 10 + int((date.today().year)/10)*10

    #create marker list for the timeline graph
    marker_list = []
    yearActive = decade_start #this set the active year to the 1st decade
    for yearpoint in range(decade_start, decade_stop,10):
        if yearpoint == yearActive:
            activeClass = "active"
        else:
            activeClass = ""

        marker_list.append({"year" : yearpoint, "class" : activeClass})        

    return render_template(\
        "timeline.html", \
        timelineList = list(timeline_list), \
        decadeStart = decade_start, \
        decadeStop = decade_stop, \
        markerList = marker_list
        )
# --- End of timeline route ----#

if __name__ == "__main__":
    app.run(debug=True)