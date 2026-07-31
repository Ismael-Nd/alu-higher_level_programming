#!/usr/bin/python3
"""Sends a search query to the search_user endpoint and prints a result."""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
