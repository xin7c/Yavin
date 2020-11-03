#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:run.py
@time:2020/11/03
"""

# airtest run testcase/setting.air --log log/
# airtest report testcase/setting.air --log_root log/ --export ~/Downloads/ --plugin poco.utils.airtest.report
import os
import subprocess
from config.config import Config
import argparse


def run():
    """
    无法直接运行，必须在项目根目录下使用命令行参数！
    命令行参数 -c | -p | -h
    """
    parser = argparse.ArgumentParser(
        description='请提供case名和包名~',
        prog='Yavin启动脚本',
        usage='case名默认setting.air | 包名必填:[liveme | pro | poplive | Frill]',
        epilog='有问题请联系xuchu@joyme.sg'
    )
    parser.add_argument('-c', '--case', dest='case', type=str, default='setting.air', help='测试用例名字.air')
    parser.add_argument('-p', '--packagename', dest='packagename',
                        type=str, required=True,
                        help='包名[liveme | pro | poplive | Frill]')
    args = parser.parse_args()

    package_name_dict = Config.get_yaml().get("package_name_dict", None)

    # TODO 拉取apk

    # TODO 安装apk

    # TODO 解析apk包名

    # TODO 写入文件是否线程安全？
    if args.packagename not in package_name_dict.keys():
        raise KeyError("传入包名未知，请不要瞎写！")
    with open("package_name.txt", "w+") as f:
        f.write(package_name_dict[args.packagename])
    cmd = [
        "airtest",
        "run",
        f"testcase/{args.case}",
        "--log",
        "log/"
    ]
    ret = subprocess.call(cmd, cwd=os.getcwd())
    if ret == 0:
        print("看起来执行成功了呢")


if __name__ == '__main__':
    run()
