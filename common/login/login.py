# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.login.UserLogin import *
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
    user = LoginUser(username, password)
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
    if poco(text="Agree").exists() or poco(text="PHONE").exists():
        login()
