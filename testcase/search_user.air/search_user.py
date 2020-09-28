# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''搜索用户'''
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
import re
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from common.pages.SearchPage import *

poco = AndroidUiautomationPoco()


def search_user(keyword):
    # 进入搜索页面
    poco(SearchPage.HOME_SEARCH_IMG).click()
    sleep(20)
    assert_equal(poco(SearchPage.SEARCH_CONTENT_TAB).exists(), True, msg='进入搜索页面失败')
    # snapshot(msg='成功进入搜索页面')
    poco(SearchPage.SEARCH_CONTENT_TAB).click()
    sleep(2)
    text(keyword)
    assert_equal(poco(SearchPage.SEARCH_CONTENT_TAB).get_text(), keyword, msg='昵称输入失败')
    sleep(5)
    if poco(SearchPage.SEARCH_USER_NAME_ID).exists():
        user_list_id = poco(SearchPage.SEARCH_USER_NAME_ID)
        user_list = []
        for i in range(len(user_list_id)):
            user_list.append(poco(SearchPage.SEARCH_USER_NAME_ID)[i].get_text())
        print(user_list)
        user_name1 = user_list[0]
        m = re.search(keyword, user_name1, re.IGNORECASE)
        if m:
            print("找到了", keyword)
            # 找到了相应的用户
            assert_equal(poco(SearchPage.SEARCH_FOLLOW_ID).exists(), True, msg='找到搜索的用户昵称了')
            snapshot(msg='找到了搜索的用户')
            for k in range(len(poco(SearchPage.SEARCH_FOLLOW_ID))):
                if exists(Template('followed.png')):
                    touch(Template('followed.png'))
                    sleep(3)
                else:
                    break
        else:
            snapshot(msg='没有关注任何人')
            poco(SearchPage.SEARCH_FOLLOW_ID)[1].click()
            snapshot(msg='关注了搜索页面的第一个用户')
            # 点击进入搜索用户的他人页面
        
    else:
        # 没有找到相应的用户
        assert_exists(Template('search_user_null.png'))
        snapshot(msg='没有搜索到相应的用户')
    
    poco(SearchPage.SEARCH_CANCEL_ID).click()
    sleep(5)
    assert_equal(poco(SearchPage.SEARCH_BACK_ID).exists(), True, msg='成功回退到搜索页面')
    sleep(2)
    poco(SearchPage.SEARCH_BACK_ID).click()
    snapshot(msg='回到首页')


restart_app()
login_if_needed()
search_user('Hello')
# init_app()
# search_user('hello world china')
