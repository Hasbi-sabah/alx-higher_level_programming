#!/usr/bin/python3
"""
Python script that takes in a URL, and displays the value of the X-Request-Id variable.
"""
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as req:
    info = req.info()
    print(info['X-Request-Id'])
