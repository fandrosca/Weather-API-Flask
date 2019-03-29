#import libraries
from datetime import datetime
import os
import pytz
import requests
import math

#Key from the openweathermap website
API_KEY = 'b20dcab04464f8a1e2675c9d325e7b77'

#weather API
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

#define function using the API
def query_api(city):
    try:
        print(API_URL.format(city, API_KEY)) #API format
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
