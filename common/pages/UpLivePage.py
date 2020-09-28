# -*- encoding=utf8 -*-
from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class UpLivePage(BasePage):

    UP_LIVE_PAGE_ACTIVITY_NAME = 'com.cmcm.live/com.cmcm.cmlive.activity.UpLiveActivity'

    def in_current_page(self):
        if current_activity() == self.UP_LIVE_PAGE_ACTIVITY_NAME:
            return True
        else:
            return False

    def click_start_uplive(self):
        poco("com.cmcm.live:id/txt_video_start_live").click()
