# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from common.pages.HomePage_old import *
from common.pages.SearchPage import *
from common.pages.SecondaryGirlsPage import *
from common.pages.LiveViewPage import *
from common.live_related.view_live import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import *

from common.app.app_control import restart_app
from common.login.login import login_if_needed

poco = AndroidUiautomationPoco()


def scan_home():
    sleep(20)
    HomePage().goto_feature()
    sleep(2)
    assert_exists(Template("homepage_feature.png"), msg="定位到了Feature_tab页面")
    HomePage().goto_new()
    sleep(2)
    assert_exists(Template("homepage_new.png"), msg="定位到了new_tab页面")
    HomePage().goto_game()
    sleep(2)
    assert_exists(Template("homepage_game.png"), msg="定位到了game_tab页面")
    HomePage().goto_nearby()
    sleep(2)
    assert_exists(Template("homepage_nearby.png"), msg="定位到了nearby_tab页面")
    sleep(2)
    HomePage().goto_ranking_board()
    sleep(2)
    assert_exists(Template("homepage_ranking_board.png"), msg="定位到了ranking_board_tab页面")
    HomePage().goto_world()
    sleep(2)
    HomePage().goto_videos()
    sleep(2)
    assert_exists(poco('com.cmcm.live:id/like_count_tv').exists(), msg='进入videos页面失败')
    
    
restart_app()
login_if_needed()
scan_home()
