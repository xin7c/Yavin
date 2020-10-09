# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from common.app.app_control import restart_app
from common.popup.featurelist_popup import featurelist_popup_window
from common.login.login import login_if_needed
from common.pages.HomePage_old import HomePage
from common.pages.MePage import MePage
from common.pages.MyFamPage import MyFamPage
from common.pages.FamilyChatPage import FamilyChatPage
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def speak_meg():
    # 上麦后发送图片信息
    time.sleep(5)
    poco("com.cmcm.live:id/vcall_small_mask_head_icon")[1].click()

    # 发送图片、语音、文本、视频消息
    poco("com.cmcm.live:id/toolbox_et_message").click()
    text("验证第一句发送成功")
    time.sleep(3)
    poco("com.cmcm.live:id/toolbox_btn_send").click()
    sleep(5)

    # 图片
    poco("com.cmcm.live:id/iv_photo").click()
    poco("com.cmcm.live:id/iv_pic")[1].click()
    poco("com.cmcm.live:id/tv_photo_send").click()
    poco.click([0.5, 0.5])
    print("图片发送成功")
    sleep(5)

    # 发送视频
    poco("com.cmcm.live:id/iv_video").click()
    time.sleep(3)
    exists(Template("toast_nopic.png"))
    print("上麦不能发送视频")
    sleep(5)

    # 发送语音消息
    poco("com.cmcm.live:id/iv_audio").click()
    poco("com.cmcm.live:id/toolbox_audio").click()
    exists(Template("toast_nospk.png"))
    print("上麦不能发送语音")
    sleep(5)

    # @人功能
    poco("com.cmcm.live:id/iv_audio").click()
    poco("com.cmcm.live:id/toolbox_et_message").click()
    text("@")
    time.sleep(10)
    poco("com.cmcm.live:id/layout_member_user_avater")[0].click()
    time.sleep(5)
    poco("com.cmcm.live:id/toolbox_btn_send").click()
    # 检验被@的人是否收到
    sleep(5)


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

speak_meg()
