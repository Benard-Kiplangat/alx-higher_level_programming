#!/usr/bin/python3
"""
Ascript that fetches https://alx-intranet.hbtn.io/status and
displays response body and type"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
