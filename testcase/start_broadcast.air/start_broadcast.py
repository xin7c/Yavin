# -*- encoding=utf8 -*-

__author__ = "shilei"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.app.app_control import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.login.login import login_if_needed
from common.popup.featurelist_popup import *
from airtest.core.android import Android
from common.pages.HomePage import *
from common.pages.UpLivePage import *
from airtest.core.helper import log

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
android = Android()


def start_broadcasting():
    home_page = HomePage()
    uplive_page = UpLivePage()
    if not home_page.in_current_page():
        raise AssertionError("当前不在首页")
    home_page.click_uplive_button()
    if not uplive_page:
        raise AssertionError("当前不在准备直播页")

    # 选择tag
    if poco("com.cmcm.live:id/topic_arrow").exists():
        poco("com.cmcm.live:id/topic_arrow").click()
        for p in range(3):
            if poco("com.cmcm.live:id/tag_txt").exists():
                poco("com.cmcm.live:id/tag_txt")[p].click()
                sleep(2)
                poco("com.cmcm.live:id/tag_select_confirm_btn").click()
                sleep(3)

    # 选择美颜
    if poco("com.cmcm.live:id/iv_beauty").exists():
        poco("com.cmcm.live:id/iv_beauty").click()
        sleep(3)
        sticker()
        android.keyevent("back")
    else:
        return

    # 开始直播
    poco(uplive_page.click_start_uplive()).click()
    sleep(8)

    poco("com.cmcm.live:id/arrow_button").click()
    sleep(5)
    # 发公告
    if exists(Template("sticky_note.png")):
        touch(Template("sticky_note.png"))
        sleep(3)
        if poco("com.cmcm.live:id/tv").exists():
            poco("com.cmcm.live:id/tv")[1].click()
            text("follow me please")
            android.keyevent("back")

            # TODO 断言
    else:
        raise AssertionError("发公告失败")

    poco("com.cmcm.live:id/arrow_button").click()
    # 切换摄像头
    if exists(Template("switch_camera.png")):
        touch(Template("switch_camera.png"))
        poco("com.cmcm.live:id/arrow_button").click()
        touch(Template("switch_camera.png"))

    else:
        raise AssertionError("切换摄像头失败")

    poco("com.cmcm.live:id/arrow_button").click()

    # 静音与取消静音
    if exists(Template("mute.png")):
        touch(Template("mute.png"))
        sleep(5)
        poco("com.cmcm.live:id/arrow_button").click()
        touch(Template("mute.png"))
        sleep(3)

    poco("com.cmcm.live:id/arrow_button").click()

    # 发宝箱  线上禁止
    # lucky_coindrop()
    # goal_coindrop()

    # 管理员与封禁
    broadcaster_manage()

    # 聊天
    if exists(Template("chat.png")):
        touch(Template("chat.png"))
        text("hello welcome to my broadcast")
        poco("com.cmcm.live:id/send_button").click()

    else:
        raise AssertionError("发消息失败")


# 管理员与封禁
def broadcaster_manage():
    # disable chat
    if poco("com.cmcm.live:id/level_head_icon").exists():
        poco("com.cmcm.live:id/level_head_icon").click()
        disablechat_name = poco("com.cmcm.live:id/tv").get_text()
        if poco("com.cmcm.live:id/id_dialog_anchor_manage").exists():
            poco("com.cmcm.live:id/id_dialog_anchor_manage").click()
            poco("com.cmcm.live:id/forbid_btn").click()
        poco("com.cmcm.live:id/arrow_button").click()
        touch(Template("manage.png"))
        sleep(3)
        if poco("com.cmcm.live:id/txt_name").get_text() == disablechat_name:
            poco("com.cmcm.live:id/txt_release").click()
            android.keyevent("back")
            sleep(3)

    else:
        log("disable chat failed cause no viewers")

    # admin
    if poco("com.cmcm.live:id/level_head_icon").exists():
        poco("com.cmcm.live:id/level_head_icon").click()
        sleep(5)
        admin_name = poco("com.cmcm.live:id/tv").get_text()
        if poco("com.cmcm.live:id/id_dialog_anchor_manage").exists():
            poco("com.cmcm.live:id/id_dialog_anchor_manage").click()
            poco("com.cmcm.live:id/admin_btn").click()
            poco("com.cmcm.live:id/arrow_button").click()
            touch(Template("manage.png"))
            poco("com.cmcm.live:id/txt_admin").click()
            sleep(3)
            if admin_name == poco("com.cmcm.live:id/txt_name").get_text():
                poco("com.cmcm.live:id/txt_release").click()
                android.keyevent("back")

    else:
        log("admin failed")

    # block
    if poco("com.cmcm.live:id/level_head_icon").exists():
        poco("com.cmcm.live:id/level_head_icon").click()
        block_name = poco("com.cmcm.live:id/tv").get_text()
        if poco("com.cmcm.live:id/id_dialog_anchor_manage").exists():
            poco("com.cmcm.live:id/id_dialog_anchor_manage").click()
            sleep(3)
            poco("com.cmcm.live:id/block_btn").click()
            sleep(3)
            if poco("com.cmcm.live:id/blockade_positive").exists():
                poco("com.cmcm.live:id/blockade_positive").click()
                sleep(3)
                if poco("com.cmcm.live:id/dialog_anchor_close").exists():
                    poco("com.cmcm.live:id/dialog_anchor_close").click()
                    poco("com.cmcm.live:id/arrow_button").click()
                    touch(Template("manage.png"))
                    sleep(3)
                    poco("com.cmcm.live:id/txt_black").click()
                    if block_name == poco("com.cmcm.live:id/txt_name").get_text():
                        poco("com.cmcm.live:id/txt_release").click()
                        sleep(3)
                    android.keyevent("back")

    else:
        log("block failed")


