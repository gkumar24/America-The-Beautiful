from flask import Flask, render_template, redirect, url_for
from datetime import date
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

def Connect_MongoDB():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    return client
# ---- End of Connect_MongoDB ----#

def Close_Connection_MongoDB(client):
    client.close()
    return True
# ---- End of Close_Connection_MongoDB ----#


# Set route
@app.route('/')
def index():
    return render_template("index.html")
# --- End of index route ----#

# Set route
@app.route('/timeline')
def timeline():
    # Variable to hold status of mars_db and mars_collection
    dbExist = False
    colExist = False

    # Get client for Mongo DB
    myClient = Connect_MongoDB()

    #Check if natpark_db exist, and if db exist, check for timeline_col
    dbList = myClient.list_database_names()
    if "natpark_db" in dbList:
        dbExist = True
        natParkDB = myClient.natpark_db
        #Get list of collection, and check for timeline collection
        colList = natParkDB.list_collection_names()
        if "timeline_col" in colList:
            colExist = True
            timelineCol = natParkDB.timeline_col
    
    start_decade = 1

    if colExist == True:
        # get national park list witht he timeline
        timeline_list = list(timelineCol.find().sort([("Year_Established",1)]))

        #get the first year the national park established 
        firstpark_data = list(timelineCol.find().sort([("Year_Established",1)]).limit(1))
        
        #define the start and end of the decade
        decade_start = int(int(firstpark_data[0]["Year_Established"])/10)*10
        decade_stop = 10 + int((date.today().year)/10)*10

        print(decade_stop)

        #create marker list for the timeline graph
        marker_list = []
        yearActive = decade_start #this set the active year to the 1st decade
        for yearpoint in range(decade_start, decade_stop,10):
            if yearpoint == yearActive:
                activeClass = "active"
            else:
                activeClass = ""

            marker_list.append({"year" : yearpoint, "class" : activeClass})        

    else:
        error_message = list({"Error":"No Data found, Scrape to get data"})
    print(marker_list)
    # Close client
    status = Close_Connection_MongoDB(myClient) 

    return render_template(\
        "timeline.html", \
        timelineList = list(timeline_list), \
        decadeStart = decade_start, \
        decadeStop = decade_stop, \
        markerList = marker_list
        )
# --- End of index route ----#


if __name__ == "__main__":
    app.run(debug=True)