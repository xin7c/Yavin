#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:config.py
@time:2020/09/21
"""

import yaml
import os
from collections import defaultdict


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
    package_name = conf.get_data.get("package_name", None)
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
        package_name = self.get_yaml().get("package_name", None)
        base_page_element = self.get_yaml().get("BasePage", None)[element]
        return ''.join((package_name, base_page_element))

    @property
    def get_user_device_map(self):
        user_device_map = self.get_yaml(yaml_name="devices.yaml")
        return user_device_map.get("user_device_map")

    def get_info_by_sn(self, sn: str):
        """
        :param sn: 传入设备号
        :return: 返回字典
        """
        sn_data = self.get_user_device_map.get(sn, None)
        if sn_data is None:
            print("获取设备配置信息为空")
            return None
        info = defaultdict()
        info["login_type"] = sn_data.get("login_type", None)
        info["username"] = sn_data.get("username", None)
        info["password"] = sn_data.get("password", None)
        return info


if __name__ == '__main__':
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path, "config.yaml")
    data = Config.get_yaml()
    print(f"data ---> {data['HomePage']['username']}")
    print(Config().get_info_by_sn("50354b4659543398").get("username"))
