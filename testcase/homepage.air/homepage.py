# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入首页各个tab页面'''
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

poco = AndroidUiautomationPoco()


def scan_featured():
    poco('com.cmcm.live:id/home_tabs').swipe('right')
    sleep(2)
    if poco(text="Featured").exists():
        poco(text="Featured").click()
        sleep(2)
        assert_exists(Template("homepage_feature.png"), "定位到了Feature_tab页面")
        scroll()
    else:
        raise AssertionError('没有找到Featured tab')
    

def scan_new():
    poco('com.cmcm.live:id/home_tabs').swipe('left')
    sleep(2)
    if poco(text="New").exists():
        poco(text="New").click()
        sleep(5)
        assert_exists(Template("homepage_new.png"), "定位到了new_tab页面")
        scroll()
    else:
        raise AssertionError('没有找到New tab')


def scan_nearby():
    poco('com.cmcm.live:id/home_tabs').swipe('left')
    sleep(2)
    if poco(text="Nearby").exists():
        poco(text="Nearby").click()
        sleep(5)
        assert_exists(Template("homepage_nearby.png"), "定位到了nearby_tab页面")
        scroll()
    else:
        raise AssertionError('没有找到对应的nearby tab')


def scan_world():
    poco('com.cmcm.live:id/home_tabs').swipe('left')
    sleep(2)
    if poco(text="World").exists():
        poco(text="World").click()
        sleep(5)
        assert_exists(Template("homepage_world.png"), "定位到了world_tab页面")
        scroll()
    else:
        raise AssertionError('没有找到对应的world tab')


def scan_game():
    poco('com.cmcm.live:id/home_tabs').swipe('left')
    sleep(2)
    if poco(text="Game").exists():
        poco(text="Game").click()
        sleep(5)
        assert_exists(Template("homepage_game.png"), "定位到了game_tab页面")
        scroll()
    else:
        raise AssertionError('没有找到对应的game tab')


def scan_videos():
    poco('com.cmcm.live:id/home_tabs').swipe('left')
    sleep(2)
    if poco(text="Videos").exists():
        poco(text="Videos").click()
        sleep(5)
        # assert_exists(Template("homepage_videos.png"), "定位到了homepage_videos_tab页面")
        assert poco('com.cmcm.live:id/like_count_tv').exists(), '进入videos页面失败'
        scroll()
    else:
        raise AssertionError('没有找到videos tab')
        
        
def scan_social():
    poco('com.cmcm.live:id/home_tabs').swipe('right')
    sleep(2)
    if poco(text="Social").exists():
        poco(text="Social").click()
        sleep(5)
        # assert_exists(Template("homepage_social.png"), "定位到了game_tab页面")
        assert poco('com.cmcm.live:id/game_tab_title').get_text() == 'Social', '进入Social页面失败'
        scroll()
    elif poco(text='Follow').exists():
        poco(text='Follow').click()
        assert poco('com.cmcm.live:id/follow_title_tv').exists(), '进入Follow页面'
        scroll()
    else:
        raise AssertionError('没有找到Social tab也没有找到follow tab')

      
def scan_ranking_board():
    poco('com.cmcm.live:id/home_rank_img').click()
    sleep(20)
    assert_exists(Template("homepage_ranking_board.png"), "定位到了ranking_board_tab页面")
    scroll()
    poco('com.cmcm.live:id/singleBack').click()
    sleep(2)
    assert poco('com.cmcm.live:id/uplive').exists(), "没有返回到首页"
    
    
def scroll():
    for i in range(20):
        poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.2)
    for i in range(8):
        poco.swipe([0.5, 0.2], [0.5, 0.8], duration=0.2)
    sleep(5)
        
        
restart_app()
login_if_needed()
scan_social()
scan_featured()
scan_new()
scan_world()
scan_game()
scan_videos()
scan_ranking_board()

 
    



