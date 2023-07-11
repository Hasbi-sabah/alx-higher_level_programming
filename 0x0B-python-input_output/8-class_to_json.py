#!/usr/bin/python3
"""
Module for the function class_to_json()
"""
import json


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    return json.dumps(obj.__dict__)
