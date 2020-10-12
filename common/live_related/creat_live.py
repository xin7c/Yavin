# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

'''直播间内上下滑动切换直播间，并去除弹窗，然后点击关闭按钮关闭直播'''

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.pages.BasePage import BasePage

class AnchorPage(BasePage):

    def start_broadcast(self):
        """
        开普通直播
        """
        self.poco(self.page_ele_loc("ID_UPLIVE")).click()
        self.poco(self.page_ele_loc("ID_TXT_VIDEO_START_LIVE")).click()

    def close_broadcast(self):
        """
        关播
        """
        self.poco("com.cmcm.live:id/img_close").click()
        self.poco("com.cmcm.live:id/button1").click()


if __name__ == '__main__':
    print(AnchorPage().cls_name)
    obj = AnchorPage()
    obj.restart_app()

    obj.start_broadcast()
    sleep(30)
    obj.close_broadcast()

