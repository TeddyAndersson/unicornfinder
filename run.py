#!/usr/local/bin/python2.7
# coding=utf-8
# -*- coding: utf-8 -*-
# Athour: Teddy Andersson.

#All imports for the project
from bottle import route, run, template, request, response, static_file, redirect
import bottle
import os
import requests


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


@route('/', method='GET')
def render_main_page():

    url = "http://unicorns.idioti.se"
    headers = {"Accept": "application/json"}
    r = requests.get(url, headers=headers)
    unicorns_list = r.json()
    return template('index', unicorns=unicorns_list)


@route('/unicorn/<id>', method='GET')
def render_unicorn_page(id):
    unicorn_url = "http://unicorns.idioti.se/" + str(id)
    unicorn_req = requests.get(unicorn_url, headers={"Accept": "application/json"})
    unicorn_dict = unicorn_req.json()

    lat = str(unicorn_dict.get("spottedWhere").get("lat"))
    lon = str(unicorn_dict.get("spottedWhere").get("lon"))
    nearby_res_list = get_nearby_lodges_list(lat, lon)

    print(str(nearby_res_list[0].get("name")))

    return template("unicorn", unicorn=unicorn_dict)


def get_nearby_lodges_list(lat, lon):
    lodges_radius = 7000
    nearby_url = get_nearby_lodges_url(lat, lon, lodges_radius)
    nearby_req = requests.get(nearby_url)
    nearby_response_json = nearby_req.json()
    while nearby_response_json.get("results").size == 0:
        nearby_url = get_nearby_lodges_url(lat, lon, (lodges_radius + 7000))
        nearby_req = requests.get(nearby_url)
        nearby_response_json = nearby_req.json()
        print(nearby_url)
    print("Final URL: " + nearby_url)
    return nearby_url


def get_nearby_lodges_url(lat, lon, radius):
    types = "lodging"
    key = "AIzaSyCJhyHp-740GGvy4bBLJatNOIOnru-4hfA"
    nearby_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + \
                 "location=" + lat + "," + lon + "&" + \
                 "radius=" + str(radius) + "&" + \
                 "types=" + types + "&" + \
                 "key=" + key
    return nearby_url

#command for running the service local.    
run(host='localhost', port=8080, debug=True, reloader=True)

#command for running the service on heroku. 
port = os.environ.get('PORT', 5000) #Get required port, default to 5000.
#run(host='0.0.0.0', port=port)
