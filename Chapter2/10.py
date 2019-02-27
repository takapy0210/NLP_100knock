# coding: utf-8

fname = 'hightemp.txt'

with open(fname) as f:
    lines = f.readlines()
    print(len(lines))