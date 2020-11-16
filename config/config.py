#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:config.py
@time:2020/09/21
"""
import subprocess
import sys

import yaml
import os
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
package_name_path = os.path.join(file_path, "package_name.txt")


def page_ele_loc(self, key: str) -> str:
    """
    页面元素定位字符串，可能是id、name、text、xpath等
    将在Base元类中被注入
    :param self: 子类实例
    :param key: 必填 元素str，对应yaml文件中xxxPage下的字段
    :return: 元素str
    """
    # print(f"page_ele_loc {self.__dict__}")
    # 获取配置
    conf = Config()
    # 读取临时文件中的包名
    with open(package_name_path, "r") as f:
        package_name = f.read().strip()
        if package_name:
            pass
        else:
            package_name = conf.get_data.get("package_name", None)
    # package_name = conf.get_data.get("package_name", None)
    page_config_data = conf.get_data.get(self.cls_name, None)
    # print(page_config_data, self.cls_name, package_name, page_config_data.get(key, None))
    # 判断ID前缀，拼接package_name
    if key.startswith("ID_"):
        return ''.join((package_name, page_config_data.get(key, None)))
    return page_config_data.get(key, None)


class Config(object):
    """
    获取配置文件，返回配置字段
    """

    @staticmethod
    def get_yaml(yaml_name: str = "config.yaml") -> any:
        """
        获取当前路径
        current_path = os.path.abspath(".")
        yaml_path = os.path.join(current_path, "config.yaml")
        :return: data = get_data(yaml_path)
        """
        # 打开yaml文件
        # print("***获取yaml文件数据***")
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        # current_path = os.path.abspath(".")
        yaml_file = os.path.join(parent_dir, yaml_name)
        with open(yaml_file, 'r', encoding="utf-8") as file:
            file_data = file.read()
        # 将字符串转化为字典或列表
        yaml_data = yaml.load(file_data, Loader=yaml.FullLoader)
        # print(yaml_data)
        # print("类型：", type(yaml_data))
        return yaml_data

    @property
    def get_package_name(self):
        """
        :return:暴露package_name
        """
        with open(package_name_path, "r") as f:
            package_name = f.read().strip()
            if package_name:
                # print(f"读取txt[{package_name}]")
                pass
            else:
                package_name = self.get_data.get("package_name", None)
        return package_name

    def package_name_dict(self, key: str):
        return self.get_yaml().get('package_name_dict').get(key)

    @property
    def get_data(self):
        """
        获取包名、设备信息
        :return:
        """
        return self.get_yaml()

    def get_base_page(self, element):
        """
        获取包名、设备信息
        :return:
        """
        with open(package_name_path, "r") as f:
            package_name = f.read().strip()
            if package_name:
                # print(f"读取txt[{package_name}]")
                pass
            else:
                package_name = self.get_data.get("package_name", None)
        # package_name = self.get_yaml().get("package_name", None)
        base_page_element = self.get_yaml().get("BasePage", None)[element]
        return ''.join((package_name, base_page_element))

    @property
    def _get_user_device_map(self):
        """
        读取config/devices.yaml
        :return:
        """
        user_device_map = self.get_yaml(yaml_name="devices.yaml")
        return user_device_map.get("user_device_map")

    @property
    def get_devices_list(self):
        """
        读取config/devices.yaml
        :return: config/devices.yaml中的设备号列表
        """
        devices_list = [x for x in self._get_user_device_map]
        return devices_list

    def get_info_by_sn(self, sn: str):
        """
        读取config/devices.yaml
        :param sn: 传入设备号
        :return: 返回字典
        """
        sn_data = self._get_user_device_map.get(sn, None)
        if sn_data is None:
            print("获取设备配置信息为空")
            return None
        info = defaultdict()
        info["login_type"] = sn_data.get("login_type", None)
        info["username"] = sn_data.get("username", None)
        info["password"] = sn_data.get("password", None)
        return info

    @staticmethod
    def get_apk_version(package_name: str) -> str:
        """
        调用adb获取apk版本号
        :example Config.get_apk_version(Config.get_yaml().get("package_name"))
        :param package_name: 比如com.cmcm.live
        :return:
        """
        cmd = [
            "adb",
            "shell",
            "dumpsys",
            "package",
            f"{package_name}",
            "|",
            "grep",
            "versionName",
        ]
        try:
            ret = subprocess.run(cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 check=True)
            if ret.returncode == 0:
                version_name = str(ret.stdout, encoding="utf-8").strip().split("=")[-1]
                print(f"success:[{version_name}]")
                return version_name
            else:
                print(f"error:[{ret}]")
                return "获取apk版本号失败!"
        except subprocess.CalledProcessError as e:
            return f"可能的设备连接错误: {e}"


if __name__ == '__main__':
    print(package_name_path)
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path, "config.yaml")
    data = Config.get_yaml()
    print(f"data ---> {data['HomePage']['username']}")
    print(Config().get_info_by_sn("50354b4659543398").get("username"))
    print(Config().get_devices_list)
    print(Config().get_apk_version(Config.get_yaml().get("package_name")))
    print(Config().get_package_name)
    print(Config().package_name_dict('poplive'))
