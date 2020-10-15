# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-10 17:38
# file: goto_single_live.py
# IDE: PyCharm

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.pages.BasePage import BasePage
from common.pages.HomePage import HomePage
from common.pages.PrepareLivePage import PrepareLivePage
from common.pages.LivePage import LivePage


def goto_single_live():
    # 点击开播按钮进入准备直播页面
    home_page = HomePage()
    pre_live_page = PrepareLivePage()
    live_page = LivePage()
    
    home_page.goto_prepare_live_page()
    sleep(2)
    assert_equal(pre_live_page.in_current_page(), True, "开播按钮存在")
    sleep(2)
    # 编辑直播标题
    pre_live_page.click_live_title()
    sleep(2)
    pre_live_page.set_live_title().snap()
    sleep(2)
    # 点击开播按钮进入直播间
    pre_live_page.click_go_live()
    sleep(10)
    assert_equal(LivePage().in_current_page(), True, "主播直播数据按钮存在")
    live_page.close_review_pop()
    # 关闭直播
    live_page.close_live_anchor


def home_goto_multi_two_live():
    pass




goto_single_live()

        
        
        
        
    
    