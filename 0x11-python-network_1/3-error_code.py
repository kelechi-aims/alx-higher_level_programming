#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
'''
from urllib import request, error
import sys
from urllib.error import HTTPError

url = sys.argv[1]
if __name__ == '__main__':
    try:
        with request.urlopen(url) as response:
            body_bytes = response.read()
            body_string = body_bytes.decode('utf-8')
            print(body_string)
    except HTTPError as e:
        print('Error code:', e.code)
