# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-10 17:49
# file: LivePage.py
# IDE: PyCharm

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.pages.BasePage import BasePage


class LivePage(BasePage):
    """
    逻辑层
    """
    def in_current_page(self):
        """
        直播数据按钮存在，证明开播成功
        :return:
        """
        return self.poco(self.page_ele_loc("ID_BTN_LIVE_DETAIL_DATA")).exists() or False
    
    def close_live(self):
        """
        点击关闭按钮
        :return:
        """
        self.find_click(self.page_ele_loc("ID_IMG_CLOSE"))
        return self
    
    def close_live_guide_is_exist(self):
        """
        判断关闭直播引导是否存在，返回True or False
        :return:返回bool类型
        """
        return self.poco(self.page_ele_loc("ID_IMG_CLOSE")).exists() or False
    
    def close_live_guide(self):
        """
        关闭首次关闭直播时弹出的关闭直播引导动画，点击任意地方动画消失
        :return:
        """
        self.poco.click([500 / self.screen_size[0], 500 / self.screen_size[1]])
        return self
    
    def close_live_confirm_popup_exist(self):
        """
        关闭直播确认弹窗如果存在，返回True，不存在返回False
        :return:
        """
        return self.poco(self.page_ele_loc("ID_BUTTON1")).exists() or False
    
    def close_live_finish(self):
        """
        主播关闭直播时，二次弹窗点击Finish关闭直播
        :return:
        """
        self.find_click(self.page_ele_loc("ID_BUTTON1"))
        return self
    
    def close_live_continue(self):
        """
        主播关闭直播时，点击continue继续直播
        :return:
        """
        self.find_click(self.page_ele_loc("ID_BUTTON2"))
        return self
    
    def close_live_anchor(self):
        """
        关闭直播，判断关闭直播引导是否存在，存在把引导关闭，判断关闭直播时二次确认弹窗是否存在
        :return:
        """
        self.find_click(self.page_ele_loc("ID_IMG_CLOSE"))
        sleep(2)
        # 关闭直播引导动画是否存在
        if self.close_live_guide_is_exist():
            self.close_live_guide()
            sleep(2)
        # 关闭直播时是否弹出了二次确认弹窗
        if self.close_live_confirm_popup_exist():
            self.close_live_finish()
            sleep(3)
        # 点击直播结束页面关闭按钮
        self.find_click(self.page_ele_loc("ID_IMG_CLOSE"))
        assert_equal(self.in_current_page(), False, "直播关闭成功")
        return self
