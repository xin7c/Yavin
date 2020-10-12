# -*- encoding=utf8 -*-

__author__ = "shilei"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal
from common.login.user_login import LoginPage
from common.pages.LivePage import LivePage
from common.pages.SettingPage import SettingPage
from common.pages.PrepareLivePage import PrepareLivePage
from common.pages.HomePage import HomePage


if __name__ == '__main__':

    # 重启app->邮箱登录
    login_obj = LoginPage()
    login_obj.restart_app()
    login_obj.email_login()

    # 主播开播->关播
    home_obj = HomePage()
    home_obj.goto_prepare_live_page()

    preparelive_obj = PrepareLivePage()
    preparelive_obj.click_go_live()

    sleep(10)
    live_obj = LivePage()
    live_obj.close_live_anchor()

    # 退出登录
    setting_obj = SettingPage()
    # setting_obj.logout()











