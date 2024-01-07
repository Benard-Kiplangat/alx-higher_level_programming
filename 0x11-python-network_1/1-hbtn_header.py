#!/usr/bin/python3
"""
A script that takes a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found
in the header of the response
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv
    req = Request(argv[1])
    with urlopen(req) as r:
        headers = r.info()
        print(headers['X-Request-Id'])
