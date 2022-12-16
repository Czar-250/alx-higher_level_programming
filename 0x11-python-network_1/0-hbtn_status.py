#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as response:
        data = response.read()

        # decode gets the string representation of the message
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf8")))
