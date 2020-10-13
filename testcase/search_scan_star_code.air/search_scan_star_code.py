# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入搜索页面点击进入二维码页面'''

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

poco = AndroidUiautomationPoco()


def star_code():
    # 进入搜索页面
    poco('com.cmcm.live:id/home_search_img').click()
    sleep(5)
    assert poco('com.cmcm.live:id/search_content').exists(), '进入搜索页面失败'
    snapshot(msg='成功进入搜索页面')
    poco('com.cmcm.live:id/search_content').click()
    sleep(2)
    assert poco(text='Scan Star Code').exists(), '没有出现二维码入口'
    poco(text='Scan Star Code').click()
    sleep(2)
    assert poco(text='Align the star code within the frame to scan').exists(), '进入二维码页面失败'
    sleep(5)
    # 返回到搜索页面
    poco('com.cmcm.live:id/qr_act_back').click()
    sleep(2)
    poco('com.cmcm.live:id/search_cancel').click()
    sleep(5)
    assert poco('com.cmcm.live:id/search_back').exists(), '成功回退到搜索页面'
    sleep(2)
    poco('com.cmcm.live:id/search_back').click()

    snapshot(msg='回到首页')
    
    
restart_app()
login_if_needed()
star_code()
