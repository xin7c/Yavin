# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.login.user_login import *
from common.app.config import user_device_map
from airtest.core.api import *

auto_setup(__file__)


def login():
    sn = device().getprop('ro.serialno')
    if sn not in user_device_map.keys():
        raise(AssertionError('{sn} is not configured by any username/password'.format(sn=sn)))
    login_type = user_device_map[sn]['login_type']
    username = user_device_map[sn]['username']
    password = user_device_map[sn]['password']
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


def login_if_needed():
    # from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    # poco = AndroidUiautomationPoco(use_airtest_input=True,
    #                         screenshot_each_action=False)
    # if poco(text="Agree").exists() or poco(text="PHONE").exists():
    #     login()
    pass
