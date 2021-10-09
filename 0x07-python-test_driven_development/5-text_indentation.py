#!/usr/bin/python3
# 5-text_indentation.py
# Juan Duque <3428@holbertonschool.com>

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    