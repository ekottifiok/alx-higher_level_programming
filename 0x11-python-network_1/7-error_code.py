#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email
and sends a POST request to the passed URL
"""
from requests import request
from sys import argv

if __name__ == '__main__':
    """If the HTTP status code is greater than or equal to 400"""
    with request('GET', argv[1]) as response:
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print('Index')
