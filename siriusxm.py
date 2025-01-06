"""
https://xmplaylist.com/api/documentation
"""
import requests


def get_channel(channel: str):
    """
    Some known channels:
        thecoffeehouse
        lifewithjohnmayer
        theblend
        thebridge
    """
    r = requests.get(f'https://xmplaylist.com/api/station/{channel}')
    return r.json()
