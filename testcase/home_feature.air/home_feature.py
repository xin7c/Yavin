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


def scan_feature():
    sleep(20)
    HomePage().goto_feature()
    # 滑动查看跟多视频
    HomePage().scroll_page()
    # 观看直播
    HomePage().home_goto_live()
    sleep(120)
    assert_equal(poco(LiveViewPage().LIVE_GIFT_BTN).exists(), True, msg='进入直播间失败')
    # 调用view_more_live()观看直播
    view_more_live()
    # 关闭直播
    close_live()
    

restart_app()
login_if_needed()
scan_feature()