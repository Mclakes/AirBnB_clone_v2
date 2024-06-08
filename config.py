#!/usr/bin/python3
"""Module Script for Configuring Environment Variables"""
from os import environ

HBNB_ENV = environ.get("HBNB_ENV")
HBNB_MYSQL_USER = environ.get("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = environ.get("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = environ.get("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = environ.get("HBNB_MYSQL_DB")
HBNB_TYPE_STORAGE = environ.get("HBNB_TYPE_STORAGE")
