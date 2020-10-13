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
from common.popup.videoplayer import videoplayer_popup_handler

poco = AndroidUiautomationPoco()


def goto_talent():
    # 进入搜索页面
    poco('com.cmcm.live:id/home_search_img').click()
    sleep(60)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')
    if poco(text='Talent').exists():
        poco(text='Talent').click()
        sleep(30)
        title_name = poco('android.widget.TextView').get_text()
        assert_equal(title_name, 'Talents', '进入talents页面')
        # 浏览直播视频
        for i in range(2):
            poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
            sleep(20)
            snapshot(msg='滑动页面看更多直播视频')
        # 选择一个视频进入
        poco('android.widget.ImageView')[2].click()
        sleep(120)
        # 调用view_live()
        view_live()
        assert poco('com.cmcm.live:id/gender_title').exists(), '回到girls页面'
        poco('com.cmcm.live:id/gender_video_back').click()
        assert poco('com.cmcm.live:id/search_content').exists(), '回到搜索页面'
    else:
        raise TabError('没有找到对应的girls tab')


@videoplayer_popup_handler
def view_live():
    if poco(text='Follow and get notified when the broadcast starts').exists():
        poco(text='Follow and get notified when the broadcast starts').click()
        sleep(2)
    assert poco('com.cmcm.live:id/anchor_nickname').exists(), '进入直播播放页面成功'
    # 进入视频
    for i in range(5):
        name_before = poco('com.cmcm.live:id/anchor_nickname').get_text()
        poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
        sleep(120)
        name_now = poco('com.cmcm.live:id/anchor_nickname').get_text()
        assert_not_equal(name_before, name_now, '切换直播成功')
        snapshot(msg='直播播放页面')
    poco('com.cmcm.live:id/img_close').click()
    if poco(text='Swipe up to the next broadcast').exists():
        poco.click([0.5, 0.5])
        sleep(2)
        poco('com.cmcm.live:id/img_close').click()


restart_app()
login_if_needed()
goto_talent()
