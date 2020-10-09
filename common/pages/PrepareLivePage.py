# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-09 18:42
# file: PrepareLivePage.py
# IDE: PyCharm

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.pages.BasePage import BasePage


class PrepareLivePage(BasePage):
    """
    逻辑层
    """
    def in_current_page(self):
        """
        检测准备直播按钮是否存在来判断是否在准备直播页面
        :return:
        """
        return self.poco(self.page_ele_loc("ID_START_LIVE")).exists() or False
    
    def click_live_title(self):
        """
        点击直播标题，并删除默认的标题内容
        :return:
        """
        self.find_click(self.page_ele_loc("ID_LIVE_TITLE"))
        sleep(2)
        
        
        


if __name__ == '__main__':
    print(PrepareLivePage().cls_name)
    sp = PrepareLivePage()
    # sp.goto_setting_page()
    print(sp.editor_live_title())
    # sp.goto_network_ping()
    # sp.click1("lalala")
    print(sp.screen_size)
