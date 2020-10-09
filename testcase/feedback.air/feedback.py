# -*- encoding=utf8 -*-

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.pages.HomePage_old import HomePage
from common.pages.MePage import MePage
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_control import *
from common.login.login import login_if_needed
from airtest.core.api import *
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

restart_app()
login_if_needed()

# 进入个人页
home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('冷启后没有来到主页')
home_page.goto_me_page()
sleep(5)

me_page = MePage()
if not me_page.in_current_page():
    raise AssertionError('进入我的页面失败')

while not poco(text='Feedback').exists():
    poco.swipe([0.5, 0.6], [0.5, 0.1], duration=0.1)


# gmail形式反馈 Account deletion, Troubleshoot, Feedback信息
def feedback():
    poco(text='Feedback').click()
    poco(text='Account deletion, Troubleshoot, Feedback').click()
    assert_equal(poco("android.webkit.WebView").offspring("start").exists(), True)
    poco("com.cmcm.live:id/bottomBtn").click()
    poco(text="Account Issues").click()
    assert_exists(Template('share_icon.png'), '没有吊起分享渠道')


feedback()
