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
import subprocess
import sys
import time

from airtest.core.android.adb import ADB
from config.config import Config

# sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

file_path = os.path.dirname(os.path.abspath(__file__))

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
        print(f"返回{lDevice}")
        return lDevice
    else:
        return sDevices


def action(serial_no: str, case_name: str):
    print(serial_no)
    if os.path.isdir(f"{file_path}/log/{serial_no}"):
        print(f"{file_path}/log/{serial_no}存在")
    else:
        os.makedirs(f"{file_path}/log/{serial_no}")
        print(str(f"{file_path}/log/{serial_no}") + 'is created')
    os.system(
        f"airtest run {file_path}/testcase/{case_name} --device Android://127.0.0.1:5037/{serial_no} --log {file_path}/log/{serial_no}/")
    os.system(
        f"airtest report {file_path}/testcase/{case_name}  --log {file_path}/log/{serial_no}/ --export {file_path}/html_logs/{serial_no} --plugin "
        f"poco.utils.airtest.report")


def muti_run():
    print('Parent process {0} is Running'.format(os.getpid()))
    # cmd = "adb kill-server && adb start-server"
    # p = subprocess.Popen(cmd,
    #                      shell=True,
    #                      stdout=subprocess.PIPE,
    #                      stderr=subprocess.STDOUT)
    # p.wait()
    # time.sleep(1)
    # os.system("adb kill-server && adb start-server")
    jobs = []
    # for i in serialno_list:
    for i in GetDeviceNum():
        p = multiprocessing.Process(target=action, args=(i,
                                                         "setting.air"))
        print('process start')
        p.start()
        time.sleep(3)
        jobs.append(p)

    for j in jobs:
        j.join()
    print('Process close')


if __name__ == '__main__':
    # print(GetDeviceNum())

    print(file_path)
    muti_run()
    # for i in GetDeviceNum():
    #     action(i)
