# Purpose
# To create visitAvg.json file
import pandas as pd

#Importing SqlAlchemy to use import DataFrame into Postgress.
import sqlalchemy
from config import password, username
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Exporting tranformed file to Postgres. Appending since table heads already exist in Postgres
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/NationalParkDB')

# establish a connection
connection = engine.connect()

 # Read title table into dataframe
linear_select = "SELECT park_code1, park_code2, park_name1, park_name2, lon1, lon2, lat1, lat2, linear_distance FROM public.linear_distance_between_park order by park_name1, linear_distance"
linear_df = pd.read_sql(linear_select, connection)
linear_df.set_index(["park_code1","park_code2"], inplace = True) 
# linear_df.groupby(["park_code1"])

linear_df.to_json("static/json/linearDistance.json")