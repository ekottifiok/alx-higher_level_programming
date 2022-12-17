#!/bin/bash
# a script that causes server to respond with message
curl -sLX HEAD -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
