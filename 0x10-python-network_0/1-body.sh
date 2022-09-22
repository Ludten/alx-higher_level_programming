#!/bin/bash
# takes in a URL and displays the body of the response
if [[ $(curl -o /dev/null -sL -w "%{http_code}" "$1") -eq 200 ]]; then curl -sL "$1"; fi
