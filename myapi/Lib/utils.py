import requests
from . import ms_globals

BASE_URI = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"


def get_address_details(address):
    if not address:
        return {}

    url = BASE_URI % (address, ms_globals.get_map_key())
    _response = requests.get(url)

    if _response.status_code != 200:
        raise Exception(_response.status_code)

    _response = _response.json()['results'][0]
    response = {}
    if _response:
        response["coordinate"] = {}
        response["coordinate"]["lat"] = _response['geometry']['location']["lat"]
        response["coordinate"]["lng"] = _response['geometry']['location']["lng"]
        response["address"] = _response['formatted_address']

    return response
