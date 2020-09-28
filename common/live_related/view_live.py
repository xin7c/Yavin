# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

'''直播间内上下滑动切换直播间，并去除弹窗，然后点击关闭按钮关闭直播'''

import sys
from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.popup.videoplayer import videoplayer_popup_handler
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
poco = AndroidUiautomationPoco()


@videoplayer_popup_handler
def view_more_live():
    if poco(text='Follow and get notified when the broadcast starts').exists():
        poco(text='Follow and get notified when the broadcast starts').click()
        sleep(2)
    assert poco('com.cmcm.live:id/anchor_nickname').exists(), '进入直播播放页面成功'
    # 进入视频
    for i in range(5):
        name_before = poco('com.cmcm.live:id/anchor_nickname').get_text()
        poco.swipe([0.5, 0.58], [0.5, 0.1], duration=0.3)
        sleep(120)
        # 判断直播是否结束
        if poco('com.cmcm.live:id/txt_lucky').exists():
            name_now = poco('com.cmcm.live:id/live_end_user_name_tv').get_text()
        else:
            name_now = poco('com.cmcm.live:id/anchor_nickname').get_text()
        assert_not_equal(name_before, name_now, '切换直播成功')
        snapshot(msg='直播播放页面')


@videoplayer_popup_handler
def view_one_live():
    if poco(text='Follow and get notified when the broadcast starts').exists():
        poco(text='Follow and get notified when the broadcast starts').click()
        sleep(2)
    assert poco('com.cmcm.live:id/anchor_nickname').exists(), '进入直播播放页面成功'
    sleep(120)


def close_live():
    poco("com.cmcm.live:id/img_close").click()
    sleep(2)
    # 首次关闭直播引导手势
    if poco(text='Swipe up to the next broadcast').exists():
        poco.click([0.5, 0.5])
        sleep(2)
        poco('com.cmcm.live:id/img_close').click()
    if poco('com.cmcm.live:id/button1').exists():
        poco('com.cmcm.live:id/button1').click()
        sleep(1)
    snapshot(msg='关闭直播')