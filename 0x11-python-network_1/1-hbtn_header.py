#!/usr/bin/python3
"""
takes in a url, sends a request to the url
displays the value of the x-request-id variable
found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
