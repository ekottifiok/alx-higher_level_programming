#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv
from urllib.error import HTTPError
if __name__ == '__main__':
    """You have to manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code"""
    try:
        with urlopen(Request(argv[1])) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
