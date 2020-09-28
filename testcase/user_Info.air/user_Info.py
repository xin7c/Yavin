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

# 进入个人页
poco("com.cmcm.live:id/me_page").click()


# 修改用户个人信息
def update_user_info():
    # 修改个人信息
    poco("com.cmcm.live:id/personal_edit_img").click()
    sleep(2)

    # 上传头像
    if poco("com.cmcm.live:id/item_edit_add_img").exists():
        poco("com.cmcm.live:id/item_edit_add_img").click()
        poco(text="Take a Photo").click()
        # 勾选照相机+声音授权弹窗
        if poco("android:id/alertTitle").exists():
            poco("com.android.packageinstaller:id/do_not_ask_checkbox").click()
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
        if poco("android:id/alertTitle").exists():
            poco("com.android.packageinstaller:id/do_not_ask_checkbox").click()
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
        # 拍照保存
        poco("com.huawei.camera:id/shutter_button").click()
        poco("com.huawei.camera:id/btn_done").click()
        poco("com.android.gallery3d:id/head_select_right").click()
        print("头像上传成功")
    else:
        # 先删除一张，后拍照
        poco("com.cmcm.live:id/item_edit_poster_img")[1].click()
        poco(text="Delete").click()
        print("已经上传了8张头像")

    # 修改用户名
    # 先删除用户名
    poco("com.cmcm.live:id/edit_attrib_nickname_clear").click()
    poco("com.cmcm.live:id/edit_user_name").click()
    text("Testname123")
    if poco(text="Testname123").exists():
        print("用户名修改成功")
        sleep(5)

    # 修改性别
    if poco(text="Male").exists():
        poco(text="Male").click()
        poco(text="Female").click()
        print("已经将男性改为女性")
    elif poco(text="Female").exists():
        poco(text="Female").click()
        poco(text="Secret").click()
        print("已经将男性改为隐藏性别")
    elif poco(text="Secret").exists():
        poco(text="Secret").click()
        poco(text="Male").click()
        print("已经将隐藏性别改为男性")
        sleep(3)
    # 修改年龄，提示一年只能修改一次
    poco("com.cmcm.live:id/edit_attr_tv_birthday").click()
    if exists(Template("age_toast.png")):
        print("一年只能修改一次年龄")

    # 上滑
    poco.swipe([0.5, 0.9], [0.5, 0.2], duration=0.2)

    # 修改个人描述
    poco("com.cmcm.live:id/edit_sign").click()
    # text(self.user_sign)
    text("I am a boy")
    print("添加个人签名完成")
    sleep(5)

    # 添加兴趣爱好
    poco(text="Add").click()
    sleep(2)

    if poco(text="音樂").exists():
        # 删除后重新添加
        j = int(poco("com.cmcm.live:id/edit_selected_num").get_text())
        for i in range(j):
            poco("com.cmcm.live:id/tag_cancel").click()
            poco("com.cmcm.live:id/button1").click()
        poco(text="音樂").click()
    poco(text="SAVE").click()
    print("添加音乐兴趣爱好成功")
    sleep(2)
    poco(text="SAVE").click()
    sleep(5)
    # 保存本次修改信息
    print("本次修改成功")


# 查看Top Fans
def top_fans():
    poco("com.cmcm.live:id/personal_top_fan_tv").click()
    # 查看周榜礼物奖励
    poco("com.cmcm.live:id/tv_tops_type").click()
    sleep(5)
    poco("com.cmcm.live:id/close_btn").click()

    # 切换各级tab看展示是否正常
    poco(text="Daily").click()
    sleep(1)

    poco(text="Total").click()
    # 进入top1个人页
    poco("com.cmcm.live:id/top_fan_01").click()

    if exists(Template("addFollow.png")):
        print("没有关注他，那快关注吧")
        poco("com.cmcm.live:id/img_follow").click()

    elif exists(Template("following.png")):
        print("已经关注了，取消关注")
        poco("com.cmcm.live:id/img_follow").click()
    sleep(5)
    # while poco("com.cmcm.live:id/txt_loading_state").exists():
    #     poco.swipe([0.5,0.2],[0.5,0.9],duration=0.2)
    poco("com.cmcm.live:id/img_back").click()

    poco(text="Star points (total)").click()
    poco("com.cmcm.live:id/top_fan_01").click()
    sleep(1)
    if exists(Template("addFollow.png")):
        print("没有关注他，那快关注吧")
        poco("com.cmcm.live:id/txt_follow_status_hint").click()
    elif exists(Template("following.png")):
        print("已经关注了，取消关注")
        poco("com.cmcm.live:id/txt_follow_status_hint").click()
    sleep(5)
    poco("com.cmcm.live:id/img_back").click()
    sleep(5)
    poco("com.cmcm.live:id/img_left").click()

    print("周榜验证结束")


# 验证粉丝列表和关注列表
# def fans():
#     poco.swipe([0.5,0.2],[0.5,0.3])
#     fans = poco("com.cmcm.live:id/personal_fans_count_tv").get_text()
#     followings = poco("com.cmcm.live:id/personal_followings_count_tv").get_text()
#
#     poco("com.cmcm.live:id/personal_fans_count_tv").click()
#     #搜索查询一个人
#     text("a")

def my_bag():
    sleep(5)
    poco.swipe([0.5, 0.7], [0.5, 0.1], duration=0.5)
    touch(Template("mybag.png"))
    sleep(5)
    # 循环点击左侧菜单栏
    # menu = poco("com.cmcm.live:id/mybag_menu").get_text()
    # print(menu)
    # munu_title = poco("bag_title").get_text()
    # print(munu_title)
    # munu_title = []
    # title_len = len(munu_title)
    # # for i in range(title_len):

    poco("com.cmcm.live:id/mybag_back").click()


