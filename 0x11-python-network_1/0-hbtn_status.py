#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as req:
    res = req.read()
print("Body response:")
print(f"    - type: {type(res)}")
print(f"    - content: {res}")
print(f"    - utf8 content: {req.msg}")
