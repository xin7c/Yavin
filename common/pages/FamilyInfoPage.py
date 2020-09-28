# -*- encoding=utf8 -*-
from airtest.core.api import sleep

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class FamilyInfoPage(BasePage):
    """
    家族信息页面。有别于群组信息页面(GroupInfoPage).
    虽然这两个页面的 activity 是一样的，但细节上有区别，业务上也代表不同的页面
    """

    GROUP_INFO_PAGE_ACTIVITY_NAME = 'com.cmcm.live/com.cmcm.letter.view.activity.GroupInfoActivity'
    # fixme: 多语言兼容问题
    TEXT_SETUP_KINGDOM_EVENT = "Set up Kingdom event"

    WIDGET_FAMILY_NAME = "com.cmcm.live:id/txt_fam_name"

    # 已佩戴的徽章上的文字，即家族名
    WIDGET_WORN_CREST = "com.cmcm.live:id/txt_member_main_name"
    # 佩戴徽章的文字，点击可以佩戴徽章
    WIDGET_WEAR_CREST = "com.cmcm.live:id/txt_info_setmain"

    def in_current_page(self):
        if current_activity() == self.GROUP_INFO_PAGE_ACTIVITY_NAME and \
                poco(text=self.TEXT_SETUP_KINGDOM_EVENT).exists():
            return True
        else:
            return False

    def get_family_name(self):
        return poco(self.WIDGET_FAMILY_NAME).get_text()

    def click_wear_crest(self):
        poco.swipe([0.5, 0.9], [0.5, 0.2])
        time.sleep(1)
        poco(self.WIDGET_WEAR_CREST).click()
        sleep(0.5)
        # 确认佩戴的弹窗
        if poco('com.cmcm.live:id/scrollView').exists():
            if poco("com.cmcm.live:id/button1").exists():
                poco("com.cmcm.live:id/button1").click()
            else:
                poco("com.cmcm.live:id/button2").click()
                sleep(3)
        sleep(8)
        poco.swipe([0.5, 0.2], [0.5, 0.9])

    def get_worn_crest_name(self):
        """
        :return: 如果已经佩戴了徽章，则返回徽章的名字；否则返回 None
        """
        poco.swipe([0.5, 0.9], [0.5, 0.2])
        time.sleep(1)
        if poco(self.WIDGET_WORN_CREST).exists():
            poco.swipe([0.5, 0.2], [0.5, 0.9])
            return poco(self.WIDGET_WORN_CREST).get_text()
        else:
            poco.swipe([0.5, 0.2], [0.5, 0.9])
            return None
