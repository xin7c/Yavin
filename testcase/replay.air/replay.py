# -*- encoding=utf8 -*-
__author__ = "zhangleilei"
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.pages.HomePage import HomePage
from common.pages.MePage import MePage
from common.pages.ReplayPage import *
from common.app.app_control import *
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 评论 评论一条信息，内容+1
def comment():
    comment_content = poco("com.cmcm.live:id/tv_comments_num").get_text()
    before_comment_content = int(''.join([i for i in comment_content if str.isdigit(i)]))
    poco("com.cmcm.live:id/iv_comment").click()
    poco("com.cmcm.live:id/tv_input").set_text("verify")
    poco("com.cmcm.live:id/tv_send_button").click()
    time.sleep(2)
    after_comment_content=poco("com.cmcm.live:id/tv_comments_num").get_text()
    poco("com.cmcm.live:id/img_close").click()
    after_comment_amount = int(''.join([i for i in after_comment_content if str.isdigit(i)]))
    assert_equal(before_comment_content+1, after_comment_amount, "评论数量不正确")


# 快进
def fast():
    poco("com.cmcm.live:id/seekbar_video_progress").swipe([0.0842, 0.63026])
    assert_equal(poco("com.cmcm.live:id/iv_praise").exists(), True)


# 暂停 停留5秒，暂停按钮，前后时间相同证明暂停
def pause():
    poco("com.cmcm.live:id/video_playback_image_view").click()
    assert_exists(Template("pause.png"))
    before_pause = poco("com.cmcm.live:id/video_playback_progress_txt").get_text()
    time.sleep(5)
    after_pause = poco("com.cmcm.live:id/video_playback_progress_txt").get_text()
    assert_equal(before_pause, after_pause)


# 钻石榜榜单
def diamond():
    poco("com.cmcm.live:id/kcoin_num").click()
    time.sleep(3)
    poco(text="Total").click()
    assert_exists(Template("diamond.png"))
    poco("com.cmcm.live:id/img_left").click()


# 点赞 已经点过赞，取消点赞/从未点过赞，点赞
def praise():
    before_click_praise_content = poco("com.cmcm.live:id/tv_likes_num").get_text()
    before_click_praise_amount = int(''.join([i for i in before_click_praise_content if str.isdigit(i)]))
    poco("com.cmcm.live:id/iv_praise").click()
    time.sleep(3)
    after_click_praise_content = poco("com.cmcm.live:id/tv_likes_num").get_text()
    after_click_praise_amount = int(''.join([i for i in after_click_praise_content if str.isdigit(i)]))
    print(after_click_praise_amount)
    if before_click_praise_amount < after_click_praise_amount:
        assert_equal(before_click_praise_amount+1, after_click_praise_amount)
    elif before_click_praise_amount > after_click_praise_amount:
        assert_equal(before_click_praise_amount-1, after_click_praise_amount)


# 分享
def share():
    poco("com.cmcm.live:id/chat_share_command").click()
    assert_exists(Template("share.png"))
    touch(Template("share.png"))
    # 进入Facebook页面后返回
    time.sleep(3)
    poco(type="android.widget.Button").click()
    assert_exists(Template("share.png"))


restart_app()
login_if_needed()

home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('冷启后没有来到主页')
home_page.goto_me_page()
sleep(5)

me_page = MePage()
if not me_page.in_current_page():
    raise AssertionError('进入我的页面失败')
me_page.click_replay_button()


replay_page = ReplayPage()
if not replay_page.in_current_page():
    raise AssertionError('进入回放列表页失败')
replay_page.click_first_replay()


if not poco("com.cmcm.live:id/img_watch_loading_floor").exists():
    raise AssertionError('进入第一个回放失败')
comment()
fast()
pause()
diamond()
praise()
share()

