# -*- encoding=utf8 -*
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from airtest.core.api import sleep, assert_equal, text
from common.pages.BasePage import BasePage
from common.pages.SettingPage import SettingPage


class LoginPage(BasePage):
    """
    逻辑层
    """
    def agreement(self):
        """
        协议界面是否存在
        """
        if self.poco(text=self.page_ele_loc("TEXT_AGREE")).exists():
            self.poco(text=self.page_ele_loc("TEXT_AGREE")).click()

    def email_login(self):
        """
        邮箱登录
        :return:
        """
        # 协议界面是否存在
        self.agreement()

        buttom_login_layout_more = self.poco(self.page_ele_loc("ID_BOTTOM_LOGIN_LAYOUT")).child(name=self.page_ele_loc("NAME_ANDROID_WIDGET_IMAGEVIEW"))

        if len(buttom_login_layout_more) == 3:
            # 点击【MORE】按钮
            self.poco(self.page_ele_loc("ID_BOTTOM_LOGIN_LAYOUT")).child(name=self.page_ele_loc("NAME_ANDROID_WIDGET_IMAGEVIEW"))[2].click()
        else:
            pass

        # 点击邮箱登录
        self.poco(self.page_ele_loc("ID_BOTTOM_LOGIN_LAYOUT")).child(
            name=self.page_ele_loc("NAME_ANDROID_WIDGET_IMAGEVIEW"))[3].click()

        #输入用户名密码
        if self.poco(self.page_ele_loc("ID_IV_CLEAR")).exists():
            self.poco(self.page_ele_loc("ID_IV_CLEAR")).click()
        self.poco(self.page_ele_loc("ID_ET_EMAIL")).click()
        self.poco(self.page_ele_loc("ID_ET_EMAIL")).set_text("callmegood@fluxer.tv")

        self.poco(self.page_ele_loc("ID_BTNTV")).click()
        self.poco(self.page_ele_loc("ID_ET_PASSWORD")).click()
        self.poco(self.page_ele_loc("ID_ET_PASSWORD")).set_text("Love?cat:dog")
        self.poco(self.page_ele_loc("ID_BTNTV")).click()

        self.remove_pop_windows()

    def iphone_login(self):
        """
        手机号登录
        :return:
        """
        self.agreement()
        if self.poco(text=self.page_ele_loc("TEXT_PHONE")).exists():
            self.poco(text=self.page_ele_loc("TEXT_PHONE")).click()
            if self.poco(self.page_ele_loc("ID_IV_CLEAR")).exists():
                self.poco(self.page_ele_loc("ID_IV_CLEAR")).click()

            # 选择+86区号
            if self.poco(self.page_ele_loc("ID_TV_COUNTRY_CODE")).get_text() != self.page_ele_loc("TEXT_CHINA_PHONE_CODE"):
                self.poco(self.page_ele_loc("ID_TV_COUNTRY_CODE")).click()
                for i in range(30):
                    if self.poco(text=self.page_ele_loc("TEXT_CHINA")).exists():
                        logging.info("找到了。。。。。")
                        self.poco(text=self.page_ele_loc("TEXT_CHINA")).click()
                        break
                    else:
                        logging.info("没有找到")
                        self.up_swipe()

            logging.info("开始输入手机号...")
            self.poco(self.page_ele_loc("ID_ET_PHONE")).set_text("13466367252")
            self.poco(self.page_ele_loc("ID_BTNTV")).click()
            logging.info("开始输入密码...")
            self.poco(self.page_ele_loc("ID_ET_PASSWORD")).set_text("Liuxm2019!")
            self.poco(self.page_ele_loc("ID_BTNTV")).click()

            self.remove_pop_windows()

    def remove_pop_windows(self):

        # 每日奖励签到弹窗
        sleep(10)
        if self.poco(self.page_ele_loc("ID_CHECK_IN_CLOSE")).exists():
            self.poco(self.page_ele_loc("ID_CHECK_IN_CLOSE")).click()


if __name__ == '__main__':
    print(LoginPage().cls_name)
    login_obj = LoginPage()
    login_obj.restart_app()

    # login_obj.email_login()
    login_obj.iphone_login()

    setting_obj = SettingPage()
    setting_obj.logout()

