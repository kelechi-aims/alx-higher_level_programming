#!/usr/bin/python3
for chr in range(97, 123):
    if chr != 101 and chr != 113:
        print("{:c}".format(chr), end='')
