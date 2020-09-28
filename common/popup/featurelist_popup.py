# -*- encoding=utf8 -*-

"""
负责点掉首页弹窗
"""

from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.get_current_activity import *

poco = AndroidUiautomationPoco(force_restart=False)
android = Android()


def featurelist_popup_window():
    if current_activity() == "com.cmcm.live/com.cmcm.cmlive.activity.VideoListActivity":
        # 异常断播弹窗
        if poco("com.cmcm.live:id/scrollView").exists():
            poco("com.cmcm.live:id/button2").click()
        # 隐私弹窗
        if poco("com.cmcm.live:id/agree_tv").exists():
            poco("com.cmcm.live:id/agree_tv").click()
        # 星光任务
        if poco("com.cmcm.live:id/check_in_positive").exists():
            poco("com.cmcm.live:id/check_in_close").click()
        # 私信弹窗
        if poco("com.cmcm.live:id/letter_remind_img").exists():
            android.keyevent("back")
        # 评分弹窗
        if poco("com.cmcm.live:id/rating_positive").exists():
            poco("com.cmcm.live:id/rating_close").click()
        # 闪屏/开屏
        if poco("com.cmcm.live:id/img_ad").exists():
            poco("com.cmcm.live:id/txt_right").click()




