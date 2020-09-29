#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:zkTools.py
@time:2020/09/29
"""
# /usr/local/Cellar/zookeeper/3.6.2/bin

import os
import subprocess
import time

from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsError, NoNodeError
from kazoo.recipe.watchers import DataWatch


class KazooCli(object):

    def __init__(self):
        # self.zk = KazooClient(hosts='127.0.0.1')
        self.zk = KazooClient(hosts='10.61.153.83')
        self.zk.start()  # 与zookeeper连接

    def func_cb(self, data, stat):
        print(self.zk.state)
        print(f"Data is {data}")
        print(f"Version is {stat.version}")
        # # res = subprocess.call(['git', data])
        # print(f"命令行执行结果[{res}]")

    def get_lock(self, path="lock"):
        try:
            res = self.zk.create(path, b"l0")
            print(f"创建节点成功[{res}]")

        except NodeExistsError as e:
            print("节点已存在，无法创建")
            print(e)

    def unlock(self, path="lock"):
        try:
            res = self.zk.delete(path)
            print(f"删除节点成功[{res}]")
        except NoNodeError as e:
            print("节点不存在，删空气呢")
            print(e)

    def start(self):
        node = self.zk.get_children('/')
        print(node)

    def stop(self):
        self.zk.stop()


# TODO 是否可以通过修改zk的配置来触发切换package_name的操作？
if __name__ == '__main__':
    kc = KazooCli()
    kc.start()
    # try:
    #     watcher = DataWatch(kc.zk, "/yavin/package_name", kc.func_cb)
    #     while True:
    #         time.sleep(1)
    # except Exception as e:
    #     print(e)
    #     kc.zk.stop()

    kc.unlock()
    kc.get_lock()
    kc.stop()
