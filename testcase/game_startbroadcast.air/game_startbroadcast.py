# -*- encoding=utf8 -*-
__author__ = "liyue"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.app.app_control import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.login.login import login_if_needed
from common.popup.featurelist_popup import *
from airtest.core.android import Android
from common.pages.SearchPage import *
from common.pages.UpLivePage import *
from common.pages.HomePage_old import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
android = Android()


def game_startbroadcast():
    search_page = SearchPage()
    uplive_page = UpLivePage()
    home_page = HomePage()

    if not home_page.in_current_page():
        raise AssertionError('当前不在首页')
    poco(home_page.SEARCH_BUTTON).click()
    sleep(5)
    if not search_page.in_current_page():
        raise AssertionError('当前不在搜索页，无法进入游戏')
    if exists(Template("game_button.png")):
        touch(Template("game_button.png"))
        sleep(2)
        if poco("com.cmcm.live:id/iv_game_live").exists():
            poco("com.cmcm.live:id/iv_game_live").click()
            if not uplive_page.in_current_page():
                raise AssertionError("当前无法进入准备直播页")
            uplive_page.click_start_uplive()
            if not uplive_page.in_current_page():
                raise AssertionError('当前不在直播间')
            if poco("com.cmcm.live:id/btn_no_reminder").exists():
                poco("com.cmcm.live:id/iv_tip_close").click()
                uplive_page.click_start_uplive()
                sleep(2)
            if poco("com.cmcm.live:id/topic_title").exists():
                poco("com.cmcm.live:id/tag_txt").click()
                uplive_page.click_start_uplive()

            # 检查系统弹窗
            if poco("android:id/message").exists():
                poco("android:id/button1").click()
                sleep(2)
            sleep(5)
            assert_equal(poco("com.cmcm.live:id/img_close").exists(), True, msg="开播失败")

            sleep(20)
            poco("com.cmcm.live:id/img_close").click()
            poco("com.cmcm.live:id/button1").click()
            sleep(2)
            poco("com.cmcm.live:id/img_close").click()


        else:
            raise AssertionError("无游戏button无法开播")

    else:
        raise AssertionError("游戏button不展示，无法进入游戏")


restart_app()
login_if_needed()
sleep(2)
game_startbroadcast()












