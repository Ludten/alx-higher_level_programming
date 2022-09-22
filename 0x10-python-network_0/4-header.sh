#!/bin/bash
# takes in a URL and displays the body of the response
curl -H "X-School-User-Id: 98" -sL "$1"
