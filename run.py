#!/usr/local/bin/python2.7
# coding=utf-8
# -*- coding: utf-8 -*-
# Athour: Teddy Andersson.

#All imports for the project
from bottle import route, run, template, request, response, static_file, redirect
import bottle
import os
import requests
import json


'''---------------------------- Code for Routes with static files -----------------------------'''

@route('/static/Css/<filename>')
def send_static(filename):
    "Hanterar CSS filer"
    return static_file(filename, root='./static/Css') 


@route('/static/JS/<filename>')
def send_static(filename):
    "Hanterar JavaScripts filer"
    return static_file(filename, root='./static/JS') 


@route('/static/fonts/<filename>')
def send_static(filename):
    "Hanterar Typsnitts filer"
    return static_file(filename, root='./static/Fonts') 


@route('/static/images/<filename>')
def send_static(filename):
    "Hanterar Typsnitts filer"
    return static_file(filename, root='./static/Images') 

'''----------------------- Code for Routes --------------------------'''
key = "AIzaSyACeeo4FSwZm6iBpP6sQ-ocIw-cuT7h8do"

@route('/', method='GET')
def main_page():
    url = "http://unicorns.idioti.se"
    headers = {"Accept": "application/json"}
    req = requests.get(url, headers=headers)
    unicorns_list = req.json()
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(unicorns_list)
    else:
        unicorns = sorted(unicorns_list, key=lambda k: k['name'])
        return template('index', unicorns=unicorns)


@route('/unicorn/<id>', method='GET')
def unicorn_page(id):
    unicorn_url = "http://unicorns.idioti.se/" + str(id)
    unicorn_req = requests.get(unicorn_url, headers={"Accept": "application/json"})
    unicorn_dict = unicorn_req.json()
    unicorn_dict["spottedWhen"]["date"] = unicorn_dict["spottedWhen"]["date"][:10]
    lat = str(unicorn_dict.get("spottedWhere").get("lat"))
    lon = str(unicorn_dict.get("spottedWhere").get("lon"))
    nearby_lodgings_dict = get_nearby_lodgings(lat, lon)
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        unicorn_json_dict = unicorn_dict
        unicorn_json_dict["nearbyLodgings"] = {"lodgings": nearby_lodgings_dict.get("lodgings"),
                                               "lodgingSearchRadius": nearby_lodgings_dict.get("radius")}
        return json.dumps(unicorn_json_dict)
    else:
        print nearby_lodgings_dict
        return template("unicorn", unicorn=unicorn_dict,
                    lodgings=nearby_lodgings_dict.get("lodgings"),
                    radius=nearby_lodgings_dict.get("radius"))


@route('/api', method='GET')
def api_page():
    return template("api-doc")


def get_nearby_lodgings(lat, lon):
    lodgings_radius = 7000
    nearby_url = get_nearby_lodging_url(lat, lon, lodgings_radius)
    nearby_req = requests.get(nearby_url)
    nearby_response_json = nearby_req.json()
    while len(nearby_response_json.get("results")) == 0:
        lodgings_radius = lodgings_radius + 7000
        nearby_url = get_nearby_lodging_url(lat, lon, (lodgings_radius))
        nearby_req = requests.get(nearby_url)
        nearby_response_json = nearby_req.json()
        print(nearby_url)
    print("Final URL: " + nearby_url)
    nearby_lodgings_list = nearby_response_json.get('results')
    lodgings_dict = {"radius": str(lodgings_radius), "lodgings": []}
    for lodge in nearby_lodgings_list:
        details_dict = get_place_details(lodge.get("place_id"))
        a_lodge_dict = {"name": lodge.get("name"),
                        "website": details_dict.get("website"),
                        "rating": details_dict.get("rating")}
        lodgings_dict["lodgings"].append(a_lodge_dict)
    return lodgings_dict


def get_place_details(place_id):
    place_url = "https://maps.googleapis.com/maps/api/place/details/json?" + \
                "key=" + key + "&" + \
                "placeid=" + place_id
    place_req = requests.get(place_url)
    website = place_req.json().get("result").get("website")
    rating = place_req.json().get("result").get("rating")
    place_details_dict = {"website": website, "rating": rating}
    return place_details_dict


def get_nearby_lodging_url(lat, lon, radius):
    types = "lodging"
    nearby_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + \
                 "location=" + lat + "," + lon + "&" + \
                 "radius=" + str(radius) + "&" + \
                 "types=" + types + "&" + \
                 "key=" + key
    return nearby_url

#command for running the service local.    
#run(host='0.0.0.0', port=8080, debug=True, reloader=True)

#command for running the service on heroku. 
port = os.environ.get('PORT', 5000) #Get required port, default to 5000.
run(host='0.0.0.0', port=port)
