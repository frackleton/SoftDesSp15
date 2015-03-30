"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
import pprint 


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    #put together input for get_json
    params = {'address':place_name}
    portion = urllib.urlencode(params)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?' + portion
    response_data = get_json(url)


    #uses output of get_json to get location
    lat_lng_dict = response_data['results'][0]['geometry']['location']
    #format dictionary to tuple
    return (lat_lng_dict['lat'],lat_lng_dict['lng'])



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    #get url pieces
    params = {'lat':latitude,'lon':longitude}
    portion = urllib.urlencode(params)
    #stop by location query. input lat and lng 
    mbta_url = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&'+portion#+'&format=json'
    #get info from url
    mbta_info = get_json(mbta_url)

    #pull out the name and distance of closest stop
    closest_distance= mbta_info['stop'][0]['distance']
    closest_stop = mbta_info['stop'][0]['stop_name']
    return (closest_stop, closest_distance)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.

    """
    coords= get_lat_long(place_name)
    stop_plus_distance =get_nearest_station(coords[0],coords[1])

    return stop_plus_distance[0] + ' is ' + stop_plus_distance[1] + ' miles from ' + place_name

if __name__ == '__main__':
    #pprint.pprint(get_json('https://maps.googleapis.com/m aps/api/geocode/json?address=Fenway%20Park'))
    #print get_lat_long("Fenway Park")  
    #print get_nearest_station(42.3466764,-71.0972178)
    print find_stop_near("Fenway Park")