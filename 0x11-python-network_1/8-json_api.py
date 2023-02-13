#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email
and sends a POST request to the passed URL
"""
from requests import request
from sys import argv

if __name__ == '__main__':
    """The letter must be sent in the variable q"""
    if len(argv) < 2:
        argv.append("")
    with request('POST', "http://0.0.0.0:5000/search_user",
                 data={'q': argv[1]}) as response:
        try:
            data = response.json()
            if data == {}:
                print("No result")
            else:
                print("[{}] {}".format(data.get('id'), data.get('name')))
        except ValueError:
            print('Not a valid JSON')
