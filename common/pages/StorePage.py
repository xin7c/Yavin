# -*- encoding=utf8 -*-
from common.pages.BasePage import BasePage
from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class StorePage(BasePage):
    WIDGET_MALL_IMG = 'com.cmcm.live:id/mall_product_img'
    WIDGET_LUCK_DRAW_BTN = "com.cmcm.live:id/market_tab_tv_lottery"
    HISTORY_BTN = 'Reward Record'
    BAG_BTN = "com.cmcm.live:id/market_top_package"
    TEXT_SUM_MONEY = "com.cmcm.live:id/my_coin_tv"
    TEXT_DRAW_FIRST_PRICE = "com.cmcm.live:id/draw_one"

    def in_current_page(self):
        if not poco(self.WIDGET_MALL_IMG).exists():
            return True
        else:
            return False

    # 背包
    def go_bag(self):
        poco(self.BAG_BTN).click()

    # 历史记录
    def go_history(self):
        poco(text=self.HISTORY_BTN).click()

    def get_sum_money(self):
        sum_money = int(poco(self.TEXT_SUM_MONEY)[0].get_text())
        return sum_money

    def first_price(self):
        first_content = poco(self.TEXT_DRAW_FIRST_PRICE)[0].get_text()
        first_price = int(''.join([i for i in first_content if str.isdigit(i)]))
        return first_price

    def click_luck_draw_coin(self):
        poco(self.WIDGET_LUCK_DRAW_BTN).click()

    def click_draw_first_price(self):
        poco(self.TEXT_DRAW_FIRST_PRICE)[0].click()

