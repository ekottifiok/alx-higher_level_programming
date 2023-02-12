#!/usr/bin/python3
"""Write a Python script that
fetches https://alx-intranet.hbtn.io/status
"""
from requests import request

if __name__ == '__main__':
    """"""
    with request('GET', "https://alx-intranet.hbtn.io/status") as reponse:
        print("Body response:")
        print("\t- type: {}".format(type(reponse.text)))
        print("\t- content: {}".format(reponse.text))
