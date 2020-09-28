# -*- encoding=utf8 -*-
__author__ = "zhangleilei"
from common.app.app_control import *
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

restart_app()
login_if_needed()
poco("com.cmcm.live:id/me_page").wait_for_appearance(timeout=4)
poco("com.cmcm.live:id/me_page").click()


def myselfpage_scroll():
    for i in range(4):
        sleep(2)
        poco.scroll(direction="vertical", percent=1, duration=2)


# fans
poco("com.cmcm.live:id/personal_fans_count_tv").click()
myselfpage_scroll()
poco("com.cmcm.live:id/search_content").set_text("xiaoBR")
poco("com.cmcm.live:id/search_name").wait_for_appearance(timeout=8)
assert poco("com.cmcm.live:id/search_name").exists()
if exists(Template("unfollowed.png")):
    poco("com.cmcm.live:id/search_follow").click()
    sleep(3)
    assert_exists(Template("followed.png"))
elif exists(Template("followed.png")):
    poco("com.cmcm.live:id/search_follow").click()
    sleep(3)
    assert_exists(Template("unfollowed.png"))

poco("com.cmcm.live:id/search_image").click()
assert poco("com.cmcm.live:id/img_share").exists()
poco("com.cmcm.live:id/img_back").click()
poco("com.cmcm.live:id/img_left").click()

# following
poco("com.cmcm.live:id/personal_followings_count_tv").click()
myselfpage_scroll()
poco("com.cmcm.live:id/search_content").set_text("zllf")
poco("com.cmcm.live:id/search_name").wait_for_appearance(timeout=8)
assert poco("com.cmcm.live:id/search_name").exists()
poco("com.cmcm.live:id/search_image").click()
assert poco("com.cmcm.live:id/img_share").exists()
# 返回个人页
poco("com.cmcm.live:id/img_back").click()
poco("com.cmcm.live:id/img_left").click()
sleep(2)

# 历史记录
poco.swipe([0.5, 0.6], [0.5, 0.1], duration=0.1)
poco(text="History").click()
poco("com.cmcm.live:id/footprints_follow").wait_for_appearance(timeout=8)
poco("com.cmcm.live:id/footprints_name").click()
sleep(3)
# 断言进入他人页
assert poco("com.cmcm.live:id/img_share").exists()
poco("com.cmcm.live:id/img_back").click()
myselfpage_scroll()
poco("com.cmcm.live:id/custom_title_back_frame").click()
assert poco("com.cmcm.live:id/me_page").exists()

