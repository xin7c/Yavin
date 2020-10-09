# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from common.popup.featurelist_popup import featurelist_popup_window
from airtest.core.api import *
from common.pages.HomePage_old import HomePage
from common.pages.MePage import MePage
from common.pages.SettingPage import SettingPage
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def ping():
    if poco(text = 'Upload diagnosis report').exists():
        poco(text = 'Upload diagnosis report').click()
    else:
        raise AssertionError('ping失败，通知检查')



restart_app()
login_if_needed()
featurelist_popup_window()

home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('进入我的页面失败')
home_page.goto_me_page()
sleep(5)

me_page = MePage()
if not home_page.in_current_page():
    raise AssertionError('进入我的页面失败')


setting_page = SettingPage()
setting_page.goto_setting_page()
if not setting_page.in_current_page():
    raise AssertionError('进入设置页失败')
setting_page.goto_network_ping()

ping()


