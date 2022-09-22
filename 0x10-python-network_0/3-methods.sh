#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -i -s "$1" | grep -w Allow | cut -d' ' -f 2-
