# -*- encoding=utf8 -*-
__author__ = 'wanglimin'
'''进入首页各个tab页面'''
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from common.pages.SearchPage import *
from common.pages.VideoRecorderPage import *
from common.pages.HomePage import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed

poco = AndroidUiautomationPoco()


def videos_record(msg):
    # 进入搜索页面
    poco(SearchPage.HOME_SEARCH_IMG).click()
    sleep(30)
    assert_equal(poco(SearchPage.SEARCH_CONTENT_TAB).exists(), True, msg='进入搜索页面失败')
    if not SearchPage().is_videos_tab_exists():
        raise AssertionError('没有找到对应的videos tab')
    poco(text=SearchPage.VIDEOS_TEXT).click()
    sleep(30)
    assert_equal(poco(VideoRecorderPage.VIDEO_RECORDER_ICON_ID).exists(), True, msg='没有进入到video页面')
    poco(VideoRecorderPage.VIDEO_RECORDER_ICON_ID).click()
    # 开播系统相机权限
    allow_windows = poco(VideoRecorderPage.CAMERA_PERMISSION_BTN_ID)
    for i in range(4):
        if allow_windows:
            allow_windows.click()
            sleep(2)
        else:
            break
    assert_equal(poco(VideoRecorderPage.VIDEO_RECORD_ICON_ID).exists(), True, msg='进入videos录制页面')
    # 录制
    for i in range(3):
        poco(VideoRecorderPage.VIDEO_RECORD_ICON_ID).long_click(5)
    assert_equal(poco(VideoRecorderPage.VIDEO_DELETE_ICON_ID).exists(), True, msg='短视频录制失败s')
    poco(VideoRecorderPage.VIDEO_DELETE_ICON_ID).click()
    sleep(2)
    assert_equal(poco(VideoRecorderPage.VIDEO_BTN_ID).exists(), True, msg='删除片段弹窗delete')
    poco(VideoRecorderPage.VIDEO_BTN_ID).click()
    snapshot(msg='删除一段')
    sleep(2)
    poco(VideoRecorderPage.VIDEO_RECORD_ICON_ID).long_click(3)
    snapshot(msg='重新录制一段')
    poco(VideoRecorderPage.VIDEO_GENERATE_ICON_ID).click()
    sleep(60)
    assert_equal(poco(VideoRecorderPage.VIDEO_PUBLISH_ICON_ID).exists(), True, msg='发布编辑页面')
    poco(VideoRecorderPage.VIDEO_PUBLISH_ICON_ID).click()
    sleep(60)
    assert_equal(poco(VideoRecorderPage.VIDEO_EDIT_OK_ICON_ID).exists(), True, msg='发布分享页面')
    # 输入文本
    text(msg)
    assert_equal(poco(VideoRecorderPage.VIDEO_DESCRIBE_ID).get_text().startswith(msg), True, msg='短视频编辑文案失败')
    poco(VideoRecorderPage.VIDEO_EDIT_OK_ICON_ID).click()
    sleep(3)
    assert_equal(poco(VideoRecorderPage.VIDEO_PUBLISH_PROGRESS_ID).exists(), True, msg='正在发布视频失败')
    sleep(60)
    poco(VideoRecorderPage.VIDEO_BACK_ID).click()
    sleep(2)
    assert_equal(poco(HomePage.HOMEPAGE_LIVE).exists(), True, msg='回到搜索页面失败')


restart_app()
login_if_needed()
videos_record('发布短视频')
