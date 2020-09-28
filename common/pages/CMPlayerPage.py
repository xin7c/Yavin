# -*- encoding=utf8 -*-
from airtest.core.api import sleep

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class CMplayerPage(BasePage):
    CMplayer_PAGE_ACTIVITY_NAME = 'com.cmcm.live/com.cmcm.cmlive.activity.fragment.CMVideoPlayerActivity'

    def in_current_page(self):
        if current_activity() == self.CMplayer_PAGE_ACTIVITY_NAME:
            return True
        else:
            return False
