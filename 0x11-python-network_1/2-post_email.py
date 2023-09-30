#!/usr/bin/python3
'''
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
'''

from urllib import request, parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({'email': email}).encode('ascii')
if __name__ == "__main__":
    with request.urlopen(url, data=data) as response:
        body_bytes = response.read()
        body_string = body_bytes.decode('utf-8')
        print(body_string)
