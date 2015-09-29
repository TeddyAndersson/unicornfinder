#!/usr/local/bin/python2.7
# coding=utf-8
# -*- coding: utf-8 -*-
# Athour: Teddy Andersson.
import datetime
import os
import psycopg2
import urlparse
import MySQLdb

#local db connection Keep in mind that this is a MySql db connection and not for POSTGRE 
#cnx = MySQLdb.connect(user='root', db='', passwd='', host='localhost', charset= "utf8" )


#Connection for Postgre db
cnx = psycopg2.connect(database="", user="", password="", host="", port="5432")

