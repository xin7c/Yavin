# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入搜索页面点击顶部进入game页面，开游戏直播'''

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

# from common.popup.videoplayer import videoplayer_dialog_check

poco = AndroidUiautomationPoco()


def goto_search_page():
    # 进入搜索页面
    poco('com.cmcm.live:id/home_search_img').click()
    sleep(20)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')


def go_live_game():
    goto_search_page()
    if poco(name='com.cmcm.live:id/tag_desc', text='Game').exists():
        poco(name='com.cmcm.live:id/tag_desc', text='Game').click()
        sleep(5)
        assert poco('com.cmcm.live:id/iv_game_live').exists(), '进入game二级页面失败'
        poco('com.cmcm.live:id/iv_game_live').click()
        sleep(2)
        # 开播系统相机权限
        allow_windows = poco('com.android.packageinstaller:id/permission_allow_button')
        for i in range(4):
            if allow_windows:
                allow_windows.click()
                sleep(2)
            else:
                break
        assert poco('com.cmcm.live:id/txt_video_start_live').exists(), '进入游戏准备直播页面'
        if poco('com.cmcm.live:id/edt_video_title').get_text() != poco('com.cmcm.live:id/topic_arrow').get_text():
            poco('com.cmcm.live:id/topic_arrow').click()
            sleep(2)
            assert poco('com.cmcm.live:id/topic_title').exists(), '进入游戏直播topic页面'
            # 选择第一个游戏标签
            select_tag = poco('com.cmcm.live:id/tag_txt')[0].get_text()
            poco('com.cmcm.live:id/tag_txt')[0].click()
            sleep(2)
            show_tag = poco('com.cmcm.live:id/topic_arrow').get_text()
            assert_equal(select_tag, show_tag, '游戏标签选中')
            snapshot(msg='游戏开播横屏')
        # 横屏开播
        poco('com.cmcm.live:id/txt_video_start_live').click()
        sleep(2)
        if poco('com.cmcm.live:id/btn_no_reminder').exists():
            poco('com.cmcm.live:id/btn_no_reminder').click()
            sleep(2)
            poco('com.cmcm.live:id/txt_video_start_live').click()
            
        # 弹窗引导LiveMe will start capturing everything that's displayed on your screen.
        if poco('com.android.systemui:id/remember').exists():
            poco('com.android.systemui:id/remember').click()
            sleep(2)
            poco('android:id/button1').click()
        assert poco('com.cmcm.live:id/anchor_nickname').exists(), '游戏开播成功'
        sleep(300)
        assert poco('com.cmcm.live:id/anchor_nickname').exists(), '游戏直播仍在继续'
        # 关闭直播
        poco('com.cmcm.live:id/img_close').click()
        sleep(2)
    else:
        raise AssertionError("搜索页面没有扎到game入口")


restart_app()
login_if_needed()
go_live_game()
