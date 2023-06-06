#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        k = i * 10 + j
        if k == 89:
            print("{:02d}".format(k))
        else:
            print("{:02d}, ".format(k), end='')
