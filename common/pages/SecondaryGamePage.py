# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
from airtest.core.api import *

poco = AndroidUiautomationPoco()


class SecondaryGamePage(BasePage):
    # game页面game开播按钮
    GAME_GO_LIVE_iCON = 'com.cmcm.live:id/iv_game_live'
    GAME_TYPE = 'com.cmcm.live:id/home_tab_title'
    LOADING_STATUS = 'com.cmcm.live:id/txt_loading_state'
    LIVE_VIEW_NAME = 'android.widget.ImageView'
    
    # poco(name='android.widget.ImageView')[0].click()
    
    def in_current_page(self):
        if poco(self.GAME_GO_LIVE_iCON).exists():
            return True
        else:
            return False
        
    def obtain_all_game_tab(self):
        # 获取游戏所有的标签tag
        game_title = poco(self.GAME_TYPE)
        game_type_list = []
        for l in range(len(game_title)):
            game_type_list.append(game_title[l].get_text())
        print(game_type_list)
        return game_type_list
      
    def loading_status(self):
        # 刷新游戏列表是否已经到最低端
        if poco(self.LOADING_STATUS).exists():
            return False
        else:
            return True
    
    def is_game_live_exists(self):
        if len(poco(self.LIVE_VIEW_NAME)) > 0:
            return True
        else:
            return False
    
    def goto_game_live(self):
        poco(self.LIVE_VIEW_NAME)[0].click()
        sleep(60)
        
    
    
    
    
    
   
    
   





