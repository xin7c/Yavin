# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入搜索页面trending tab页面'''
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from common.popup.videoplayer import videoplayer_popup_handler

poco = AndroidUiautomationPoco()


def trending():
    # 进入搜索页面
    poco('com.cmcm.live:id/home_search_img').click()
    sleep(60)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')
    滑动trending列表
    if poco('com.cmcm.live:id/recycler_view').exists():
        poco('com.cmcm.live:id/recycler_view').scroll('horizontal')
    snapshot(msg='滑动trending列表')
    
    
trending()
