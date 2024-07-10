#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7158015873:AAGg4IlXLhPey6_M_0x2CC4J-5wZut-o6Kc")
    API_ID = int(os.environ.get("API_ID", "21179966"))
    API_HASH = os.environ.get("API_HASH", "d97919fb0a3c725e8bb2a25bbb37d57c")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7326397503")
