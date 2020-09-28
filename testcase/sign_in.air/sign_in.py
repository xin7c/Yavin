# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 点击首页按钮进入签到中心
# poco("com.cmcm.live:id/icon_active").click()
# sleep(10)


def show_star_gift():
    poco("com.cmcm.live:id/icon_active").click()
    sleep(10)
    if poco("com.cmcm.live:id/rlistview").exists():
        print("US 大区签到")
    else:
        # 点击每天奖励展示预览图片
        poco(text="DAY1").click()
        assert poco(text="You may get").exists(), "第一天奖励展示异常"

        poco(text="DAY2").click()
        assert poco(text="You may get").exists(), "第二天奖励展示异常"

        poco(text="DAY3").click()
        assert poco(text="You may get").exists(), "第三天奖励展示异常"

        poco(text="DAY4").click()
        assert poco(text="You may get").exists(), "第四天奖励展示异常"

        poco(text="DAY5").click()
        assert poco(text="You may get").exists(), "第五天奖励展示异常"

        poco(text="DAY6").click()
        assert poco(text="You may get").exists(), "第六天奖励展示异常"

        poco(text="DAY7").click()
        assert poco(text="You may get").exists(), "第七天奖励展示异常"
        # 签到规则
        # poco(text = "Rules").click()
        # touch(Template("close_rules.png"))


def sign_in():
    # 签到
    if exists(Template("Check_in.png")):
        print("找到了")
        touch(Template("Check_in.png"))
        sleep(2)
        touch(Template("close_gifts.png"))
        print("关闭弹窗成功")

    else:
        print("今天已经签过到了")


def receive_star():
    # 上滑，领取星光
    poco.swipe([0.5, 0.9], [0.5, 0.2], duration=1)
    sleep(2)
    print("上滑成功")

    # 判断有CLAIM就领取
    if poco(text="CLAIM").exists():
        for i in poco(text="CLAIM"):
            poco(text="CLAIM").click()
            time.sleep(5)
    else:
        # 在页面的一个模块里实现左右滑动,检查是否领取完
        poco("android.view.View").scroll('horizontal')
        if poco(text="CLAIM").exists():
            for i in poco(text="CLAIM"):
                poco(text="CLAIM").click()
                time.sleep(5)
        else:
            print('没有星光可以领取')


def event_center():
    # 查看活动中心
    poco("com.cmcm.live:id/textActivity").click()
    sleep(2)


restart_app()
login_if_needed()
show_star_gift()
sign_in()
receive_star()
event_center()
