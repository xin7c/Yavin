# -*- encoding=utf8 -*-
__author__ = 'liuxiaomei'

from common.login.LoginPage import LoginPage
from common.pages.HomePage import HomePage
from common.pages.SettingPage import SettingPage
from config.config import Config
from airtest.core.api import *

auto_setup(__file__)

class LoginAction():
    def __init__(self):
        self.home_obj = HomePage()

    def login(self):
        devices_list = Config().get_devices_list
        sn = device().getprop('ro.serialno')
        if sn not in devices_list:
            raise(AssertionError('{sn} is not configured by any username/password'.format(sn=sn)))
        config_obj = Config()
        login_type = config_obj.get_info_by_sn(sn).get('login_type')
        username = config_obj.get_info_by_sn(sn).get("username")
        password = config_obj.get_info_by_sn(sn).get('password')
        user = LoginPage(username, password)
        if login_type == 'email':
            user.email_login()
        elif login_type == 'google':
            user.google_login()
        elif login_type == 'twitter':
            user.twitter_login()
        elif login_type == 'ins':
            user.instagram_login()
        elif login_type == 'phone':
            user.phone_login()


    def login_if_needed(self):
        """
        判断是否需要登录，如果未登录则进行登录操作，如果已登录则跳过
        """

        self.home_obj.restart_app()

        if self.home_obj.in_appin():
            print("已登录成功，不需要登录")
        else:
            self.login()


    def mandatory_login(self):
        """
        强制登录：如果已登录那么先退出登录账号，在进行登录
        """
        # self.home_obj.restart_app()

        if self.home_obj.in_appin():
            print("已登录，将退出账号在进行登录")
            setting_obj = SettingPage()
            setting_obj.logout()

        self.home_obj.restart_app()
        self.login()


if __name__ == '__main__':
    LoginAction().mandatory_login()
    LoginAction().login_if_needed()

