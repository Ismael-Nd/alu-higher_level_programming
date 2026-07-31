#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response to a URL."""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
