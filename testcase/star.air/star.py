# -*- encoding=utf8 -*-
__author__ = "meizhuo"
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from airtest.core.api import *
from common.app.app_control import restart_app
from common.login.login import login_if_needed
from common.popup.videoplayer import videoplayer_popup_handler
from common.popup.featurelist_popup import featurelist_popup_window

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 星光case
def Star():
    # 关闭活动闪屏
    if poco("com.cmcm.live:id/new_activity_back").exists():
        poco("com.cmcm.live:id/new_activity_back").click()

    # 进入首页第一个直播间，因为第一个位置用户经常变，当红榜tab
    poco(name="com.cmcm.live:id/left_label_txt")[0].click()
    sleep(10)
    # 调用view_live()
    view_live()

    # 关闭关注引导
    if poco("com.cmcm.live:id/img_follow").exists():
        poco("com.cmcm.live:id/img_follow").click()

    #美国主播没有入口+其他直播间干扰
    sleep(5)
    if poco("com.cmcm.live:id/star_mission_img").exists():
        # 点击星光入口，开发H5页面，点击送礼按钮
        poco("com.cmcm.live:id/star_mission_img").click()
        sleep(10)
        touch(Template("send_star.png"))
        # 送一个星光礼物
        poco("com.cmcm.live:id/gift_send_btn_grade").click()
        sleep(5)

        # 检查消耗的星光数
        poco.click([0.5,0.5])

        # 再点击进入星光任务页面
        poco("com.cmcm.live:id/star_mission_img").click()
        sleep(10)
        if exists(Template("claim_button.png")):
            poco(text="Claim").click()
            print("点击进入任务页面")
            sleep(5)
            if exists(Template("CLAIM.png")):
                # 点击领取星光
                for i in poco(text = "CLAIM"):
                    print(i)
                    poco(text="CLAIM").click()
                    print("领取成功")
                    time.sleep(5)
            else:
                print('没有星光可以领取')

            # 星光任务界面送礼联动
            touch(Template("send_star.png"))
            sleep(5)
            # 检验用户消耗星光数值
            star_num = poco("com.cmcm.live:id/star_info_tv").get_text()
            print("送之前星光储值" + star_num)
            sleep(5)

            poco("com.cmcm.live:id/gift_send_btn_grade").click()

            # 检验用户消耗星光数值
            new_star_num = poco("com.cmcm.live:id/star_info_tv").get_text()
            print("送之后的星光储值" + new_star_num)
            sleep(5)

            assert_not_equal(star_num, new_star_num + str(10), "星光送礼失败")

            # 退出直播间
            poco("com.cmcm.live:id/img_close").click()
        elif exists(Template("check_button.png")):
            poco(text="Check").click()
            touch(Template("send_star.png"))
            poco("com.cmcm.live:id/gift_send_btn_grade").click()
            poco.click([0.5,0.5])
            # 退出直播间
            poco("com.cmcm.live:id/img_close").click()
    else:
        raise AssertionError('没有找到星光入口')



#关闭直播间内测宝箱
@videoplayer_popup_handler
def view_live():
    if poco(text='Follow and get notified when the broadcast starts').exists():
        poco(text='Follow and get notified when the broadcast starts').click()
        sleep(2)
    # assert poco('com.cmcm.live:id/anchor_nickname').exists(), '进入直播播放页面成功'


restart_app()
login_if_needed()
featurelist_popup_window()
Star()
