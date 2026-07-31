#!/bin/bash
# Displays the size, in bytes, of the body of the response from a URL
curl -sw "%{size_download}\n" -o /dev/null "$1"
