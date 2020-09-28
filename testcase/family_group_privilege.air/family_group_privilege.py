# -*- encoding=utf8 -*-
__author__ = "meizhuo"

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from common.app.app_control import restart_app
from common.popup.featurelist_popup import featurelist_popup_window
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def privilege_page():
    # 进入个人页
    poco("com.cmcm.live:id/me_page").click()
    sleep(5)
    assert poco('com.cmcm.live:id/setting_img').exists(), '进入个人页面'
    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.2)
    sleep(1)
    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.2)
    time.sleep(5)
    poco(text='My FAM').click()
    time.sleep(10)
    assert poco('com.cmcm.live:id/title_left').get_text() == 'My FAM', '进入我的群组页面'
    if poco("com.cmcm.live:id/my_fam_list_item_my_group_host_img").exists():
        for i in poco("com.cmcm.live:id/my_fam_list_item_my_group_host_img"):
            i.click()
            time.sleep(10)
            if poco("com.cmcm.live:id/recycler_view").exists():
                poco("com.cmcm.live:id/letter_chat_group_setup").click()
                sleep(5)
                assert poco('com.cmcm.live:id/group_info_img').exists(), '进入家族设置页面'
                # 进入家族特权页面
                poco('com.cmcm.live:id/txt_badge').click()
                sleep(5)
                snapshot(msg='家族特权页面')
                # poco(text='Silver Clan').click()
                snapshot(msg='Silver Clan页面')
                poco(text='Gold Clan').click()
                sleep(2)
                snapshot(msg='Gold Clan页面')
                poco(text='Silver Tribe').click()
                sleep(2)
                snapshot(msg='Silver Tribe页面')
                poco(text='Gold Tribe').click()
                sleep(2)
                snapshot(msg='Gold Tribe页面')
                poco.swipe([0.6, 0.15], [0.2, 0.15], duration=0.5)
                sleep(2)
                poco(text='Silver Dynasty').click()
                snapshot(msg='Silver Dynasty页面')
                break
            else:
                poco('com.cmcm.live:id/img_left_group').click()
                sleep(2)
                assert poco('com.cmcm.live:id/title_left').get_text() == 'My FAM', '进入我的群组页面'
    else:
        raise AssertionError('没有加入任何家族')


restart_app()
login_if_needed()
featurelist_popup_window()
privilege_page()


