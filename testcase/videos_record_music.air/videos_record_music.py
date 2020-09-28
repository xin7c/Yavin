# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入首页各个tab页面'''
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

poco = AndroidUiautomationPoco()


def videos_scan():
    # 进入搜索页面
    poco('com.cmcm.live:id/home_search_img').click()
    sleep(20)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')
    poco(text='Videos').click()
    sleep(20)
    assert poco('com.cmcm.live:id/video_record').exists(), '没有进入到video页面'
    snapshot(msg='成功进入videos页面')
    poco('com.cmcm.live:id/video_record').click()
    # 开播系统相机权限
    allow_windows = poco('com.android.packageinstaller:id/permission_allow_button')
    for i in range(4):
        if allow_windows:
            allow_windows.click()
            sleep(2)
        else:
            break
    assert poco('com.cmcm.live:id/img_record').exists()
    snapshot(msg='进入videos录制页面')
    # 选则音乐
    poco('com.cmcm.live:id/view_bgm').click()
    sleep(20)
    assert poco(text='Music').exists(), '进入音乐列表'
    for i in range(3):
        poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
        sleep(5)
    poco('com.cmcm.live:id/name').click()
    poco('com.cmcm.live:id/music_user_button').wait(20)
    assert poco('com.cmcm.live:id/music_user_button').exists(), '播放音乐成功'
    poco('com.cmcm.live:id/music_user_button').click()
    sleep(10)
    assert poco('com.cmcm.live:id/music_circle').exists(), '选中背景音乐失败'


restart_app()
videos_scan()
login_if_needed()