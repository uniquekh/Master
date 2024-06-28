#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6711520175:AAG-brvJUQhgUAT7NGk62LBfyodNj_Lirh8")
    API_ID = int(os.environ.get("API_ID", "20995706"))
    API_HASH = os.environ.get("API_HASH", "3240c1615daa1fbbca45c34a9bb8ecf2")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7146854725")
