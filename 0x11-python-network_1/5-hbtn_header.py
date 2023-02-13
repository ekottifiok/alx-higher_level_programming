#!/usr/bin/python3
"""Write a Python script that
fetches a url that was passed in by argument
"""
from requests import request
from sys import argv

if __name__ == '__main__':
    """You must use the packages requests and sys"""
    argv.append('https://alx-intranet.hbtn.io')
    with request('GET', argv[1]) as response:
        print(response.headers.get("x-request-id"))
