# Dependencies
import os
import sys
from bs4 import BeautifulSoup as bs, re
from splinter import Browser
from datetime import datetime

# -----------------------------------------------------------------------------------------#
# Function to return Beautifulsoup
# -----------------------------------------------------------------------------------------#

# Function to create beautiful soup object, for the given url and browser
def Create_BeautifulSoup(url,browser):
    browser.visit(url)
    
    # Get html content of the visited page
    html_content = browser.html

    # Create a Beautiful Soup object, for the browser html
    soup = bs(html_content, 'html.parser')
    
    return soup  
# -- End of Create_BeautifulSoup -- #

# -----------------------------------------------------------------------------------------#
# Function to Scrape National Park Establishment Date from Wiki
# -----------------------------------------------------------------------------------------#
# Scrate National Park Establishment date from Wiki
def Scrape_EstablishDate():

    try:        
    # Chrome Driver
        executable_path = {'executable_path': '/Chromedrv/chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
    except:
        # On error, return Status as False, with empty value
        return_value = {"status":False,"Error":{}}

    print("driver")
    # -----------------------------------------------------------------------------------------#
    # National Park Detail
    # -----------------------------------------------------------------------------------------#
    try:
        # URL 
        url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'

        # Create a Beautiful Soup object, for the browser html
        soup = Create_BeautifulSoup(url,browser)

        # List to store Scrape data
        NatParkScrape = []  

        # Create a empty dictionary to store individual row
        NatParkDetail = {}

        # Parse through the table
        nat_park_body = soup.find("table",class_='wikitable').find("tbody").find_all("tr")
        for nat_park_row in nat_park_body:
            # NatParkDetail["name"] = nat_park_row.find("th").text.encode("utf-8")
            print(nat_park_row.encode("utf-8"))
            break
            # detail_cell = nat_park_row.find_all("td")
            # for cell in detail_cell:
            #     print(cell.text)
            # # NatParkDetail["image"] = detail_cell[0].text
            # NatParkDetail["location"] = detail_cell[1].text
            # NatParkDetail["date_established"] = detail_cell[2].text
            # NatParkDetail["area"] = detail_cell[3].text
            # NatParkDetail["description"] = detail_cell[5].text

            # Append the dictionary to the NatParkDetail list 
            NatParkScrape.append(dict(NatParkDetail))
        print(NatParkScrape)
        # quit browser
        browser.quit()

        # return value along with scrape status
        return_value = {"status":True,"value":NatParkScrape}
    except:
        # On error, return Status as False, with empty value
        print(sys.exc_info()[0])
        return_value = {"status":False}
        browser.quit()

    # return the Scrape result
    return return_value

# -- End of function Scrape_EstablishDate -- #


