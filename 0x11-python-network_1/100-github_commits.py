#!/usr/bin/python3
"""Write a Python script that takes 2 arguments
in order to solve this challenge."""
from requests import request
from sys import argv

if __name__ == '__main__':
    """The first argument will be the repository name"""
    with request(
            'GET',
            'https://api.github.com/repos/rails/rails/commits') as response:
        if response.status_code >= 400:
            print(None)
        try:
            data = response.json()
            if data == {} or len(data) < 10:
                print("No result")
            else:
                for item in data[:10]:
                    print("{}: {}".format(
                        item.get('sha'),
                        item.get('commit').get('author').get('name')))
        except ValueError:
            print(None)
