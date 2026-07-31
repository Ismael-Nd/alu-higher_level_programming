#!/bin/bash
# Displays the response body of a URL, only when the status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -s "$1"
