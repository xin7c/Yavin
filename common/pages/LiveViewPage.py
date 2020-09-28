# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class LiveViewPage(BasePage):
    # 游戏直播页面横竖屏切换btn
    GAME_SCREEN_SWITCH_BTN = 'com.cmcm.live:id/screen_switch_btn'
    LIVE_GIFT_BTN = 'com.cmcm.live:id/gift_icon'
