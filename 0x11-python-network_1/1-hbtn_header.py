#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
'''
from urllib import request
import sys


with request.urlopen(sys.argv[1]) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
