#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:run.py
@time:2020/09/24
"""
import multiprocessing
import os

# airtest run testcase/setting.air --device Android://127.0.0.1:5037/CB5A2AE8LW
# airtest run testcase/setting.air --device Android://127.0.0.1:5037/T7G0216117000139

serialno_list = [
    "CB5A2AE8LW",
    "T7G0216117000139"
]


def action(serialno):
    print(serialno)
    os.system(f"airtest run testcase/setting.air --device Android://127.0.0.1:5037/{serialno}")


if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    jobs = []
    for i in serialno_list:
        p = multiprocessing.Process(target=action, args=(i,))
        print('process start')
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
    print('Process close')

