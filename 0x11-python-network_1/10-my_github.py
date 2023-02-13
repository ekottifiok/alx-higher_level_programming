#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
from requests import request
from sys import argv

if __name__ == '__main__':
    """The first argument will be your username"""

    with request('POST', 'https://api.github.com/user',
                 headers={
                     "Accept": "application/vnd.github+json",
                     "Authorization": "Bearer {}".format(argv[2]),
                     "X-GitHub-Api-Version": "2022-11-28"
                 }) as response:
        try:
            data = response.json()
            if data == {}:
                print("No result")
            else:
                print(data.get('id'))
        except ValueError:
            print('None')
