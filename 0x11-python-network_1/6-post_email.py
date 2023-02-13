#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email
and sends a POST request to the passed URL
"""
from requests import request
from sys import argv

if __name__ == '__main__':
    """"""
    with request('POST', argv[1], data={'email': argv[2]}) as response:
        print(response.text)
