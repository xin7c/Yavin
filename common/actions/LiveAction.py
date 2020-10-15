# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-15 11:19
# file: LiveAction.py.py
# IDE: PyCharm

from common.pages.BasePage import BasePage
from common.pages.HomePage import HomePage
from common.pages.PrepareLivePage import PrepareLivePage
from common.pages.LivePage import LivePage
from airtest.core.api import sleep, assert_equal


class LiveAction(BasePage):
    home_page = HomePage()
    pre_live_page = PrepareLivePage()
    live_page = LivePage()
    
    def go_pre_live_page_and_set_title(self):
        """
        去准备直播页面名并设置直播标题
        :return:
        """
        # 判断首页开播按钮是否存在
        assert_equal(self.home_page.up_live_icon_is_exists(), True, "home页开播按钮不存在")
        # 点击直播按钮进入准备直播页面
        self.home_page.goto_prepare_live_page().snap("进入准备直播页面")
        sleep(2)
        # 判断开播按钮是否存在
        assert_equal(self.pre_live_page.in_current_page(), True, "准备直播页面开播按钮不存在")
        # 设置开播标题
        self.pre_live_page.click_live_title().set_live_title()
        return self
        
    def go_single_live(self):
        """
        开启普通直播
        :return:
        """
        # 去准备直播页面并设置标题
        self.go_pre_live_page_and_set_title()
        # 点击开播按钮开启普通直播
        self.pre_live_page.click_go_live().snap("已经进入直播间")
        # 判断是否开播成功
        assert_equal(self.live_page.in_current_page(), True, "开播失败")
        # 关闭直播
        self.live_page.close_live_anchor
        return self
        
    def go_nine_two_beam(self):
        """
        开启九连麦2人视频连麦
        :return:
        """
        pass

   
if __name__ == '__main__':
    sp = LiveAction()
    sp.go_single_live()
