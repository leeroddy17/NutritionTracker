import requests
import json
import pandas as pd


api_id = '15aba186'
api_key = 'f031b8ad950cd14549bef2cedb080529'



headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-app-id': api_id,
            'x-app-key': api_key,
            'x-remote-user-id': '0'
}

def get_facts(q):
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

    query = {
        "query":q
    }

    response = requests.request("POST", url, headers=headers, data=query)
    dictionary = response.json()
    return dictionary['foods'][0]

def get_hits(q):
    url = 'https://trackapi.nutritionix.com/v2/search/instant?query=' + q
    response = requests.request("GET", url, headers=headers)
    dictionary = response.json()

    options = []
    for item in dictionary['common']:
        options.append(item['food_name'])
        if len(options) == 10: # Caps the size at 10
            break

    return options