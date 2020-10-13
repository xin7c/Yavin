# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-09 19:07
# file: HomePage.py
# IDE: PyCharm

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.pages.BasePage import BasePage


class HomePage(BasePage):
    """
    逻辑层
    """
    def goto_prepare_live_page(self):
        """
        点击开播按钮进入准备直播页面
        :return:
        """
        self.find_click(self.page_ele_loc("ID_UPLIVE"))
        sleep(5)
        return self
    
    def goto_message_page(self):
        """
        从homepage页面点击私信按钮进入message页面
        :return:
        """
        self.find_click(self.page_ele_loc("ID_TAB_MESSAGE"))
        sleep(5)
        return self
    
    def goto_me_page(self):
        """
        从homepage页面进入个人中心页面
        :return:
        """
        self.find_click(self.page_ele_loc("ID_ME_PAGE"))
        sleep(5)
        return self
    
    def goto_follow_page(self):
        """
        从homepage页面进入Follow页面
        :return:
        """
        self.find_click(self.page_ele_loc("ID_HOME_TAB_FOLLOW"))
        sleep(5)
        return self
        
    def goto_home_page(self):
        """
        回到主页面
        :return:
        """
        self.find_click(self.page_ele_loc("ID_HOME_PAGE"))
        sleep(5)
        return self
    
    def goto_new_page(self):
        """
        进入New页面
        :return:
        """
        self.find_text(self.page_ele_loc("TEXT_NEW"))
        sleep(5)
        return self


if __name__ == '__main__':
    print(HomePage().cls_name)
    sp = HomePage()
    # sp.goto_setting_page()
    print(sp.goto_home_page())
    # sp.goto_network_ping()
    # sp.click1("lalala")
    print(sp.screen_size)