# -*- encoding=utf8 -*-
__author__ = "zhangleilei"

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from common.app.app_control import *
from common.login.login import login_if_needed
from common.pages.HomePage_old import HomePage
from common.pages.MePage import MePage
from common.pages.StorePage import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def draw(page):
    page.click_luck_draw_coin()
    sum_money = page.get_sum_money()
    first_price = page.first_price()
    if sum_money >= 20:
        page.click_draw_first_price()
        sleep(4)
        assert_exists(Template("draw_result.png"), " draw end")
        # 关闭充值成功弹框,获得当前余额
        poco("com.cmcm.live:id/draw_result_ok").click()
        current_money = page.get_sum_money()
        # 余额是不是正确
        assert_equal(sum_money-first_price, current_money, "the coin is correct")
    else:
        assert_exists(Template("no_enough_money.png"), "the sum_money is not enough ")


# 背包
def go_bag():
    poco("com.cmcm.live:id/market_top_package").click()
    assert poco(text='My Bag').exists()
    poco("com.cmcm.live:id/mybag_back").click()
    sleep(3)


# 历史记录
def go_history():
    poco(text='Reward Record').click()
    poco.scroll()
    assert poco(text='Luck Draw Records').exists()
    poco("com.cmcm.live:id/left_area").click()


restart_app()
login_if_needed()

home_page = HomePage()
if not home_page.in_current_page():
    raise AssertionError('冷启后没有来到主页')
home_page.goto_me_page()
sleep(7)

me_page = MePage()
if not me_page.in_current_page():
    raise AssertionError('进入我的页面失败')
me_page.click_Store_button()

store_page = StorePage()
if not store_page.in_current_page():
    raise AssertionError('进入store页面失败')

draw(store_page)


# 背包
store_page.go_bag()
time.sleep(5)
assert_equal(poco(text='My Bag').exists(), True)
poco("com.cmcm.live:id/mybag_back").click()
sleep(2)

#历史记录

store_page.go_history()
time.sleep(5)
assert_equal(poco(text='Luck Draw Records').exists(), True)

