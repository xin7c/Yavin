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


def send_message():
    TEXT_BOX= 'com.cmcm.live:id/toolbox_et_message'
    TEXT_SEND_BUTTON = 'com.cmcm.live:id/toolbox_btn_send'
    PIC_BUTTON = 'com.cmcm.live:id/iv_photo'
    PIC_LISR_BUTTON = 'com.cmcm.live:id/tv_select'
    PIC_SENT_BUTTON = 'com.cmcm.live:id/tv_photo_send'
    #拍照需要的权限
    ALL_TAKE_PIC1= 'com.huawei.camera:id/shutter_button'
    ALL_TAKE_PIC11 = 'com.huawei.camera:id/btn_done'

    ALL_TAKE_PIC2 = 'com.android.camera2:id/photo_video_button'
    ALL_TAKE_PIC22 = 'com.android.camera2:id/done_button'

    # 相册文件列表
    PHOTOS_LIST= 'com.cmcm.live:id/iv_icon'
    SLETE_BUTTON = 'com.cmcm.live:id/tv_select'
    SLEET_OK_button = 'com.cmcm.live:id/tv_photo_ok'
    #视频
    VIDEO_BUTTON = 'com.cmcm.live:id/iv_video'
    VIDEO_TAKE_BUT = 'com.cmcm.live:id/view_count_down'
    VIDEO_SEND_BUT = 'com.cmcm.live:id/img_publish'
    #语音
    VOICE_BUT = 'com.cmcm.live:id/iv_audio'
    VOICE_RECODING = 'com.cmcm.live:id/toolbox_audio'


    # 发送图片、语音、文本、视频消息
    poco(TEXT_BOX).click()
    text("验证第一句发送成功")
    time.sleep(3)
    poco(TEXT_SEND_BUTTON).click()
    sleep(5)

    # 图片
    poco(PIC_BUTTON).click()
    poco(PIC_LISR_BUTTON)[1].click()
    poco(PIC_SENT_BUTTON).click()
    poco.click([0.5, 0.5])
    print("图片发送成功")
    sleep(5)

    # 拍照
    poco(PIC_BUTTON).click()
    touch(Template("take_photo.png"))
    time.sleep(3)
    if poco(ALL_TAKE_PIC2).exists():
        poco(ALL_TAKE_PIC2).click()
        time.sleep(2)
        poco(ALL_TAKE_PIC22).click()
    time.sleep(3)
    # 问题：如何检验发送成功，对方收到了
    print("拍照图片发送成功")
    sleep(5)

    # 相册
    poco(VIDEO_BUTTON).click()
    touch(Template("photo_album.png"))
    sleep(2)
    poco(PHOTOS_LIST)[0].click()
    sleep(2)
    poco(SLETE_BUTTON).click()
    poco(SLEET_OK_button).click()
    poco.click([0.5, 0.5])
    sleep(3)
    print("相册图片发送成功")

    # 发送视频
    poco(VIDEO_BUTTON).click()
    time.sleep(3)
    # 录制10s，保存视频
    poco(VIDEO_TAKE_BUT).click()
    sleep(5)
    touch(Template("break.png"))
    poco(VIDEO_TAKE_BUT).click()
    time.sleep(10)
    poco(VIDEO_SEND_BUT).click()
    print("视频发送成功")
    sleep(5)

    # 发送语音消息
    poco(VOICE_BUT).click()
    poco(VOICE_RECODING).long_click(10)
    poco(VOICE_BUT).click()
    print("语音发送成功")
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
send_message()


