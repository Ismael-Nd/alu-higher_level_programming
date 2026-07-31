#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and prints its body."""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
