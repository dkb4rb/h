#!/usr/bin/python3
# 8-class_to_json.py
# Juan Duque <3428@holbertonschool.com>

import json


def class_to_json(obj):
    return obj.__dict__
