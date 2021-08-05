"""
@Author: Rikesh Chhetri
@Date: 2021-08-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-08-04 08:03:30
@Title : Program Aim is to write a python program for loading
         real time stock details though an alphavantage api.
"""

import csv
import time
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

demo = os.getenv("API_KEY")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey={}'.format(demo)

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)
        time.sleep(3)
        
    

