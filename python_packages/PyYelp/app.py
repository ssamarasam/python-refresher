'''
API - yelp
'''
import requests
import config

url = 'https://yelp.com/business/search'

headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
