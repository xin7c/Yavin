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


# TODO 采用zk的目的：是否可以通过修改zk的配置来触发切换package_name的操作？

class KazooCli(object):

    def __init__(self):
        # self.zk = KazooClient(hosts='127.0.0.1')
        self.zk = KazooClient(hosts='10.61.153.83:2182')
        self.zk.start()  # 与zookeeper连接

    def func_cb(self, data, stat, event):
        print(self.zk.state)
        # print(args)
        print(data, stat, event)
        if event is not None:
            print(f"节点 [{event.path}]变更： #类型 {event.type} #状态 {event.state}")
        # print(f"Data is {data}")
        # print(f"Version is {stat.version}")
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
        # self.zk.ensure_path("/cc")
        try:
            self.zk.create("/yavin/package_name", b"com.cmcm.live", makepath=True)
        except NodeExistsError as e:
            print(e, "创建节点已存在")
        print(self.zk.get("/yavin/package_name"))
        node = self.zk.get_children('/')
        print(node)

    def get_children(self, path: str) -> list:
        """
        获取路径子节点
        :param path: "/cc"
        :return: children list
        """
        res = self.zk.create("/cc/del_", b"add", ephemeral=True, sequence=True, makepath=True)[4:]
        print(res)
        time.sleep(1)
        children = self.zk.get_children(path)
        print(children, res)
        if res < max(children):
            print("拿锁失败")
        else:
            print("成功获取锁！")
            b = self.zk.delete("/cc/" + res)
            print(f"删除节点，释放锁{b}")
        return children

    def stop(self):
        self.zk.stop()


if __name__ == '__main__':
    kc = KazooCli()
    # kc.start()

    try:
        print(kc.zk.get_children("/cc"))
        watcher = DataWatch(kc.zk, "/cc/del_0000000151", kc.func_cb)
        while True:
            time.sleep(30)
    except Exception as e:
        print(e)
        kc.zk.stop()
    # kc.unlock()
    # kc.get_lock()
    kc.get_children("/cc")
    # kc.stop()
