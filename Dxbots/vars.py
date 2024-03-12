# Copyright (C) 2024 DX-MODS
#Licensed under the  MIT License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = environ.get('API_ID',"24953797") 
    API_HASH = environ.get('API_HASH',"f5a80bf6f55664689631266f3eb6d1ce") 
    BOT_TOKEN = environ.get('BOT_TOKEN',"7008143481:AAEuHzuKUPo4F2x4aT89PF_8l5p0L8oBvvk")
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6488346050").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = environ.get('OWNER_USERNAME',"Shashankls")
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
       # URL = "https://{}/".format(FQDN)
       URL = FQDN
    else:
        #URL = "https://{}/".format(FQDN)
        URL = FQDN 
    DATABASE_URL = environ.get('DATABASE_URL',"mongodb+srv://Shashanklsxm:shashank.ls1324@cluster0.wltjc4b.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1006488346050")).split())) 
