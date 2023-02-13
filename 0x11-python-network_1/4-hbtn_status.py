#!/usr/bin/python3
"""Write a Python script that
fetches https://alx-intranet.hbtn.io/status
"""
from requests import request

if __name__ == '__main__':
    """You must use the packages requests and sys"""
    with request('GET', "https://alx-intranet.hbtn.io/status") as response:
        print("Body response:\n\t- type: {}\n\t- content: {}" .format(
            type(response.text),
            response.text))
