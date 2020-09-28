# -*- encoding=utf8 -*-
__author__ = "liulili"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from common.pages.HomePage import HomePage
from common.pages.OtherPage import OtherBasePage
from airtest.core.api import *
from airtest.core.helper import log
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from common.app.app_control import restart_app
from common.login.login import login_if_needed

restart_app()
login_if_needed()

# 进入直播间
if not HomePage().in_current_page():
    raise AssertionError("冷启app后没有进入主页")
poco("com.cmcm.live:id/recycler_view").child("android.view.ViewGroup")[0].click()

# 点击头像进入个人卡片
poco("com.cmcm.live:id/img_user_head").click()

if poco("com.cmcm.live:id/id_dialog_anchor_report").exists():
    #poco("com.cmcm.live:id/id_dialog_anchor_report").click()
    log("个人卡片展示成功！")
    print("个人卡片展示成功！")
    poco("com.cmcm.live:id/level_head_icon").click()
sleep(5.0)

# 判断是否进入了他人页面
other_page = OtherBasePage()
if not other_page.in_current_page():
    raise AssertionError("没有来到他人页")
other_page.click_more_menu()

# 点击加入封锁清淡
# FIXME：多语言怎么兼容？
poco(text="Add to Block List").click()
sleep(1.0)

# 封锁确认弹窗
poco("com.cmcm.live:id/blockade_positive").click()
print("已确认添加至封锁！")
log("已确认添加至封锁！")
sleep(3.0)

poco("com.cmcm.live:id/img_user_head").click()
sleep(1.0)
poco("com.cmcm.live:id/level_head_icon").click()


if poco("android.view.ViewGroup").exists():
    print("添加封锁成功了！")
assert_exists(Template("block_win.png"), '添加封锁成功了')

