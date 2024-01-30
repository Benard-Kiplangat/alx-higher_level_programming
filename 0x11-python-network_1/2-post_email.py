#!/usr/bin/python3
"""
A script that takes a URL and email, sends a POST request to
the passed URL with the email as a parameter, then displays
the body of the response
"""


if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(argv[1], data)

    with request.urlopen(req) as r:
        body = r.read()
        print(body.decode('utf-8'))
