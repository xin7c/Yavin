# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *

poco = AndroidUiautomationPoco()


class SecondaryGirlsPage(BasePage):
    GIRLS_TAB_ID = 'com.cmcm.live:id/gender_title'
    GIRLS_BACK_ICON_ID = 'com.cmcm.live:id/iv_back'
    GIRLS_TAB_TEXT = 'Girls'
    GIRLS_LIVE_NAME = 'android.widget.ImageView'
    GIRLS_REFRESH_LOADING_MORE_ID = 'com.cmcm.live: id/img_load_more'
    GIRLS_REFRESH_END_ID = 'com.cmcm.live:id/txt_loading_state'
    GUYS_TAB_TEXT = 'Boys'
    
    def in_current_page(self):
        if poco(self.GIRLS_TAB_ID).get_text() == self.GIRLS_TAB_TEXT:
            return True
        else:
            return False
    
    def is_load_more_icon_exists(self):
        if poco(self.GIRLS_REFRESH_LOADING_MORE_ID).child(self.GIRLS_REFRESH_END_ID).exists():
            return True
        else:
            return False
    
    def go_view_live(self):
        if len(poco(self.GIRLS_LIVE_NAME)) <= 0:
            raise AssertionError('girls页面没有找到直播')
        poco(name=self.GIRLS_LIVE_NAME)[0].click()
