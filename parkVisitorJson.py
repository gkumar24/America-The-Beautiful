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
visitor_select = "SELECT park_code, avg_jan, avg_feb, avg_mar, avg_apr, avg_may, avg_jun, avg_jul, avg_aug, avg_sep, avg_oct, avg_nov, avg_dec, avg_monthly, great_month FROM public.visitor_average"
visitor_df = pd.read_sql(visitor_select, connection)

visitor_df.to_json("static/json/visitAvg.json")