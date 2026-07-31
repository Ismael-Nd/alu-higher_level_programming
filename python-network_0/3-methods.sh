#!/bin/bash
# Displays all HTTP methods accepted by the server for a given URL
curl -s -X OPTIONS -I "$1" | tr -d '\r' | awk -F': ' '/^Allow/{print $2}'
