#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:setting_1.py
@time:2020/09/24
"""
from logging import log

__author__ = "xuchu"
__title__ = "设置页面测试用例"
__desc__ = "设置页面详细信息"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.pages.SettingPage import *


def setting():
    sp1 = SettingPage()
    # sp1.goto_setting_page()
    # sp1.restart_app()
    # sp1.home()
    # sp1.start_app()
    # print(Config.get_yaml().get("package_name", None))
    # assert_equal(1, 1, "1=1")
    sp1.go_me_page().snap("到个人主页")  # .back().back().back().start_app().go_me_page()
    # sp1.goto_setting_page().goto_network_ping().back().back()
    print(f"测试打印[{sp1.screen_size}]")
    # sp1.setting_page_instance().snap("after instance").restart_app().snap("重启啦~")


for i in range(1):
    logging.error(f"执行第{i+1}次 ===============")
    setting()
