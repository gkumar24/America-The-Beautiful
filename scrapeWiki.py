# Dependencies
import datetime
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# URL of page to be scraped
url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'

#Create html that will read tables
tables = pd.read_html(url)
tables

#create columns to drop data from the html table.

df = tables[1]
df.columns = ['Name', 'Image', 'Location', 'Date established as park','Area (2018)[10]','Recreation vistors (2018)[5][9]','Description']
#df.head()
df.head()

#Cleaning the data, eliminating the image and location columns
timeline_df = df[["Name", "Date established as park","Area (2018)[10]","Recreation vistors (2018)[5][9]","Description"]]
timeline_df.head()

#cleaning up date column, determining if all rows match; 
df.loc[2:, 'Date established as park'].head(62)

#Using split and lamda to isolate the year of establishment
timeline_df["year_established"] = timeline_df["Date established as park"].apply(lambda x:x.split()[-1].replace(",", " "))
# timeline_df

timeline_df["year_established"] = timeline_df["year_established"].str.split("[", n=1, expand=True)[0]
# timeline_df["Name"] = timeline_df["Name"].str

timeline_df.rename(columns = {'Name':'name'}, inplace = True)
timeline_df.rename(columns = {'Date established as park':'date_established'}, inplace = True)
timeline_df.rename(columns = {'Area (2018)[10]':'area'}, inplace = True)
timeline_df.rename(columns = {'Recreation vistors (2018)[5][9]':'recreation_visitors'}, inplace = True)
timeline_df.rename(columns = {'Description':'description'}, inplace = True)

timeline_df["park_name"] = timeline_df["name"].str.replace('[\u00BF-\u1FFF\u2C00-\uD7FF]','', regex=True)

# print(timeline_df)


#Converting to CSV file to add Key column for National Parks
timeline_df.to_csv("static/collection/timeline.csv", encoding="utf-8", index=False)


#Importing SqlAlchemy to use import DataFrame into Postgress.
import sqlalchemy
from config import password, username
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#converting to lower_case to match postgres naming conversion for this particular table
timeline_df.columns = [t.lower() for t in timeline_df.columns]

#Exporting tranformed file to Postgres. Appending since table heads already exist in Postgres
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/NationalParkDB')
engine.execute("delete FROM timeline")
timeline_df.to_sql('timeline', engine, if_exists='append', index=False)

