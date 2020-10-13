# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *

from poco.drivers.android.uiautomation import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from common.app.config import user_device_map


# 设备初始化
# adb = ADB()
# devices_list = adb.devices()
dev = device()
print(dev)
# device1 = connect_device("Android://127.0.0.1:5037/devices_list[0][0])")
# device2 = connect_device("Android://127.0.0.1:5037/devices_list[1][0])")
# if len(devices_list) >= 2:
#     poco_device1 = AndroidUiautomationPoco(Android(devices_list[0][0]))
#     poco_device2 = AndroidUiautomationPoco(Android(devices_list[1][0]))
# else:
#     poco_device1 = AndroidUiautomationPoco(Android(devices_list[0][0]))



# def private_msg():
#     # set_current(devices_list[1][0])
#     set_current(1).start_app('com.cmcm.live')
#     poco_device2('com.cmcm.live:id/me_page').click()



    





#
# def private_msg():
#     #获取device1设备上登录用户的的短id
#     restart_app()
    
# connect_device("android:///" + device2)
# restart_app()
# login_if_needed()
# private_msg()
# get_device2_user_name
