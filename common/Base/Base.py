#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:Base.py
@time:2020/09/21
"""
import logging
import os
import sys

from airtest.utils.logger import get_logger

from config import config

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))


class Base(type):
    def __new__(mcs, name, bases, attrs):
        # for k, v in attrs.items():
        #     print(f"attr_name: {k} attr_value: {v}")
        if name != "BasePage":
            attrs["new_cls_name"] = name
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        if name != "BasePage":
            cls.cls_name = name
            cls.page_ele_loc = config.page_ele_loc
            with open("package_name.txt", "r") as f:
                cls.package_name = f.read()
                if cls.package_name:
                    print("Base读取package_name.txt")
                else:
                    print("Base读取config.yaml")
                    cls.package_name = config.Config.get_yaml().get("package_name", None)
            logger = get_logger("airtest")
            logger.setLevel(logging.INFO)
            print(f"**********\n"
                  f"当前子类: {cls.cls_name}\n"
                  f"包名: {cls.package_name}\n"
                  f"**********\n")
            super().__init__(name, bases, attrs)
        else:
            print("[Base] BasePage __init__")
            cls.cls_name = name
            super().__init__(name, bases, attrs)
