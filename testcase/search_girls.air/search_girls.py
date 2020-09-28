# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入首页各个girls页面'''

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from common.live_related.view_live import *
from common.pages.SearchPage import *
from common.pages.SecondaryGamePage import *
from common.pages.LiveViewPage import *
from common.pages.SecondaryGirlsPage import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from airtest.core.api import *
from poco.drivers.android.uiautomation import *

poco = AndroidUiautomationPoco()


def goto_girls():
    # 进入搜索页面
    search_page = SearchPage()
    search_page.goto_this()
    if not search_page.in_current_page():
        raise AssertionError("进入搜索页失败")
    if not search_page.is_girls_tab_exists():
        raise AssertionError("没有找到对应的girls tab")
    # 进入女神页面
    poco(text=SearchPage.GIRLS_TEXT).click()
    sleep(30)
    assert_equal(poco(SecondaryGirlsPage.GIRLS_TAB_ID).get_text(), search_page.GIRLS_TEXT, msg='进入girls页面失败')
    # 滑动查看跟多视频
    while SecondaryGamePage().loading_status():
        poco.swipe([0.5, 0.7], [0.5, 0.1], duration=0.2)
        snapshot(msg='向下滑动视频')
        if not SecondaryGirlsPage().is_load_more_icon_exists():
            print('开始滑动')
            continue
        else:
            print('结束滑动')
            sleep(2)
            break
    print('循环结束')
    # 向上滑动
    sleep(3)
    for i in range(3):
        print('向上滑动')
        poco.swipe([0.5, 0.2], [0.5, 0.7], duration=0.2)
        print('滑动')
    # 观看直播
    SecondaryGirlsPage().go_view_live()
    sleep(120)
    assert_equal(poco(LiveViewPage().LIVE_GIFT_BTN).exists(), True, msg='进入直播间失败')
    # 调用view_more_live()观看直播
    view_more_live()
    # 关闭直播
    close_live()
    assert_equal(poco(SecondaryGirlsPage().GIRLS_TAB_ID).exists(), True, '返回到Girls列表失败')
    # 点击返回按按钮返回到搜索页面
    poco(SecondaryGirlsPage().GIRLS_BACK_ICON_ID).click()
    assert_equal(poco(SearchPage().SEARCH_CONTENT_TAB).exists(), True, msg='回到搜索页面失败')


restart_app()
login_if_needed()
goto_girls()
