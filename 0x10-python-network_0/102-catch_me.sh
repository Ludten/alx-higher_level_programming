#!/bin/bash
# a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -H 'Origin: HolbertonSchool' -X PUT -d "user_id=98" -sL `curl -X PUT -o /dev/null -s -w "%{redirect_url}" 0.0.0.0:5000/catch_me`
