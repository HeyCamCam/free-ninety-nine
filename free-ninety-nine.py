#!/usr/bin/env python3
# Python version is $PYTHON_VERSION

import requests
import os
from pushbullet import Pushbullet


# Get environment variable
PUSHBULLET_API_KEY = os.getenv('PUSHBULLET_API_KEY')

# Configure Pushbullet
pb = Pushbullet(PUSHBULLET_API_KEY)
push = pb.push_note("This is the title", "This is the body")

push
