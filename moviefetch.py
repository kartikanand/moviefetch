#! /usr/bin/env python

import os
import re
import sys

import requests

OMDB_API_URL = 'https://www.omdbapi.com'
pattern = re.compile('([^\s\w]|_)+')

def find_movie(name, year=None):
    # strip characters other than alpha-numeric
    # for some movies this has a better chance of a direct hit
    name = pattern.sub('', name)

    # create payload as per OMDB API spec
    payload = {
        't': name,
        'apikey': os.getenv('OMDB_API_KEY', '')
    }

    # if we have movie year, then add it to payload
    # this increases the chance of a direct hit
    if year:
        payload['y'] = year

    req = requests.get(OMDB_API_URL, params=payload)

    # get json object from response object
    # this is then passed to a movie stats object
    movie_json = req.json()

    return movie_json

def display_movie(movie_json):
    pass


if __name__ == '__main__':
    try:
        movie_name =  sys.argv[1]
    except IndexError:
        print('Please provide a movie name')
        sys.exit(1)

    movie_json = find_movie(movie_name)

    if movie_json["Response"] == "False":
        print('Movie not found')
        sys.exit(1)

    display_movie(movie_json)

