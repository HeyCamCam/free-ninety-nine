#!/usr/bin/env python3

import requests
import os
from pushbullet import Pushbullet


# Get environment variable
PUSHBULLET_API_KEY = os.getenv('PUSHBULLET_API_KEY')

# Configure Pushbullet
pb = Pushbullet(PUSHBULLET_API_KEY)

# Configure requests for steamdb.info
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}
r = requests.get('https://steamdb.info/sales/?min_discount=95&min_rating=0', headers=headers)
status_code = str(r.status_code)

# Create Pushbullet note
#push = pb.push_note("SteamDB", "I got status code " + status_code + " when connecting to SteamDB")

# Send message
#push
