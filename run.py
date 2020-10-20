#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:run.py
@time:2020/09/24
"""
import multiprocessing
import os

# airtest run testcase/setting.air.air --device Android://127.0.0.1:5037/CB5A2AE8LW
# airtest run testcase/setting.air.air --device Android://127.0.0.1:5037/T7G0216117000139
from airtest.core.android.adb import ADB
from config.config import Config

serialno_list = [
    "CB5A2AE8LW",
    "5LM0216122006648"
]


def GetValidDevices():
    """获取本地连接的设备号列表"""
    lData = ADB().devices('device')
    lPositiveDevices = [item[0] for item in lData]
    return lPositiveDevices


def GetDeviceNum():
    sDevices = Config.get_yaml().get("android_devices")
    lDevice = GetValidDevices()
    if not sDevices and lDevice:
        return [lDevice[0]]
    elif 'all' in sDevices:
        return lDevice
    else:
        return sDevices


def action(serialno):
    print(serialno)
    if os.path.isdir(f"log/{serialno}"):
        print("log/存在")
    else:
        os.makedirs(f"log/{serialno}")
        print(str(f"log/{serialno}") + 'is created')
    os.system(f"airtest run testcase/setting.air --device Android://127.0.0.1:5037/{serialno} --log log/{serialno}/")
    os.system(f"airtest report testcase/setting.air --log log/{serialno}/ --export html_logs/{serialno} --plugin "
              f"poco.utils.airtest.report")


def muti_run():
    print('Parent process {0} is Running'.format(os.getpid()))
    jobs = []
    # for i in serialno_list:
    for i in GetDeviceNum():
        p = multiprocessing.Process(target=action, args=(i,))
        print('process start')
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
    print('Process close')


if __name__ == '__main__':
    # print(GetDeviceNum())
    muti_run()
    # for i in GetDeviceNum():
    #     action(i)
