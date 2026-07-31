#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response to a URL."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
