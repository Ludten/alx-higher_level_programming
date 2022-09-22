#!/bin/bash
# takes in a URL and displays the size of the body of the response
curl -Is "$1" | awk -v IGNORECASE=1 '/^Content-Length/ { print $2 }'
