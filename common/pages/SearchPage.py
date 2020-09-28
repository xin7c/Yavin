# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
from airtest.core.api import *
poco = AndroidUiautomationPoco()


class SearchPage(BasePage):
    # 首页的搜索图标
    HOME_SEARCH_IMG = 'com.cmcm.live:id/home_search_img'
    # 搜索页面的搜索输入框
    SEARCH_CONTENT_TAB = 'com.cmcm.live:id/search_content'
    SEARCH_USER_NAME_ID = 'com.cmcm.live:id/search_name'
    SEARCH_FOLLOW_ID = 'com.cmcm.live:id/search_follow'
    SEARCH_CANCEL_ID = 'com.cmcm.live:id/search_cancel'
    SEARCH_BACK_ID = 'com.cmcm.live:id/search_back'
    # 搜索页面game入口
    GAME_NAME = 'com.cmcm.live:id/tag_desc'
    GAME_TEXT = 'Game'
    # 搜索页面Videos入口
    VIDEOS_TEXT = 'Videos'
    
    # Girls入口
    GIRLS_TEXT = 'Girls'
    # Talent入口
    TALENT_NAME = 'Talent'
    # Guys入口
    GUYS_NAME = 'Guys'
    
    def goto_this(self, from_page=None):
        # 点击搜索图标进入搜索页面
        sleep(30)
        poco(self.HOME_SEARCH_IMG).click()
        sleep(60)
    
    def in_current_page(self):
        if poco(self.SEARCH_CONTENT_TAB).exists():
            return True
        else:
            return False
        
    def is_game_tab_exists(self):
        if poco(name=self.GAME_NAME, text=self.GAME_TEXT).exists():
            return True
        else:
            return False
            
    def goto_game(self):
        # 进入game二级页面
        poco(text=self.GAME_TEXT).click()
        sleep(60)
        
    def is_videos_tab_exists(self):
        if poco(text=self.VIDEOS_TEXT).exists():
            return True
        else:
            return False
        
    def goto_videos(self):
        # 进入videos二级页面
        poco(text=self.VIDEOS_TEXT).click()
        sleep(60)
    
    def is_girls_tab_exists(self):
        if poco(text=self.GIRLS_TEXT).exists():
            return True
        else:
            return False
        
    def goto_girls(self):
        poco(text=self.GIRLS_TEXT).click()
        sleep(30)
        
    



