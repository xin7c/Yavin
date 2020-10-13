
from common.app.app_control import *
from common.login.login import login_if_needed
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

restart_app()
login_if_needed()
poco("com.cmcm.live:id/me_page").wait_for_appearance(timeout=4)
poco("com.cmcm.live:id/me_page").click()
# 获取用户等级
user_level_content = poco("com.cmcm.live:id/personal_level_num_tv").get_text()
user_level_digital = int(''.join([i for i in user_level_content if str.isdigit(i)]))
poco.swipe([0.5, 0.8], [0.5, 0.3], duration=0.1)

# 60等级以下 提示toast
if user_level_digital < 60:
    # poco(text="Visitor Records").click()
    touch(Template(r"visitor records.png", record_pos=(-0.319, 0.01), resolution=(1080, 2280)))
    assert_exists(Template(r"unlock_at_60LV.png", record_pos=(0.001, 0.716), resolution=(1080, 2280)), "请填写测试点")

# 大于60级，进入访客记录，进入他人页
if user_level_digital >= 60:
    touch(Template(r"visitor records.png", record_pos=(-0.319, 0.01), resolution=(1080, 2280)))
    time.sleep(3)
    poco("com.cmcm.live:id/following_image").click()
    poco.swipe([0.5, 0.8], [0.5, 0.3], duration=0.1)
    assert_exists(Template(r"others_page.png", record_pos=(0.343, -0.887), resolution=(1080, 2280)), "进入他人页")
















