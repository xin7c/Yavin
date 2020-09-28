# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入搜索页面点击顶部进入game页面，浏览并观看直播'''

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from common.live_related.view_live import *
from common.pages.SearchPage import *
from common.pages.SecondaryGamePage import *
from common.pages.LiveViewPage import *
from airtest.core.api import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed


def goto_game():
    search_page = SearchPage()
    search_page.goto_this()
    if not search_page.in_current_page():
        raise AssertionError("进入搜索页面失败")
    if not search_page.is_game_tab_exists():
        raise AssertionError("搜索页面没有找到Game入口")
    secondary_game_page = SecondaryGamePage()
    # 进入game二级界面
    search_page.goto_game()
    assert_equal(poco(secondary_game_page.GAME_GO_LIVE_iCON).exists(), True, '进入二级游戏tab页面失败')
    game_type_list = secondary_game_page.obtain_all_game_tab()
    if len(game_type_list) <= 0:
        raise AssertionError('游戏页面么有游戏标签tab')
    for i in range(len(game_type_list)):
        poco(text=game_type_list[i]).click()
        snapshot(msg='进入到%s页面' % game_type_list[i])
        sleep(2)
        while secondary_game_page.loading_status():
            poco.swipe([0.5, 0.7], [0.5, 0.1], duration=0.2)
            snapshot(msg='向下滑动视频')
            sleep(20)
        assert_equal(poco(secondary_game_page.GAME_TYPE)[i].get_text(), game_type_list[i], '切换游戏tab失败')
        if not secondary_game_page.is_game_live_exists():
            raise AssertionError('该%s tab页面没有游戏直播' % game_type_list[i])
        secondary_game_page.goto_game_live()
        sleep(30)
        assert_equal(poco(LiveViewPage.GAME_SCREEN_SWITCH_BTN).exists(), True, msg='游戏直播页面进入失败')
        # 切换直播间是否成功
        view_more_live()
        # 关闭直播间
        close_live()
        assert_equal(poco(SecondaryGamePage.GAME_GO_LIVE_iCON).exists(), True, msg='关闭游戏直播失败，没有回退到游戏页面')
        

restart_app()
login_if_needed()
goto_game()


