#!/bin/bash
# Sends a request to that URL, and displays the size of the body of the response
curl -so /dev/null -w "%{size_download}\n" $1
