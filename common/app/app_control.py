# -*- encoding=utf8 -*-

from airtest.core.api import *
from common.app.config import *


def restart_app():
    stop_app(package_name)
    sleep(2)
    start_app(package_name)
    sleep(8)
