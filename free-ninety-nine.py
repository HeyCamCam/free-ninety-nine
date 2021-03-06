#!/usr/bin/env python3

import os
import re
import requests
from bs4 import BeautifulSoup as soup
from pushbullet import Pushbullet


# Get environment variable
PUSHBULLET_API_KEY = os.getenv('PUSHBULLET_API_KEY')

# Configure Pushbullet
pb = Pushbullet(PUSHBULLET_API_KEY)

# Configure requests for steamdb.info
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}
website = requests.get('https://steamdb.info/sales/?min_discount=95&min_rating=0', headers=headers)

# configure beautifulsoup
website = soup(website.text, 'html.parser')

# instantiate an empty list that will store urls
STEAM_GAMES = []

# read website using beautiful soup and find the game urls
for link in website.find_all('a', {'href': re.compile(r'com\/app')}):
  STEAM_GAMES.append(link['href'])

# print URLs
print(STEAM_GAMES)

# Create Pushbullet note if free games are available
if not STEAM_GAMES:
  print("There are currently 0 free Steam games")
else:
  pb.push_note("SteamDB", "The following games are free " + str(STEAM_GAMES))
