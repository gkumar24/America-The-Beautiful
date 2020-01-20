# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

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