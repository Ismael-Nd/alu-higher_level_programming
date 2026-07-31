#!/usr/bin/python3
"""Sends a POST request with an email parameter and prints the response."""
from urllib.request import urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    with urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
