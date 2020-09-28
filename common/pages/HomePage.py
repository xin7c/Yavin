# -*- encoding=utf8 -*-

from common.app.get_current_activity import *
from common.pages.SearchPage import *
from common.pages.SecondaryGirlsPage import *

poco = AndroidUiautomationPoco()


class HomePage(BasePage):
    HOME_PAGE_ACTIVITY_NAME = 'com.cmcm.live/com.cmcm.cmlive.activity.VideoListActivity'
    Uplive_Button = 'com.cmcm.live:id/uplive'
    Me_Page = 'com.cmcm.live:id/me_page'
    HOMEPAGE_LIVE = 'com.cmcm.live:id/tv'
    SEARCH_BUTTON = 'com.cmcm.live:id/home_search_img'
    # 请求地理位置信息弹窗
    POSITION_ALLOW_BTN_ID = "com.android.packageinstaller:id/permission_allow_button"
    # 签到
    CHECK_IN_TEXT = "CHECK IN"
    CHECK_IN_RESULT_CLOSE_ID = "com.cmcm.live:id/check_in_result_close"
    # 新签到
    CHECK_IN_RESULT_CLOSE_AR_ID = "com.cmcm.live:id/checkin_ar_close"
    CHECK_IN_RESULT_CLOSE_NEW_ID = "com.cmcm.live:id/check_in_close"
    # 首页顶部导航栏页面
    HOME_TAB_ID = 'com.cmcm.live:id/home_tabs'
    HOME_FEATURE_NAME = "Featured"
    HOME_NEW_NAME = "New"
    HOME_NEARBY_NAME = "Nearby"
    HOME_FOLLOW_NAME = 'Follow'
    HOME_SOCIAL_NAME = "Social"
    HOME_GAME_NAME = "Game"
    HOME_WORLD_NAME = "World"
    HOME_VIDEOS_NAME = "Videos"
    HOME_SEARCH_IMG = 'com.cmcm.live:id/home_search_img'
    HOME_RANKING_BOARD = 'com.cmcm.live:id/home_rank_img'
    # loading 按钮
    HOME_REFRESH_LOADING_MORE_ID = 'com.cmcm.live:id/txt_loading_state'
    HOME_LOADING_END_TEXT_NAME = 'The End'
    # 主播封面
    HOME_IMG_NAME = 'android.view.ViewGroup'
    # 底部页面
    
    def in_current_page(self):
        # fixme: 不能用 top activity 的名称来判断是否在主页，因为我的页面的 top activity 跟主页是一样的
        if current_activity() == self.HOME_PAGE_ACTIVITY_NAME:
            return True
        else:
            return False

    def click_uplive_button(self):
        poco(self.Uplive_Button).click()
        for k in range(3):
            if poco("com.android.packageinstaller:id/permission_message").exists():
                poco("com.android.packageinstaller:id/permission_allow_button").click()
                sleep(2)

    def goto_me_page(self):
        poco(self.Me_Page).click()

    def watch_broadcast(self):
        if poco(self.HOMEPAGE_LIVE).exists():
            poco(self.HOMEPAGE_LIVE).click()
            sleep(6)
            
    def goto_feature(self):
        if poco(text=self.HOME_FEATURE_NAME).exists():
            poco(text=self.HOME_FEATURE_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_FEATURE_NAME)
        
    def goto_follow(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('right')
        if poco(text=self.HOME_FOLLOW_NAME).exists():
            poco(text=self.HOME_FOLLOW_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_FOLLOW_NAME)
    
    def goto_world(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('right')
        if poco(text=self.HOME_WORLD_NAME).exists():
            poco(text=self.HOME_WORLD_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_WORLD_NAME)
        
    def goto_new(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('left')
        if poco(text=self.HOME_NEW_NAME).exists():
            poco(text=self.HOME_NEW_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_NEW_NAME)

    def goto_nearby(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('left')
        if poco(text=self.HOME_NEARBY_NAME).exists():
            poco(text=self.HOME_NEARBY_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_NEARBY_NAME)
        
    def goto_game(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('left')
        if poco(text=self.HOME_GAME_NAME).exists():
            poco(text=self.HOME_GAME_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_GAME_NAME)
        
    def goto_videos(self):
        for i in range(5):
            poco(self.HOME_TAB_ID).swipe('left')
        if poco(text=self.HOME_VIDEOS_NAME).exists():
            poco(text=self.HOME_VIDEOS_NAME).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_VIDEOS_NAME)
        
    def goto_search(self):
        if poco(text=self.HOME_SEARCH_IMG).exists():
            poco(text=self.HOME_SEARCH_IMG).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_SEARCH_IMG)
        
    def goto_ranking_board(self):
        if poco(text=self.HOME_RANKING_BOARD).exists():
            poco(text=self.HOME_RANKING_BOARD).click()
        else:
            raise AssertionError('没有找到%s' % self.HOME_RANKING_BOARD)
        
    def is_loading_end(self):
        if poco(self.HOME_REFRESH_LOADING_MORE_ID).exists():
            return False
        else:
            return True

    def home_goto_live(self):
        sleep(10)
        if len(poco(self.HOME_IMG_NAME)) <= 0:
            raise AssertionError('页面没有找到直播')
        else:
            poco(name=self.HOME_IMG_NAME)[0].click()
     
    @staticmethod
    def scroll_page():
        while HomePage().is_loading_end():
            poco.swipe([0.5, 0.7], [0.5, 0.1], duration=0.2)
            snapshot(msg='向下滑动视频')
        # 向上滑动
        for i in range(5):
            print(i)
            poco.swipe([0.5, 0.2], [0.5, 0.8], duration=0.2)

