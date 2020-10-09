# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import *
from common.app.app_control import restart_app
from common.popup.featurelist_popup import featurelist_popup_window
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.pages.HomePage_old import HomePage
from common.pages.MePage import MePage
from common.pages.MyFamPage import MyFamPage
from common.pages.FamilyChatPage import FamilyChatPage
from common.pages.FamilyTastPage import FamilyTaskPage

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def group_task(Page):

    if poco(text = "Check in").exists():
        poco(text = "Check in").click()
        if exists(text = "You're not wearing this Kingdom Crest."):
            poco(text = "OK").click()
    if poco(text = "0/1").exists():
        poco(text = "Go").click()
        time.sleep(5)
        text("完成聊天Chat in Kingdom's group任务")
        poco("com.cmcm.live:id/img_left_group").click()
        time.sleep(5)
        if poco(text = "Claim").exists():
            poco(text = "Claim").click()
        else:
            assert AssertionError("聊天Chat in Kingdom's group任务失败")
    if poco(text = "0/5").exists():
        poco(text = "Go").click()
        for i in poco("com.cmcm.live:id/vcall_small_mask_head_icon"):
            i.click()
            time.sleep(30)
            i.click()
            touch(Template("hangup.png"))
        poco("com.cmcm.live:id/img_left_group").click()
        time.sleep(5)
        if poco(text="Claim").exists():
            poco(text="Claim").click()
        else:
            assert AssertionError("上麦Audio Chat in Kingdom's group任务失败")
    if poco(text = "Recharge").exists():
        poco(text = "Recharge").click()
        time.sleep(5)
        assert poco('com.cmcm.live:id/txt_coins').exists(), '进入充值页'
        poco("com.cmcm.live:id/img_left").click()



restart_app()
login_if_needed()
featurelist_popup_window()

# 冷启动后进入首页+进入个人页点击家族+进入第一个家族+进入家族聊天界面
home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('冷启后没有来到主页')
home_page.goto_me_page()
sleep(5)

me_page = MePage()
if not me_page.in_current_page():
    raise AssertionError('进入我的页面失败')
me_page.click_my_fam()
sleep(5)


my_fam_page = MyFamPage()
if not my_fam_page.in_current_page():
    raise AssertionError('进入家族列表页面失败')
my_fam_page.click_my_first_fam()
sleep(5)

my_fam_chat_page = FamilyChatPage()
if not my_fam_chat_page.in_current_page():
    raise AssertionError('进入家族聊天页面失败')

family_tast = FamilyTaskPage()
family_tast.check_goto_task()
if not family_tast.check_goto_task():
    raise AssertionError('进入家族任务页面失败')

group_task(FamilyTaskPage)
