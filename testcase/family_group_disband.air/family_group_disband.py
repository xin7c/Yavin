# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import *
from common.app.app_control import restart_app
from common.popup.featurelist_popup import featurelist_popup_window
from common.login.login import login_if_needed
from common.pages.HomePage import HomePage
from common.pages.MePage import MePage
from common.pages.MyFamPage import MyFamPage
from common.pages.FamilyChatPage import FamilyChatPage
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#解散 或者 退出家族
def disband_fam_group():
    LEAVE_FAM = 'com.cmcm.live:id/tv_info_dismiss'
    SURE = 'com.cmcm.live:id/button1'
    QUIT = 'com.cmcm.live:id/button2'

    poco.swipe([0.2,0.9],[0.2,0.2])
    poco(LEAVE_FAM).click()
    #点击取消按钮
    poco(QUIT).click()
    #点击确定按钮
    poco(LEAVE_FAM).click()
    poco(SURE).click()
    sleep(3)

    if not my_fam_page.in_current_page():
        raise AssertionError('家族结算失败/离开失败')



restart_app()
login_if_needed()
featurelist_popup_window()

# 进入个人页
home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('冷启后没有来到主页')
home_page.goto_me_page()
sleep(5)

me_page = MePage()
if not me_page.in_current_page():
    raise AssertionError('进入我的页面失败')

# 进入家族列表页
me_page.click_my_fam()
my_fam_page = MyFamPage()
if not my_fam_page.in_current_page():
    raise AssertionError('进入家族列表页面失败')

# 进入第一个家族的群聊页面
my_fam_page.click_my_first_fam()
family_chat_page = FamilyChatPage()
if not family_chat_page.in_current_page():
    raise AssertionError('进入家族聊天页面失败')
sleep(5)

family_chat_page.click_setup()
sleep(3)

disband_fam_group()

