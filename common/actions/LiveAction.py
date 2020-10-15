# -*- coding:utf-8 -*-
# author: wanglimin
# date: 2020-10-15 11:19
# file: LiveAction.py.py
# IDE: PyCharm

from common.pages.BasePage import BasePage
from common.pages.HomePage import HomePage
from common.pages.PrepareLivePage import PrepareLivePage
from common.pages.LivePage import LivePage
from config.config import Config


class LiveAction(BasePage):
    home_page = HomePage()
    pre_live_page = PrepareLivePage()
    live_page = LivePage()
    
    def go_single_live(self):
        self.home_page.
        
    