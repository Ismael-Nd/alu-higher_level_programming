#!/bin/bash
# Displays the size, in bytes, of the body of the response from a URL
curl -s -w "%{size_download}\n" -o /dev/null "$1"
