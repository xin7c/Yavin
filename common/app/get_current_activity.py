# -*- encoding=utf8 -*-

__author__ = "liyue"


from airtest.core.android.android import *
from airtest.core.android.adb import *

android = Android()
my_serialno = android.get_default_device()
adb = ADB(serialno=my_serialno, adb_path=None, server_addr=None)


def current_activity():
    return '/'.join(android.get_top_activity()[:-1])

print(current_activity())
