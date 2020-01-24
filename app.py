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

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Set route
@app.route('/')
def index():
    return render_template("index.html")
# --- End of index route ----#

# Set route
@app.route('/parkmap')
def parkmap():
    return render_template("parkmap.html")
# --- End of index route ----#

# Set route
@app.route('/dashboard/<selmonth>')
def dashboard(selmonth):
    monthcol = "avg_" + selmonth

    # establish a connection
    connection = engine.connect()

    # Read title table into dataframe
    top10_select = "SELECT A.park_code, A." + monthcol + " as avgcount, N.park_name FROM public.visitor_average as A inner join park_coordinates as N on A.park_code = N.park_code order by A." + monthcol + " desc fetch first 10 rows only"
    top10_df = pd.read_sql(top10_select, connection)

    top10_list = top10_df.to_dict(orient='records')

    bot10_select = "SELECT A.park_code, A." + monthcol + " as avgcount, N.park_name FROM public.visitor_average as A inner join park_coordinates as N on A.park_code = N.park_code order by A." + monthcol + " asc fetch first 10 rows only"
    bot10_df = pd.read_sql(bot10_select, connection)

    bot10_list = bot10_df.to_dict(orient='records')
    # print(bot10_list)
    return render_template(\
        "visitors.html", \
        top10list = list(top10_list), \
        bot10list = list(bot10_list), \
        monthsel = selmonth.upper()  
        )
# --- End of index route ----#

# Set route
@app.route('/parkboard')
def parkboard():
    return render_template("parkboard.html")
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