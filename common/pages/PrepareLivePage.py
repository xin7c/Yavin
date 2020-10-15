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
        return self.poco(self.page_ele_loc("ID_TXT_VIDEO_START_LIVE")).exists() or False
    
    def click_live_title(self):
        """
       设置直播标题，并删除默认的标题内容
        :return:
        """
        self.find_click(self.page_ele_loc("ID_EDT_VIDEO_LIVE_TITLE"))
        sleep(2)
        return self
    
    def set_live_title(self):
        """
        重新输入想要的标题内容
        :return:
        """
        self.poco(self.page_ele_loc("ID_EDT_VIDEO_LIVE_TITLE")).set_text("AirTest UI AUTOMATION")
        sleep(4)
        return self
        
    def single_switch_to_multi_live(self):
        """
        前提提条件是在普通直播模式下，切换成Multi_beam
        id和text都取不到，用坐标点击(900,1650),然后除以手机屏幕实际大小
        :return:
        """
        self.poco.click([900 / self.screen_size[0], 1650 / self.screen_size[1]])
        sleep(2)
        return self
    
    def in_multi_beam_page(self):
        """
        判断准备直播页面是否在多人连麦模式，用ID_NINE_MODE_TWO: ":id/nine_mode_two"元素是否存在在判断
        :return:
        """
        return self.poco(self.page_ele_loc("ID_NINE_MODE_TWO")).exists() or False
    
    def multi_switch_to_single_live(self):
        """
        前提提条件是在multi_beam直播模式下，切换成single
        id和text都取不到，用坐标点击(180,1650)
        :return:
        """
        self.poco.click([180 / self.screen_size[0], 1650 / self.screen_size[1]])
        sleep(2)
        return self
    
    def single_switch_to_audio_live(self):
        """
        前提提条件是在普通直播模式下，切换成Multi_beam
        id和text都取不到，用坐标点击(180,1650),然后除以手机屏幕实际大小
        :return:
        """
        self.poco.click([180 / self.screen_size[0], 1650 / self.screen_size[1]])
        sleep(2)
        return self
    
    def audio_switch_to_single_live(self):
        """
        前提提条件是在Audio直播模式下，切换成single
        id和text都取不到，用坐标点击(900,1650),然后除以手机屏幕实际大小
        :return:
        """
        self.poco.click([900 / self.screen_size[0], 1650 / self.screen_size[1]])
        sleep(2)
        return self
    
    def click_go_live(self):
        """
        选择好开播模式之后，点击go live进行开播
        :return:
        """
        self.find_click(self.page_ele_loc("ID_TXT_VIDEO_START_LIVE"))
        sleep(15)
        return self
        

if __name__ == '__main__':
    print(PrepareLivePage().cls_name)
    sp = PrepareLivePage()
    # sp.goto_setting_page()
    # print(sp.click_go_live())
    # sp.goto_network_ping()
    # sp.click1("lalala")
    # print(sp.screen_size)
    print(sp.in_current_page())
