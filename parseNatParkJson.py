import pandas as pd
import json

# read the geo Json file into dictionary
with open("static/json/natparks_geo.json") as natParkFile:
    natPark_dict = json.load(natParkFile)

# create a empty dataframe to store the park information
natPark_df = pd.DataFrame()

# parse the geo json, to a dataframe columns
natPark_df["park_Code"] = [feature["properties"]["Code"] for feature in natPark_dict["features"]]
natPark_df["park_name"] = [feature["properties"]["Name"] for feature in natPark_dict["features"]]
natPark_df["longitude"] = [feature["geometry"]["coordinates"][0] for feature in natPark_dict["features"]]
natPark_df["latitude"] = [feature["geometry"]["coordinates"][1] for feature in natPark_dict["features"]]

#Importing SqlAlchemy to use import DataFrame into Postgress.
import sqlalchemy
from config import password, username
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#converting to lower_case to match postgres naming conversion for this particular table
natPark_df.columns = [t.lower() for t in natPark_df.columns]

#Exporting tranformed file to Postgres. Appending since table heads already exist in Postgres
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/NationalParkDB')
engine.execute("delete FROM park_coordinates")
natPark_df.to_sql('park_coordinates', engine, if_exists='append', index=False)
