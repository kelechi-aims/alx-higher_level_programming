#!/usr/bin/python3
# Script that takes in a URL, sends a request to the URL and displaysthe
# value of the X-Request-Id variable found in the header of the response.
from urllib import request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
