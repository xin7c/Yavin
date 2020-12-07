# -*- encoding=utf8 -*-
import os
import threading

from airtest.cli.parser import cli_setup
from airtest.core.android.adb import ADB
from poco.drivers.unity3d import UnityPoco
from airtest.core.api import *
from airtest.core.settings import Settings as ST
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from enum import Enum, unique

from config.config import Config
from common.Base.Base import Base


@unique
class Actions(Enum):
    """
    子页面实例拦截动作名称枚举值
    """
    click = "click"
    # find = "find"
    wake = "wake"
    home = "home"


class BasePage(object, metaclass=Base):
    """
    页面基类，用于页面对象类的继承
    对象层
    """

    def __init__(self):
        """
        self.config: 获取配置文件
        self.poco: 获取poco实例
        """
        self.config = Config().get_data
        print(f"device(): {device()}")
        # 检查adb状态
        adb = ADB()
        device_list = adb.devices()
        print(f"device_list: {device_list}")
        device_num = len(device_list) >= 1
        # print(device_list)
        assert_equal(device_num, True, "设备连接数至少>=1")
        # self.device_list = device_list

        # 获取poco实例
        self.poco = AndroidUiautomationPoco(use_airtest_input=True,
                                            screenshot_each_action=False)
        # 获取根目录
        # self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # if not cli_setup():
        #     auto_setup(
        #         basedir=self.root_dir,
        #         devices=self.["android_devices"],
        #         logdir=False
        #     )
        self._setting()
        self.width, self.height = device().get_current_resolution()
        print("[BasePage] init...")
        self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.main_phone = self.config.get("main_phone")
        # auto_setup(basedir=self.root_dir, logdir=True)
        # self.device_list = []
        # for i in range(len(device_list)):
        #     self.device = connect_device(self.main_phone + device_list[i][0])
        #     # print(self.main_phone + device_list[i][0])
        #     self.device_list.append(self.device)
        #     auto_setup(
        #         basedir=self.root_dir,
        #         devices=[self.main_phone + device_list[i][0]],
        #         logdir=True)

    def __getattr__(self, attr):
        """
        扩展属性或方法
        当且仅当无聊或者没有封装完整方法的时候再使用枚举值中的方法！
        :param attr:
        :return:某一个操作元素的方法
        """
        # if not callable(attr):
        #     print(f"unknown attr: {attr}")
        #     # 尝试查找元素
        #     return print(self.config.get("package_name"))
        if attr == Actions.click.value:
            return self.find_click
        elif attr == Actions.wake.value:
            print("唤醒并解锁目标设备")
            return wake
        elif attr == Actions.home.value:
            print("返回HOME界面")
            return home

    def act_click(self, *args):
        print(f'{self.cls_name} @act_click: {str(args[0])}')

    # def set_permission(self):
    #     """Android授权"""
    #     permission = config.Config.get_yaml().get("permission", None)
    #     f = list(set(permission))
    #     print(f)
    #     for i in f:
    #         print(f"adb shell pm grant {self.package_name} {i}")
    #         os.popen(f"adb shell pm grant {self.package_name} {i}")

    def _setting(self):
        """全局设置"""
        ST.FIND_TIMEOUT = 5  # 隐式等待
        ST.FIND_TIMEOUT_TMP = 10  # 隐式等待
        ST.SNAPSHOT_QUALITY = 70  # 图片精度

    def start_app(self):
        """启动app"""
        print(f"准备启动app[{self.package_name}]")
        start_app(self.package_name)
        sleep(2)
        return self

    def stop_app(self):
        """停止app"""
        stop_app(self.package_name)
        return self

    def restart_app(self):
        """重启app"""
        stop_app(self.package_name)
        sleep(2)
        print(f"准备启动app[{self.package_name}]")
        start_app(self.package_name)
        sleep(2)
        return self

    def find(self, *element):
        """基本查找, 可能会抛出异常"""
        if len(element) == 1:
            self.poco(f"{element[0]}").wait_for_appearance(20)
            return self.poco(f"{element[0]}")
        elif len(element) == 2:
            self.poco(f"{element[0]}").child(f"{element[1]}").wait_for_appearance(20)
            return self.poco(f"{element[0]}").child(f"{element[1]}")

    def find_click(self, *element):
        """基本点击，支持链式操作"""
        self.find(*element).click()
        return self

    def find_long_click(self, *element):
        """基本长点击，支持链式操作"""
        self.find(*element).long_click()
        return self

    def find_chirden(self, *element):
        """基本查找子节点所有子节点"""
        return self.find(*element).children()

    def find_text(self, *element):
        """查找当前ui下文字"""
        return self.find(*element).get_text()

    @property
    def screen_size(self):
        """获取当前屏幕尺寸"""
        return self.width, self.height

    def snap(self, msg: str = None):
        """
        默认不填直接截图
        :param msg:描述信息
        :return:支持链式操作
        """
        if msg is not None:
            snapshot(msg=msg)
            return self
        snapshot()
        return self

    def back(self):
        keyevent("BACK")
        print('keyevent(BACK")')
        log('返回按键 keyevent(BACK")',
            timestamp=time.time(),
            desc='返回按键 keyevent(BACK")',
            snapshot=True)
        return self

    def go_me_page(self):
        """
        跳转个人页
        :return: poco
        """
        print('跳转个人页go_me_page')
        self.find_click(Config().get_base_page("ID_ME_PAGE"))
        return self

    def up_swipe(self):
        """上滑"""
        start_pt = (self.width * 0.7, self.height * 0.7)
        end_pt = (self.width * 0.7, self.height * 0.3)
        swipe(start_pt, end_pt)
        return self

    def down_swipe(self):
        """下滑"""
        start_pt = (self.width * 0.7, self.height * 0.3)
        end_pt = (self.width * 0.7, self.height * 0.7)
        swipe(start_pt, end_pt)
        return self

    def left_swipe(self):
        """左滑"""
        start_pt = (self.width * 0.3, self.height / 2)
        end_pt = (self.width * 0.7, self.height / 2)
        swipe(start_pt, end_pt)
        return self

    def right_swipe(self):
        """右滑"""
        start_pt = (self.width * 0.7, self.height / 2)
        end_pt = (self.width * 0.3, self.height / 2)
        swipe(start_pt, end_pt)
        return self

    def up_swipe_tab(self):
        """上滑tab 切换直播间"""
        start_pt = (self.width / 2, self.height * 0.5)
        end_pt = (self.width / 2, self.height * 0.1)
        swipe(start_pt, end_pt)
        return self

    def down_swipe_tab(self):
        """下滑tab 切换直播间"""
        start_pt = (self.width / 2, self.height * 0.1)
        end_pt = (self.width / 2, self.height * 0.5)
        swipe(start_pt, end_pt)
        return self

    def left_swipe_tab(self):
        """左滑tab"""
        start_pt = (self.width * 0.8, self.height / 2)
        end_pt = (self.width * 0.05, self.height / 2)
        swipe(start_pt, end_pt)
        return self

    def right_swipe_tab(self):
        """右滑tab"""
        start_pt = (self.width * 0.05, self.height / 2)
        end_pt = (self.width * 0.8, self.height / 2)
        swipe(start_pt, end_pt)
        return self

    def in_current_page(self):
        pass

    def goto_this(self, from_page=None):
        pass


if __name__ == '__main__':
    b = BasePage()
    devices = Config.get_yaml().get("android_devices", None)
    print(devices)
    print(b.cls_name)
    # b.click("com.cmcm.live:id/me_page")
    # b.restart_app()
    print(b.screen_size)
