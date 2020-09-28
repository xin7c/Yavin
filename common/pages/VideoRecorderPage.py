# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
from airtest.core.api import *
poco = AndroidUiautomationPoco()


class VideoRecorderPage(BasePage):
    
    # video按钮
    VIDEO_RECORDER_ICON_ID = 'com.cmcm.live:id/video_record'
    # 相机权限
    CAMERA_PERMISSION_BTN_ID = 'com.android.packageinstaller:id/permission_allow_button'
    # 短视频录制按钮
    VIDEO_RECORD_ICON_ID = 'com.cmcm.live:id/img_record'
    # 删除录制的一段视频按钮
    VIDEO_DELETE_ICON_ID = 'com.cmcm.live:id/view_revoke'
    # 删除视频确认按钮
    VIDEO_BTN_ID = 'com.cmcm.live:id/button1'
    # 短视频生成按钮
    VIDEO_GENERATE_ICON_ID = 'com.cmcm.live:id/view_generate'
    # 短视频发布按钮
    VIDEO_PUBLISH_ICON_ID = 'com.cmcm.live:id/img_publish'
    # 短视频编辑页面OK按钮
    VIDEO_EDIT_OK_ICON_ID = 'com.cmcm.live:id/tv_ok'
    # 短视频发布文案编辑区域
    VIDEO_DESCRIBE_ID = 'com.cmcm.live:id/et_describe'
    # 短视频发布进度条
    VIDEO_PUBLISH_PROGRESS_ID = 'com.cmcm.live:id/video_short_progress'
    # 短视频页面返回按钮
    VIDEO_BACK_ID = 'com.cmcm.live:id/img_left'
