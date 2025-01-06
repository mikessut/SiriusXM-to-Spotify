"""
https://xmplaylist.com/api/documentation
"""
import requests


def coffeehouse():
    r = requests.get('https://xmplaylist.com/api/station/thecoffeehouse')
    return r.json()
