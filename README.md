# America-The-Beautiful
UOM Data Viz Project 2 - America the Beautiful - all about National Parks

---

## File Detail
| File Name | Description |
| ---| --- |
| app.py | Flask Web Application - Execution file |
| config.py | `git ignored` need to be created, if cloned from repository |
| scrapeVisitor.py | Scraping the Visitor Count data for each of the Park |
| scrapeWiki.py | scraping the National Park timeline data |
| parkVisitorJson.py | creates `static/json/visitAvg.json` needed in Maps page |
| parseNatParkJson.py | get data for park coordinates from `static/json/natparks_geo.json` |
| parkLinearDistanceJson.py | creates a json file `static/json/linearDistance.json`, to get the distance between each parks |
| MultipleLinearRegression.ipynb | Maching Learning analysis of park visitor count data |

### Application Web page, and Templates
Folder: [templates](templates)
| File Name | Description |
| ---| --- |
| index.html | Application home page |
| timeline.html | National Park Time Line |
| parkmap.html | Leaflet Map page, showing the visitor count by month |
| visitors.html | Top 10 and Least 10 visited parks |

### Javascript Files
Folder: [static\js](static\js)
| File Name | Description |
| ---| --- |
| leaflogic.js | Create a leaflet map, to show visitor count by month |
| timeline.js | National Park Time Line |

---
---
## Running the Application
**1. create 'config.py' under America-The-Beautiful folder**

    `username = "<postgres DB user id>"`

    `password = "<postgres DB password>"`

**2. Run Flask application**

* open git bash terminal for the application base path

    `open git bash`

* Activate the Python environment

    `source activate PythonWebMongo`

* Run the flask application

    `export FLASK_APP=app.py`

    `flask run`

* Open page from the link the application is running on.

    http://127.0.0.1:5000/









