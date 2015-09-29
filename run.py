#!/usr/local/bin/python2.7
# coding=utf-8
# -*- coding: utf-8 -*-
# Athour: Teddy Andersson.

#All imports for the project
from bottle import route, run, template, request, response, static_file, redirect
import bottle
import os
import urllib2
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
    unicorn_list = r.json()
    return template('index', unicorn_list=unicorn_list)

@route('/unicorn/<id>', method='GET')
def render_unicorn_page(id):

    url = "http://unicorns.idioti.se/" + str(id)
    headers = {"Accept": "application/json"}
    r = requests.get(url, headers=headers)
    unicorn_dict = r.json()

    return template("unicorn", unicorn_dict=unicorn_dict)


#command for running the service local.    
run(host='localhost', port=8080, debug=True, reloader=True)

#command for running the service on heroku. 
port = os.environ.get('PORT', 5000) #Get required port, default to 5000.
#run(host='0.0.0.0', port=port)
