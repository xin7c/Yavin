# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入首页各个tab页面'''

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
poco = AndroidUiautomationPoco()


def goto_guys():
    # 进入搜索页面
    search_page = SearchPage()
    search_page.goto_this()
    if not search_page.in_current_page():
        raise AssertionError("进入搜索页失败")
    if not search_page.is_girls_tab_exists():
        raise AssertionError("没有找到对应的girls tab")
    # 进入男神页面
    poco(text=SearchPage.GUYS_NAME).click()
    sleep(30)
    assert_equal(poco(SecondaryGirlsPage().GIRLS_TAB_ID).get_text(),
                 SecondaryGirlsPage().GUYS_TAB_TEXT, msg='进入guys页面失败')
    # 滑动查看跟多视频
    while SecondaryGamePage().loading_status():
        poco.swipe([0.5, 0.7], [0.5, 0.1], duration=0.2)
        snapshot(msg='向下滑动视频')
        if not SecondaryGirlsPage().is_load_more_icon_exists():
            continue
        else:
            break
    # 向上滑动
    for i in range(3):
        poco.swipe([0.5, 0.1], [0.5, 0.7], duration=0.2)
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
goto_guys()
