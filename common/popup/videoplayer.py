# -*- encoding=utf8 -*-
"""
负责点掉直播间（videoplayer）弹窗
"""
import threading
from time import sleep

from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False)
android = Android()


def videoplayer_dialog_check():
    while True:

        # if poco("com.cmcm.live:id/txt_lucky").exists():
        #     poco.swipe("up")

        # 检查宝箱浮层
        if poco("com.cmcm.live:id/box_anim_view").exists():
            poco("com.cmcm.live:id/chest_close_iv").click()
            print("宝箱已关闭")

        # # 检查新用户引导
        # if poco("com.cmcm.live:id/img_follow").exists():
        #     android.keyevent("back")
        #     print("新用户引导已关闭")
        
        # 新用户关注引导弹窗
        if poco(text='Follow and get notified when the broadcast starts').exists():
            poco(text='Follow and get notified when the broadcast starts').click()
            sleep(2)
            print('新用户关注引导弹窗已经关闭')

        # 检查dialog
        if poco(name="live_first_follow_guaide.png").exists():
            poco("live_first_follow_guaide.png").click()
            print("直播间活动dialog已关闭")

        # 检查pk结束dialog
        if poco("com.cmcm.live:id/recyclerview_rank").exists():
            android.keyevent("back")
            print("pk结束dialog已关闭")

        # 检查升级弹窗
        if poco("com.cmcm.live:id/level_iv").exists():
            poco("com.cmcm.live:id/levelup_close").click()
            print("观众端升级弹窗已关闭")
            
        # 检查活动弹窗
        if poco('com.cmcm.live:id/guide_ignore').exists():
            poco('com.cmcm.live:id/guide_ignore').click()
            print("活动弹窗已关闭")

        # 检查活动宝箱
        if poco('com.cmcm.live:id/rewardImage').exists():
            poco('com.cmcm.live:id/click_btn').click()
            print('活动宝箱已关闭')

        sleep(1)


def videoplayer_popup_handler(func):
    t = threading.Thread(target=videoplayer_dialog_check)
    t.start()
    return func
