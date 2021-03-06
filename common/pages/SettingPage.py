# -*- encoding=utf8 -*
import sys
import os
import logging
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from airtest.core.api import sleep, assert_equal, log
from common.pages.BasePage import BasePage
from config.config import Config


class SettingPage(BasePage):
    """
    逻辑层
    """

    def goto_setting_page(self):
        """
        点击跳转setting页
        :return:
        """
        logging.info("跳转setting页...")
        self.find_click(self.page_ele_loc("ID_SETTINGS_ENTER"))
        # self.poco(self.page_ele_loc("ID_SETTINGS_ENTER")).click()
        sleep(2)
        return self

    def in_current_page(self):
        return self.poco(self.page_ele_loc("ID_SETTINGS_LEFT")).exists() or False

    # ping网络检测
    def goto_network_ping(self):
        """
        ping网络检测 -> Network Diagnosis
        :return:
        """
        self.poco(text=self.page_ele_loc("TEXT_NETWORK_DIAGNOSIS")).click()
        try:
            assert_equal(self.poco(text="Upload diagnosis report").exists(),
                         True,
                         msg='Upload diagnosis report 按钮出现')
            log('网络检测页面截图',
                timestamp=time.time(),
                desc='网络检测页面截图',
                snapshot=True)
        except AssertionError as e:
            log(e,
                timestamp=time.time(),
                desc='Upload diagnosis report 按钮没有出现',
                snapshot=True)
        return self

    def setting_page_instance(self):
        """
        链式调用
        :return:page实例，可以重复操作实例方法
        """
        assert_equal("setting_page_instance", "setting_page_instance", "断言setting_page_instance")
        return self

    def logout(self):
        """
        点击登出按钮，退出账号
        :return:
        """
        logging.info("退出登录...")
        self.go_me_page().goto_setting_page()
        self.up_swipe()
        self.poco(self.page_ele_loc("ID_ITEM_LOGOUT")).click()
        self.poco(self.page_ele_loc("ID_BUTTON1")).click()
        return self


if __name__ == '__main__':
    # print(SettingPage().cls_name)
    # sp = SettingPage()
    # sp.goto_setting_page()
    # print(sp.in_current_page())
    # sp.goto_network_ping()
    # sp.click1("lalala")

    # print(sp.screen_size)
    # sp.right_swipe().left_swipe()
    # print(Config.get_yaml(yaml_name="config.yaml").get("package_name", None) + ':id/setting_img')
    # print(sp.screen_size)
    print(Config().get_package_name)
