import googlemaps
from datetime import datetime
from pprint import pprint

gmaps = googlemaps.Client(key='KEY')

# # Geocoding an address
# geocode_result = gmaps.geocode('kitsilano')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("richmond center",
#                                      "pacific center",
#                                      mode="transit",
#                                      departure_time=now)

# bounds = geocode_result[0]['geometry']['bounds']
# location = geocode_result[0]['geometry']['location']


def location_info(location):
    geocode_result = gmaps.geocode(location)

    north = geocode_result[0]['geometry']['bounds']['northeast']['lat']
    east = geocode_result[0]['geometry']['bounds']['northeast']['lng']
    south = geocode_result[0]['geometry']['bounds']['southwest']['lat']
    west = geocode_result[0]['geometry']['bounds']['southwest']['lng']

    location = geocode_result[0]['geometry']['location']

    bound = { 'north':north, 'east':east, 'south':south, 'west':west }

    dic = { 'bound':bound , 'location':location }

    pprint(dic)
    return dic

"""
{'bound': {'east': -123.1389362,
           'north': 49.27936860000001,
           'south': 49.2571768,
           'west': -123.1859637},
 'location': {'lat': 49.2683705, 'lng': -123.1683297}}
 """