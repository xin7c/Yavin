#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:why_import_error.py
@time:2020/11/09
"""
import os
import sys
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.config import Config

if __name__ == '__main__':
    c = Config()
    print(c.get_package_name)
