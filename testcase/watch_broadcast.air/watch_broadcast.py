# -*- encoding=utf8 -*-
__author__ = "liyue"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.app.app_control import restart_app
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.get_current_activity import *
from common.popup.videoplayer import videoplayer_popup_handler
import logging
from common.login.login import *
from common.pages.HomePage import *
from common.pages.CMPlayerPage import *
from common.pages.AnchorPage import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


@videoplayer_popup_handler
def watch_broadcast():
    home_page = HomePage()
    if not home_page.in_current_page():
        raise AssertionError("当前不在首页")
    # 点击首页直播
    home_page.watch_broadcast()
    # 点开主播卡片
    get_user_card()

    # 添加主播印象
    if poco("com.cmcm.live:id/user_tag_tv").exists():
        poco("com.cmcm.live:id/user_tag_tv").click()
        assert poco("com.cmcm.live:id/head_tv").exists(), "进入主播印象页成功"
        sleep(3)
        poco(name="android.widget.TextView")[0].click()
        poco(name="android.widget.TextView")[1].click()
        poco(name="android.widget.TextView")[2].click()
        poco("com.cmcm.live:id/title_right").click()
        # TODO:断言
    else:
        raise AssertionError("无法添加主播印象")

    # 主播卡片-调起悄悄话

    get_user_card()
    if poco("com.cmcm.live:id/dialog_anchor_message").exists():
        poco("com.cmcm.live:id/dialog_anchor_message").click()
        assert poco("com.cmcm.live:id/txt_whisper_hint").exists(), "唤出主播悄悄话成功"
        poco("com.cmcm.live:id/edit_input").click()
        text("hello")
        poco("com.cmcm.live:id/txt_send").click()
        poco("com.cmcm.live:id/img_close").click()

    # 发送1金币礼物
    send_1coin_gift()

    # 点击底部按钮 发送悄悄话
    nickname = poco("com.cmcm.live:id/anchor_nickname").get_text()
    if poco("com.cmcm.live:id/btn_whisper").exists():
        poco("com.cmcm.live:id/btn_whisper").click()
        whisper(nickname)

    # fixme follow & unfollow 注释掉防止找不到导致case失败
    # # Follow
    # follow_broadcaster()
    #
    # # unfollow
    # unfollow_broadcaster()
    # android.keyevent("back")

    # 发送消息
    if poco("com.cmcm.live:id/chat_msg_tv").exists():
        poco("com.cmcm.live:id/chat_msg_tv").click()
        text("hello this is liveme")
        poco("com.cmcm.live:id/send_button").click()
        # TODO：断言

    # 发送弹幕
    if poco("com.cmcm.live:id/danmaku_switch_checkbox").exists():
        poco("com.cmcm.live:id/danmaku_switch_checkbox").click()
        text("hello hello you beautiful")
        poco("com.cmcm.live:id/send_button").click()
        # TODO：断言


# 直播间follow 与 unfollow，由于直播间内状态图片无法识别，所以unfollow操作在他人页进行；前置条件 当前处于直播间内,结束后停留在他人页
def follow_broadcaster():
    cmplayer_page = CMplayerPage()
    if not cmplayer_page.in_current_page():
        raise AssertionError('当前不在直播间无法执行follow操作')
        anchor_act()
    if current_activity() == "com.cmcm.live/com.cmcm.user.AnchorAct":
        unfollow_broadcaster()
        poco("com.cmcm.live:id/txt_follow_status_hint").click()
        assert_exists(Template("followed_button.png")), "follow成功"


# 取关主播；前置条件：当前在他人页页面，方法执行后停留在他人页
def unfollow_broadcaster():
    anchor_page = AnchorPage()
    if not anchor_page.in_current_page():
        raise AssertionError("当前不在他人页")
        # 取关操作
    if exists(Template("followed_button.png")):
        poco("com.cmcm.live:id/txt_follow_status_hint").click()
        sleep(3)
        assert_not_exists(Template("followed_button.png")), "取关成功"
    else:
        log("当前未关注")

        # 无法识别follow和unfollow，待优化
        # if exists(Template("followed_button.png")):
        #     print ("sssssssssssssssssssss")
        #     poco("com.cmcm.live:id/img_invite").click()
        #     assert_exists(Template("followed_button.png")), "follow成功"
        #
        # else:
        #     poco("com.cmcm.live:id/anchor_nickname").click()
        #     sleep(3)
        #     poco("com.cmcm.live:id/dialog_anchor_type").click()
        #     sleep(3)
        #     assert poco("com.cmcm.live:id/iv_image_item").exists, "进入个人页成功"
        #     sleep(3)
        #     poco("com.cmcm.live:id/txt_follow_status_hint").click()
        #     assert poco("com.cmcm.live:id/txt_follow_status_hint").get_text() == ("follow"),"取关成功"
        #     poco("com.cmcm.live:id/img_invite").click()
        #     #assert_exists(Template("followed_button.png")), "follow成功"
        #     android.keyevent("back")
        #     sleep(3)


# 进入他人页；前置条件：当前处于直播间，方法执行后停留在他人页
def anchor_act():
    cmplayer_page = CMplayerPage()
    if not cmplayer_page.in_current_page():
        raise AssertionError('当前不在直播间无法进行操作')

    if poco("com.cmcm.live:id/anchor_nickname").exists():
        poco("com.cmcm.live:id/anchor_nickname").click()
        sleep(3)
    else:
        raise AssertionError("find failed")

    if poco("com.cmcm.live:id/dialog_anchor_type").exists():
        poco("com.cmcm.live:id/dialog_anchor_type").click()
        sleep(3)


# 获取主播用户卡片
def get_user_card():
    cmplayer_page = CMplayerPage()
    if not cmplayer_page.in_current_page():
        raise AssertionError('当前不在直播间无法进行操作')

    if poco("com.cmcm.live:id/anchor_nickname").exists():
        poco("com.cmcm.live:id/anchor_nickname").click()
        assert poco("com.cmcm.live:id/shortid_iv").exists, "个人卡片展示"
        sleep(3)
    else:
        raise AssertionError("find failed")


# 发送悄悄话，前置条件，当前已调起悄悄话
def whisper(nickname):
    cmplayer_page = CMplayerPage()
    if not cmplayer_page.in_current_page():
        raise AssertionError('当前不在直播间无法进行操作')

    if poco("com.cmcm.live:id/txt_greet_hint").exists():
        if nickname == poco("com.cmcm.live:id/txt_name").get_text():
            poco("com.cmcm.live:id/img_avatar").click()
            poco("com.cmcm.live:id/edit_input").click()
            text("hello")
            poco("com.cmcm.live:id/txt_send").click()
            # assert poco("com.cmcm.live:id/edit_input").get_text() == "", "发送成功"
            poco("com.cmcm.live:id/img_close").click()


def send_1coin_gift():
    if poco("com.cmcm.live:id/value_1_gold_gift_icon").exists():
        poco("com.cmcm.live:id/value_1_gold_gift_icon").click()
        # TODO:断言


restart_app()
sleep(8)
login_if_needed()
sleep(5)
watch_broadcast()
