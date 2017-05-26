#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Simple ciscosparkapi demonstration script to post a message in a Spark Room
"""
from ciscosparkapi import CiscoSparkAPI

#
# FIX-ME
# you must fill in the variable below and change the message and the image url as desired.
# You can find out the Rooms names and related IDs using the RoomListSpark.py script
#
my_token   = ""
bot_token  = ""
SPARK_ROOM_NAME = ""
SPARK_ROOM_ID = ""
SPARK_MESSAGE = u"Cisco Spark rocks!  \ud83d\ude0e"
SPARK_FILE_URL = "https://developer.ciscospark.com/images/logo_spark_lg@256.png"

# Send a test messgae using my Spark token
my_api = CiscoSparkAPI(my_token)
my_api.messages.create(SPARK_ROOM_ID, text=SPARK_MESSAGE)

# Send a file using bot Spark token
bot_api = CiscoSparkAPI(bot_token)
bot_api.messages.create(SPARK_ROOM_ID, files=[SPARK_FILE_URL])