def moments():
    sleep(5)
    # 单独执行需要放开注释，上滑到指定位置
    # poco.swipe([0.5, 0.4], [0.5, 0.1], duration=0.5)
    if poco("com.cmcm.live:id/list_moments").exists():
        poco("com.cmcm.live:id/img_cover").click()
        # 播放第一个视频动态
        poco("com.cmcm.live:id/img_cover0").click()

        # poco("com.cmcm.live:id/like_num0").get_text()  # 点赞数
        # nickname = poco("com.cmcm.live:id/anchor_nickname ").get_text()  #用户名

        # 查看个人卡片
        poco("com.cmcm.live:id/img_user_head").click()
        sleep(5)
        # 进入个人页获
        poco("com.cmcm.live:id/level_head_icon").click()
        poco.swipe([0.5, 0.7], [0.5, 0.2])
        poco("com.cmcm.live:id/img_back").click()

        # 再次查看个人卡片进入家族页
        poco("com.cmcm.live:id/img_user_head").click()
        sleep(5)
        poco("com.cmcm.live:id/txt_fam_entry").click()
        sleep(10)
        poco("com.cmcm.live:id/img_left").click()

        # 点赞
        like_num1 = poco("com.cmcm.live:id/like_count_tv").get_text()
        poco("com.cmcm.live:id/like_btn").click()
        sleep(5)
        like_num2 = poco("com.cmcm.live:id/like_count_tv").get_text()
        assert_not_equal(like_num1, like_num2, '点赞成功')
        print("susses")
        sleep(3)
        # if like_num1 != like_num2:
        #             #     print("点赞成功")
        #             # else:
        #             #     assert "点赞异常，再试一次"

        # 评论
        poco("com.cmcm.live:id/comment_btn").click()
        poco("com.cmcm.live:id/tv_input").click()
        sleep(2)
        text("cool like")
        poco("com.cmcm.live:id/tv_send_button").click()
        sleep(5)
        word1 = poco('com.cmcm.live:id/txt_comment_content').get_text()
        if word1 == "cool like":
            print("susses")
        else:
            print("失败")
            assert_not_equal(word1, '评论成功')

        sleep(3)
        poco("com.cmcm.live:id/iv_comments_close").click()

        # 送星光
        poco("com.cmcm.live:id/short_gift_start_iv").click()
        if exists("toast.png"):
            print("自己的视频不能点赞")

        poco("com.cmcm.live:id/img_close").click()


def take_moments():
    sleep(5)
    # 单独执行需要放开注释，上滑到指定位置
    # poco.swipe([0.5, 0.4], [0.5, 0.1], duration=0.5)
    if poco("com.cmcm.live:id/list_moments").exists():
        poco("com.cmcm.live:id/img_cover").click()
        sleep(3)

        # 拍摄视频
        touch(Template("add_video.png"))
        print("进入成功")
        if poco("Direct access to the microphone to record audio").exists():
            poco("com.android.packageinstaller:id/do_not_ask_checkbox").click()
            poco("com.android.packageinstaller:id/permission_allow_button").click()
        # 添加本地音乐
        poco("com.cmcm.live:id/view_bgm").click()
        sleep(5)

        poco(text="Local music").click()
        sleep(5)
        print("进入本地音乐成功")
        poco.swipe([0.5, 0.9], [0.5, 0.2])
        poco("com.cmcm.live:id/img_back").click()

        poco("com.cmcm.live:id/music_cover")[1].click()
        sleep(10)
        # assert exists(Template("reloading.png")), '音乐加载失败'
        poco("com.cmcm.live:id/music_user_button").click()
        print("音乐插入成功")
        sleep(2)

        # 添加贴纸
        poco("com.cmcm.live:id/view_sticker").click()
        sleep(3)
        # 先点击一次，防止未加载
        poco("com.cmcm.live:id/sticker_img")[5].click()
        sleep(2)
        poco("com.cmcm.live:id/sticker_img")[5].click()
        # 点击空白处收起面板
        poco.click([0.2, 0.2])
        print("添加贴纸成功")

        # 切换摄像头
        poco("com.cmcm.live:id/view_switch_camera").click()
        sleep(2)
        poco("com.cmcm.live:id/view_switch_camera").click()
        print("切换摄像头成功")

        # 点击321倒计时,验证重拍
        poco("com.cmcm.live:id/view_count_down").click()
        sleep(5)
        poco("com.cmcm.live:id/img_record").click()
        sleep(2)
        if poco("com.cmcm.live:id/view_revoke").exists():
            poco("com.cmcm.live:id/view_revoke").click()
            # 删除本次操作
            poco("com.cmcm.live:id/button1").click()

        # 录制10s，保存视频
        poco("com.cmcm.live:id/view_count_down").click()
        sleep(10)
        touch(Template("break.png"))
        poco("com.cmcm.live:id/view_generate").click()
        sleep(3)

        # 点击发送
        poco("com.cmcm.live:id/img_publish").click()
        poco("com.cmcm.live:id/tv_ok").click()
        print("短视频发送成功")
        sleep(60)

        # 回到了首页
        poco("com.cmcm.live:id/img_left").click()


restart_app()
login_if_needed()
update_user_info()
top_fans()
# fans()
my_bag()
moments()
take_moments()
