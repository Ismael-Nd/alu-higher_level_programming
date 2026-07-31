#!/usr/bin/python3
"""Fetches a URL and prints its body, or the HTTP error code on failure."""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
