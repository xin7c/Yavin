# -*- encoding=utf8 -*-
from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class OtherBasePage(BasePage):

    MORE_MENU = "com.cmcm.live:id/img_menu"

    def in_current_page(self):
        if poco(self.MORE_MENU).exists():
            return True
        else:
            return False

    def click_more_menu(self):
        poco(self.MORE_MENU).click()

