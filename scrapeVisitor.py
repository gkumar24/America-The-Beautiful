import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

park_ids =["NPSA","NPNH","ZION","ACAD","ARCH","DENA","KATM","GLAC","OLYM","SAGU","BADL","BIBE","BISC","CONG","YOSE","HALE","PINN","VOYA","WICA","WOTR","EVER","LACL","MEVE","SHEN","CANY","CRLA","GLBA","GRTE","GRBA","HOSP","ISRO","JOTR","WHSA","YELL","BRCA","CARE","DEVA","DRTO","JEFF","GRCA","KEFJ","KOVA","MACA","INDU","MORA","NOCA","ROMO","VIIS","CHIS","CUVA","LAVO","CAVE","GRSA","PEFO","HAVO","THRO","GAAR","GUMO","WRST","GRSM","SEKI","ROCA","BLCA"]

url = "https://irma.nps.gov/STATS/MvcReportViewer.aspx?_id=6ea6a4c1-e143-42aa-b109-bd2e2b2cb531&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fRecreation+Visitors+By+Month+(1979+-+Last+Calendar+Year)&_15=True&_16=True&_18=True&_19=True&_34=False&_35=False&_39=880px&Park="


# all_dataframes = []
allParks_df = pd.DataFrame()
for park_code in park_ids:
    i = 0
    l = []
    #scrape a given page
    page = requests.get(url + park_code)
    #turn it into soup object
    soup = BeautifulSoup(page.content, "html.parser")
    
    #scrape the rows of a table with the attribute cols="14"
    table = soup.find('table', attrs={'cols':'14'})
    if table is not None:
        # stole from stackflow verbatim
        table_rows = table.find_all('tr')

        #take these rows and convert then to be nice with dataframe class constructor
        for tr in table_rows:
            if(i > 1): #the first two rows are garbage, so dont append to l until two loops in
                td = tr.find_all('td')
                row = [r.text.replace(",","").strip() for r in td]                
                l.append(row)
            i+=1

        #send the array to the dataframe to be built
        park_df = pd.DataFrame(l, columns=["Year", "JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC", "Total"])

        # add park code to identify each of the park data
        park_df["park_code"] = park_code

        #append all of these dataframes into a large dataframes
        if allParks_df.empty:
            allParks_df = park_df
        else:
            allParks_df = pd.concat([allParks_df, park_df], ignore_index=True)

# out of forloop

# Check columns with numeric values, try converting it to numeric, if not fill with 0
cols = allParks_df.columns.drop("park_code")
for col in cols:
    allParks_df[col] = pd.to_numeric(allParks_df[col],errors='coerce').fillna(0)

# get current year, remove data from current year, and any year with year value as 0
current_year = datetime.date.today().year
allParks_df = allParks_df[allParks_df.Year != 0]
allParks_df = allParks_df[allParks_df.Year != current_year]

# export the dataframe into csv 
allParks_df.to_csv(f"static/collection/park.csv")

#Importing SqlAlchemy to use import DataFrame into Postgress.
import sqlalchemy
from config import password, username
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#converting to lower_case to match postgres naming conversion for this particular table
allParks_df.columns = [t.lower() for t in allParks_df.columns]

#Exporting tranformed file to Postgres. Appending since table heads already exist in Postgres
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/NationalParkDB')
engine.execute("delete FROM visitor_count")
allParks_df.to_sql('visitor_count', engine, if_exists='append', index=False)