# 选择贴纸和美颜 前置条件：当前已唤出美颜框
def sticker():
    if poco("com.cmcm.live:id/sticker_filter_tabs").exists():
        # 选择美颜
        poco(name="android.widget.TextView")[0].click()
        poco("com.cmcm.live:id/seebar_beauty_buffing").click()
        poco("com.cmcm.live:id/seebar_beauty_white").click()
        poco("com.cmcm.live:id/seebar_beauty_eye").click()
        poco("com.cmcm.live:id/seebar_beauty_face").click()

        # 选择滤镜
        poco(name="android.widget.TextView")[1].click()
        # for i in range(2):
        #     poco("com.cmcm.live:id/sticker_bolder")[i].click()

        # 下载贴纸及选择
        poco(name="android.widget.TextView")[2].click()
        for j in range(8):
            if poco("com.cmcm.live:id/sticker_status_icon").exists():
                poco("com.cmcm.live:id/sticker_status_icon").click()
                sleep(6)
        for k in range(8):
            poco("com.cmcm.live:id/sticker_img")[k].click()
            sleep(5)
        poco("com.cmcm.live:id/sticker_img")[2].click()

    else:
        raise AssertionError("无美颜框 无法设置美颜及贴纸")


def lucky_coindrop(coins=300, number=10, desc=" "):
    uplive_page = UpLivePage()
    if not uplive_page.in_current_page():
        raise AssertionError("当前不在直播间，无法发送宝箱")
    if poco("com.cmcm.live:id/layout_bonus").exists():
        poco("com.cmcm.live:id/layout_bonus").click()
        sleep(2)
        assert poco("com.cmcm.live:id/bonus_title").exists(), "唤出选择宝箱弹窗成功"

        poco(name="android.widget.TextView")[0].click()
        poco("com.cmcm.live:id/et_gold_num").set_text(coins)
        sleep(2)
        poco("com.cmcm.live:id/et_bonus_num").set_text(number)
        sleep(2)
        poco("com.cmcm.live:id/et_bonus_desc").set_text(desc)
        sleep(2)
        poco("com.cmcm.live:id/tv_send_bonus").click()
        sleep(2)

        open_coindrop()

    else:
        raise AssertionError("无宝箱按钮无法发送")


# 任务宝箱
def goal_coindrop(gift_number=50, coin_number=300, bonus_number=10, desc=" "):
    uplive_page = UpLivePage()
    if not uplive_page.in_current_page():
        raise AssertionError("当前不在直播间，无法发送宝箱")

    if poco("com.cmcm.live:id/layout_bonus").exists():
        poco("com.cmcm.live:id/layout_bonus").click()
        sleep(2)
        poco(name="android.widget.TextView")[2].click()
        if poco("com.cmcm.live:id/bonus_winner1").exists():
            poco("com.cmcm.live:id/bonus_send").click()
            sleep(3)
        assert poco("com.cmcm.live:id/iv_gift_icon").exists(), "唤出选择宝箱弹窗成功"

        poco("com.cmcm.live:id/tv_gift_num").set_text(gift_number)
        poco("com.cmcm.live:id/et_gold_num").set_text(coin_number)
        poco("com.cmcm.live:id/et_bonus_num").set_text(bonus_number)
        poco("com.cmcm.live:id/et_bonus_desc").set_text(desc)
        poco("com.cmcm.live:id/iv_gift_icon").click()
        sleep(3)
        if poco("com.cmcm.live:id/gift_item").exists():
            poco("com.cmcm.live:id/gift_item").click()
            poco("com.cmcm.live:id/tv_send_bonus").click()
            sleep(5)
            assert poco("com.cmcm.live:id/iv_icon").exists(), "发出任务宝箱成功"
        else:
            raise AssertionError("未配置任务礼物")


# 抢宝箱
def open_coindrop():
    uplive_page = UpLivePage()
    if not uplive_page.in_current_page():
        raise AssertionError("当前不在直播间，无法发送宝箱")
    if poco("com.cmcm.live:id/gain_btn").exists():
        poco("com.cmcm.live:id/gain_btn").click()
        sleep(5)
        if poco("com.cmcm.live:id/bonus_close_btn").exists():
            poco("com.cmcm.live:id/bonus_close_btn").click()
            sleep(3)


# 启动app
restart_app()
login_if_needed()
sleep(2)
featurelist_popup_window()
sleep(3)
start_broadcasting()
assert_equal(1, 2)










