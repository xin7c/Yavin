# -*- encoding=utf8 -*-
from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class ReplayPage(BasePage):
    WIDGET_TEXT_REPLAY = 'com.cmcm.live:id/shine_act_custom_title_tv'
    WIDGET_REPLAY_LIST_ITEM = 'com.cmcm.live:id/layout_item_live_record'
    WIDGET_WATCH_ITEM = ("com.cmcm.live:id/img_watch_loading_floor")

    def in_current_page(self):
        if poco(self.WIDGET_TEXT_REPLAY).exists():
            return True
        else:
            return False

    def click_first_replay(self):
        t = poco("com.cmcm.live:id/list_live_record").offspring("android:id/list").child(
            "android.widget.LinearLayout")
        if len(t) <= 0:
            raise AssertionError("进入第一个视频失败")
        t[1].click()

    # def in_watch_replay_page(self):
    #     if poco(self.WIDGET_REPLAY_LIST_ITEM).exists():
    #         return True
    #     else:
    #         return False



