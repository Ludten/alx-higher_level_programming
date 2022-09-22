#!/bin/bash
# takes in a URL and displays the body of the response
curl -sL -H 'X-School-User-Id: 98' "$1"
