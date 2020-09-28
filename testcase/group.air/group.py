# -*- encoding=utf8 -*-
__author__ = "liulili"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco = AndroidUiautomationPoco()

from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import *
poco = UnityPoco()
poco.swipe([0.5,0.9],[0.5,0.2],duration = 0.2)
sleep(4.0)

touch(Template(r"tpl1561456787230.png", record_pos=(-0.008, -0.062), resolution=(1080, 1920)))

sleep(2.0)
#建立群组按钮
#poco("com.cmcm.live:id/my_fam_create_button").click()
touch(Template(r"tpl1561458117174.png", record_pos=(-0.004, -0.291), resolution=(1080, 1920)))
sleep(2.0)

#from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("android:id/list").child("android.widget.FrameLayout")[0].child("com.cmcm.live:id/member_check_in").click()

poco("com.cmcm.live:id/group_invite_btn").click()
sleep(1.0)
assert_exists(Template(r"tpl1561456966985.png", record_pos=(0.006, -0.296), resolution=(1080, 1920)), "群组建立成功.")






