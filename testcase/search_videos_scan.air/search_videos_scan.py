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
    sleep(30)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')
    if poco(text='Videos').exists():
        poco(text='Videos').click()
        sleep(30)
        assert poco('com.cmcm.live:id/video_record').exists(), '没有进入到video页面'
        snapshot(msg='成功进入videos页面')
        # 浏览短视频
        for i in range(10):
            poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
            assert poco('com.cmcm.live:id/video_record').exists(), '没在video页面滑动'
        # 选择一个视频进入
        poco('com.cmcm.live:id/short_video_cover_img')[2].click()
        sleep(120)
        assert poco('com.cmcm.live:id/anchor_nickname').exists(), '进入videos播放页面成功'
        # 切换视频
        for i in range(5):
            name_before = poco('com.cmcm.live:id/anchor_nickname').get_text()
            poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
            sleep(120)
            name_now = poco('com.cmcm.live:id/anchor_nickname').get_text()
            assert_not_equal(name_before, name_now, '切换videos成功')
            snapshot(msg='切换短视频')
            snapshot(msg='videos播放页面')
        poco('com.cmcm.live:id/img_close').click()
        assert poco('com.cmcm.live:id/video_record').exists(), '回到video页面'
        poco('com.cmcm.live:id/img_left').click()
        assert poco('com.cmcm.live:id/search_content').exists(), '回到搜索页面'
    else:
        raise TabError('没有找到对应的videos tab')


restart_app()
login_if_needed()
videos_scan()
