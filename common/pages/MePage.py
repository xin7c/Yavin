# -*- encoding=utf8 -*-

from common.pages.BasePage import BasePage
from common.app.get_current_activity import *
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class MePage(BasePage):

    WIDGET_PERSONAL_QR = "com.cmcm.live:id/personal_qr"
    WIDGET_USER_NAME = "com.cmcm.live:id/tv"

    def in_current_page(self):
        if poco(self.WIDGET_PERSONAL_QR).exists():
            return True
        else:
            return False

    def get_user_name(self):
        user_name = poco(self.WIDGET_USER_NAME).get_text()
        return user_name

    def click_my_fam(self):
        while not poco(text='My FAM').exists():
            # fixme：swipe 这个幅度一定能出现"我的家族"吗？不同手机swipe速度不一样吧？
            poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.2)
            time.sleep(2)
        # fixme：语言兼容性
        poco(text='My FAM').click()
        time.sleep(10)

    def click_replay_button(self):
        while not poco(text='Replay').exists():
            poco.swipe([0.5, 0.6], [0.5, 0.1], duration=0.1)
            time.sleep(2)
        poco(text='Replay').click()
        time.sleep(5)

    def click_Store_button(self):
        while not poco(text='Store').exists():
            poco.swipe([0.5, 0.6], [0.5, 0.1], duration=0.1)
            time.sleep(2)
        poco(text='Store').click()
        time.sleep(5)
