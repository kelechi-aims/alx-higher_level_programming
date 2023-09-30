#!/usr/bin/python3
# Script that fetches https://alx-intranet.hbtn.io/status

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body_bytes = response.read()
        body_string = body_bytes.decode("utf-8")

print("Body response:")
print("\t- type:", type(body_bytes))
print("\t- content:", body_bytes)
print("\t- utf8 content:", body_string)
