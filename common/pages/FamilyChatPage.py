# -*- encoding=utf8 -*-
from airtest.core.api import sleep

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class FamilyChatPage(BasePage):
    """
    家族的聊天页面。有别于群组聊天页面（GroupChatPage），虽然他们二者的 activity 是一样的。
    """

    FAMILY_CHAT_PAGE_ACTIVITY_NAME = "com.cmcm.live/com.cmcm.letter.view.chat.LetterChatAct"
    # 家族设置按钮
    WIDGET_SETUP = "com.cmcm.live:id/letter_chat_group_setup"
    #上麦按钮
    WIDGET_HEAD_ICON = "com.cmcm.live:id/vcall_small_mask_head_icon"

    #检查是否在家族页面
    def in_current_page(self):
        if current_activity() == self.FAMILY_CHAT_PAGE_ACTIVITY_NAME and \
                poco(self.WIDGET_HEAD_ICON).exists():
            return True
        else:
            return False

    #进入设置页
    def click_setup(self):
        poco(self.WIDGET_SETUP).click()
        time.sleep(5)
