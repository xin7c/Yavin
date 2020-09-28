#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:App.py
@time:2020/09/22
"""
from airtest.core.android.adb import ADB
from airtest.core.api import assert_equal

from common.pages.BasePage import BasePage


class App(BasePage):
    def __init__(self):
        super().__init__()

    def start(self):
        pass


if __name__ == '__main__':
    app = App()
