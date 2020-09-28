# -*- encoding=utf8 -*-

__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.pages.HomePage import HomePage
from common.pages.MePage import MePage
from common.pages.MyFamPage import MyFamPage
from common.pages.FamilyChatPage import FamilyChatPage
from common.pages.FamilyInfoPage import FamilyInfoPage
from airtest.core.api import *
from common.app.app_control import restart_app
from common.popup.featurelist_popup import featurelist_popup_window
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 切换徽章
def change_kingdom(page):
    fam_name = page.get_family_name()
    worn_crest_name = page.get_worn_crest_name()
    if worn_crest_name is not None:
        assert_equal(fam_name, worn_crest_name, msg="已经佩戴了徽章，但徽章名字不等于家族名字！")
        log("已经佩戴了该家族的徽章，无法继续测试，退出")
        return
    # 佩戴徽章
    page.click_wear_crest()
    # 检查佩戴是否成功
    worn_crest_name = page.get_worn_crest_name()
    assert_equal(fam_name, worn_crest_name, msg="点击佩戴徽章后，对比徽章名和家族名失败！")
    time.sleep(3)
                
                
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

# 进入家族信息页面
family_chat_page.click_setup()
family_info_page = FamilyInfoPage()
if not family_info_page.in_current_page():
    raise AssertionError('进入家族信息页失败')


change_kingdom(family_info_page)
