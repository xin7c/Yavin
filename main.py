#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Run Airtest in parallel on multi-device
"""
@author:xuchu
@file:main.py
@time:2020/10/20
"""

import os
import traceback
import subprocess
import arrow
import time
import json
import shutil
from airtest.core.android.adb import ADB
from jinja2 import Environment, FileSystemLoader

file_path = os.path.dirname(os.path.abspath(__file__))


def run(devices, air, run_all=False):
    """"
        run_all
            = True: 从头开始完整测试 (run test fully) ;
            = False: 续着data.json的进度继续测试 (continue test with the progress in data.jason)
    """
    try:
        results = load_json_data(air, run_all)
        tasks = run_on_multi_device(devices, air, results, run_all)
        for task in tasks:
            status = task['process'].wait()
            results['tests'][task['dev']] = run_one_report(task['air'], task['dev'])
            results['tests'][task['dev']]['status'] = status
            json.dump(results, open('data.json', "w"), indent=4)
        run_summary(results)
    except Exception as e:
        traceback.print_exc()


def run_on_multi_device(devices, air, results, run_all):
    """
        在多台设备上运行airtest脚本
        Run airtest on multi-device
    """
    tasks = []
    for dev in devices:
        if (not run_all and results['tests'].get(dev) and
                results['tests'].get(dev).get('status') == 0):
            print("Skip device %s" % dev)
            continue
        log_dir = get_log_dir(dev, air)
        cmd = [
            "airtest",
            "run",
            f"testcase/{air}",
            "--device",
            "Android:///" + dev,
            "--log",
            log_dir
        ]
        try:
            tasks.append({
                'process': subprocess.Popen(cmd, cwd=os.getcwd()),
                'dev': dev,
                'air': air
            })
        except Exception as e:
            print("run_on_multi_device 出错了！！！")
            traceback.print_exc()
    return tasks


def run_one_report(air, dev):
    """"
        生成一个脚本的测试报告
        Build one test report for one air script
    """
    try:
        log_dir = get_log_dir(dev, air)
        log = os.path.join(log_dir, 'log.txt')
        if os.path.isfile(log):
            # airtest report untitled.air --log_root log/ --outfile log/log.html --lang zh --static_root
            # https://host:port/static/css/ --export ./report
            cmd = [
                "airtest",
                "report",
                f"testcase/{air}",
                "--log_root",
                log_dir,
                "--export",
                f"{file_path}/summary_report/html_logs/{dev}",
                "--plugin",
                "poco.utils.airtest.report",
                "--lang",
                "zh"
            ]
            ret = subprocess.call(cmd, cwd=os.getcwd())
            return {
                'status': ret,
                'path': os.path.join(f'html_logs/{dev}/{air.split(".")[0]}.log/', 'log.html')
                # 'path': os.path.join(log_dir, 'log.html')
            }
        else:
            print("Report build Failed. File not found in dir %s" % log)
    except Exception as e:
        traceback.print_exc()
    return {'status': -1, 'device': dev, 'path': ''}


def run_summary(data):
    """"
        生成汇总的测试报告
        Build sumary test report
    """
    try:
        summary = {
            'time': "%.3f" % (time.time() - data['start']),
            'success': [item['status'] for item in data['tests'].values()].count(0),
            'count': len(data['tests'])
        }
        summary.update(data)
        summary['start'] = time.strftime("%Y-%m-%d %H:%M:%S",
                                         time.localtime(data['start']))
        # 存储配置和全局对象，从文件系统或其他位置中加载模板。
        # PackageLoader：包加载器
        # FileSystemLoader：文件系统加载器
        env = Environment(loader=FileSystemLoader(os.getcwd()),
                          trim_blocks=True)
        html = env.get_template('report_tpl.html').render(data=summary)
        summary_report_file_name = data.get("script").split(".")[0]
        # print(summary_report_file_name)
        if "/" in summary_report_file_name:
            dir_name = summary_report_file_name.split("/")[0]
            os.mkdir(f'summary_report/{dir_name}')
            # summary_report_file_name.replace("/", "_")
        _report_time_now = arrow.now().format('YYYYMMDD_HHmmss')
        with open(f'summary_report/{summary_report_file_name}_{_report_time_now}.html', "w", encoding="utf-8") as f:
            f.write(html)
        print("run_summary --- ", data)
    except Exception as e:
        traceback.print_exc()


def load_json_data(air, run_all):
    """"
        加载进度
            如果data.json存在且run_all=False，加载进度
            否则，返回一个空的进度数据
        Loading data
            if data.json exists and run_all=False, loading progress in data.json
            else return an empty data
    """
    json_file = os.path.join(os.getcwd(), 'data.json')
    if (not run_all) and os.path.isfile(json_file):
        data = json.load(open(json_file))
        data['start'] = time.time()
        return data
    else:
        clear_log_dir(air)
        return {
            'start': time.time(),
            'script': air,
            'tests': {}
        }


def clear_log_dir(air):
    """"
        清理log文件夹 log/setting.air
        Remove folder log/setting.air
        每次启动时清空log下的文件夹
    """
    log = os.path.join(os.getcwd(), 'log', air)
    if os.path.exists(log):
        shutil.rmtree(log)


def get_log_dir(device, air):
    """"
        在 setting.air/log/ 文件夹下创建每台设备的运行日志文件夹
        Create log folder based on device name under setting.air/log/
    """
    log_dir = os.path.join(file_path, 'log', air, device.replace(".", "_").replace(':', '_'))
    # print(log_dir, "get_log_dir")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir


if __name__ == '__main__':
    """
        初始化数据
        Init variables here
    """
    devices = [tmp[0] for tmp in ADB().devices()]
    air = 'setting_dir/setting.air'

    # Continue tests saved in data.json
    # Skip scripts that run succeed
    # 基于data.json的进度，跳过已运行成功的脚本
    # run(devices, air)

    # Resun all script
    # 重新运行所有脚本
    run(devices, air, run_all=True)
