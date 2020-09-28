# -*- encoding=utf8 -*-
from airtest.core.api import sleep

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()

class FamilyTaskPage(BasePage):
    Kingdom_Task = 'com.cmcm.live:id/iv_kingdom_task'

    def in_current_page(self):
        if poco(self.Kingdom_Task).exists():
        # 由于线上安卓H5页面打不开，无法确定页面元素
            poco(self.Kingdom_Task).click()
            return True
        else:
            return False

