# -*- encoding=utf8 -*-
__author__ = "liulili"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#在登录状态下启动APP
start_app("com.cmcm.live")
sleep(2)
#关闭广告
if poco("com.cmcm.live:id/img_ad").exists():
    poco("com.cmcm.live:id/txt_right").click()

# 断言是否出现了开播icon
    assert_exists(Template("broadcast.png", record_pos=(-0.124, -0.426), resolution=(720, 1280)))
sleep(1.0)

#点击小喇叭进入开播放页面
poco("com.cmcm.live:id/uplive").click()
sleep(1.0)

#开播
poco("com.cmcm.live:id/txt_video_start_live").click()
sleep(3.0)

poco("com.cmcm.live:id/layout_mask").click()
sleep(1.0)
poco(text="Sticker").click()
sleep(3.0)
#poco("com.cmcm.live:id/gridview").child("android.widget.FrameLayout")[4].child("android.widget.FrameLayout").child("com.cmcm.live:id/sticker_img").click()
#下载贴纸
if poco("com.cmcm.live:id/sticker_status_icon").exists():
    poco("com.cmcm.live:id/sticker_status_icon").click()
    sleep(6.0)
    print("下载贴纸！")
else:
    sleep(1.0)
    #poco("com.cmcm.live:id/sticker_img").click()
    poco("com.cmcm.live:id/gridview").child("android.widget.FrameLayout")[4].child("android.widget.FrameLayout").child("com.cmcm.live:id/sticker_img").click()


#assert_not_exists(Template(r"tpl1561558617494.png", record_pos=(-0.356, 0.438), resolution=(1080, 1920)), "贴纸未成功佩戴.")
assert_exists(Template("sticker_download.png", record_pos=(0.361, 0.434), resolution=(1080, 1920)), "下载佩戴贴纸正常.")





