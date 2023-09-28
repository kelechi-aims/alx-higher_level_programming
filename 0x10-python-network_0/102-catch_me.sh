#!/bin/bash
# Use curl to make a POST request with the specific user agent
curl -sL -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
