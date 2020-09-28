# -*- encoding=utf8 -*-

__author__ = "liyue"

import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

'''
测试环境获取vid
'''

def getusertoken(uid):

    url = "http://featuremix-qa.live.ksmobile.net/test/getUserToken"
    p = {"uid": uid}

    r = requests.get(url, params=p)
    return r.json().get('token')


def get_vid(uid):
    token_url = "http://featuremix-qa.live.ksmobile.net/test/getUserToken"
    p = {"uid": uid}

    r = requests.get(token_url, params=p)
    token = r.json().get('token')

    url = "http://featuremix-qa.live.ksmobile.net/user/getlive"
    p1 = {"token": token, "uid": uid}
    r1 = requests.get(url, params=p1)

    data = r1.json()["data"]
    vid = data["vid"]
    return vid



