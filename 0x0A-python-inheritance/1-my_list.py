#!/usr/bin/python3
# 1-my_list.py
# Juan Duque <3428@holbertonschool.com>
"""Define new Mylist"""


class MyList(list):
    """printing new sorte values"""

    def print_sorted(self):
        print(sorted(self))
