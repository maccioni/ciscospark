#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Simple script to list the Spark room for the current user

The package natively retrieves your Spark access token from the
SPARK_ACCESS_TOKEN environment variable.  You must have this environment
variable set to run this script.
"""

from __future__ import print_function
from ciscosparkapi import CiscoSparkAPI


# Create a CiscoSparkAPI connection object; uses your SPARK_ACCESS_TOKEN
api = CiscoSparkAPI() 
# Get info on authenticated Spark User
me = api.people.me()

print("Searching existing rooms for " + me.displayName + " (id:" + me.id + ")\n")
print("     Room Name:                                  Room ID:")
print("================================================================================")

# Get room list
rooms = api.rooms.list() 
existing_demo_rooms = [room for room in rooms ]

if existing_demo_rooms:
    counter=0
    for room in existing_demo_rooms:
        print(room.title + ": " + room.id)
        counter += 1
    print("\nThe current Spark user is part of " + repr(counter) + " Spark rooms")
else:
    print("The current Spark user is not part of any Spark room")                             
