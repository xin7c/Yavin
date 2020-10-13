# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
import datetime
from airtest.core.api import *
from poco.drivers.android.uiautomation import *

poco = AndroidUiautomationPoco()


class Message(self, device1, device2):
    
    def __init__(self):
        self.device1 = device1
        self.device2 = device2
    
    def private_message_send(self):
        init_device("Android", self.device1)
        connect_device("android:///")