#!/usr/bin/python3
""" Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    """The email must be sent in the email variable"""
    with urlopen(Request(
            argv[1],
            urlencode({'email': argv[2]}).encode('ascii'))) as response:
        print(response.read().decode("utf-8", "replace"))
