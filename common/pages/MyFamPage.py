# -*- encoding=utf8 -*-
from airtest.core.api import sleep

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class MyFamPage(BasePage):

    MYFAM_PAGE_ACTIVITY_NAME = 'com.cmcm.live/com.cmcm.letter.view.chat.MyFamAct'

    WIDGET_MY_FAM_LIST_ITEM = "com.cmcm.live:id/my_fam_list_item_my_group_root"

    def in_current_page(self):
        if current_activity() == self.MYFAM_PAGE_ACTIVITY_NAME:
            return True
        else:
            return False

    def get_my_fam_list(self):
        return poco(self.WIDGET_MY_FAM_LIST_ITEM)

    def click_my_first_fam(self):
        fam_list = self.get_my_fam_list()
        if len(fam_list) <= 0:
            raise AssertionError("试图点击家族，但该用户没有加入任何家族")
        else:
            fam_list[0].click()
            sleep(1)
            if poco('com.android.packageinstaller:id/permission_allow_button').exists():
                poco('com.android.packageinstaller:id/permission_allow_button').click()
            sleep(3)

