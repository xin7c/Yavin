# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from common.app.config import *
from common.pages.LoginPage import *
from common.pages.HomePage import *
from airtest.core.api import *

poco = AndroidUiautomationPoco()
PKG = package_name


class LoginUser(object):
    def __init__(self, user_name, user_pws):
        self.user_name = user_name
        self.user_pws = user_pws
    
    @staticmethod
    def agreement():
        # 协议界面是否存在
        if poco(text=LoginPage().AGREE_TEXT).exists():
            poco(text=LoginPage().AGREE_TEXT).click()
            sleep(5)
    
    @staticmethod
    def remove_pop_windows():
        sleep(30)
        # 请求地理位置信息弹窗是否存在
        if poco(HomePage().POSITION_ALLOW_BTN_ID).exists():
            poco(HomePage().POSITION_ALLOW_BTN_ID).click()
        sleep(10)
        # 签到弹窗是否存在
        if poco(text=HomePage().CHECK_IN_TEXT).exists():
            poco(text=HomePage().CHECK_IN_TEXT).click()
            sleep(5)
            poco(HomePage().CHECK_IN_RESULT_CLOSE_ID).click()
        # 新签到
        if poco(HomePage().CHECK_IN_RESULT_CLOSE_AR_ID).exists():
            poco(HomePage().CHECK_IN_RESULT_CLOSE_AR_ID).click()
            sleep(2)
        # 新签到
        if poco(HomePage().CHECK_IN_RESULT_CLOSE_NEW_ID).exists():
            poco(HomePage().CHECK_IN_RESULT_CLOSE_NEW_ID).click()

    def phone_login(self):
        # 协议界面是否存在
        self.agreement()
        if poco(text=LoginPage.PHONE_TEXT).exists():
            poco(text=LoginPage.PHONE_TEXT).click()
            sleep(5)
            if poco(LoginPage.CLEAR_ID).exists():
                poco(LoginPage.CLEAR_ID).click()
            sleep(2)
            
            # 选择+86区号
            if poco(LoginPage.COUNTRY_CODE_ID).get_text() != LoginPage.CHINA_PHONE_CODE_TEXT:
                poco(LoginPage.COUNTRY_CODE_ID).click()
                for i in range(30):
                    if poco(text=LoginPage.CHINA_TEXT).exists():
                        print("找到了。。。。。")
                        # poco(text = "+ 86").click()# 识别不到+86
                        poco(text=LoginPage.CHINA_TEXT).click()
                        break
                    else:
                        print("没有找到")
                        poco.swipe([0.5, 0.9], [0.5, 0.1])
            print("开始输入手机号...")
            text(self.user_name)
            sleep(5)
            poco(LoginPage.NEXT_BTN_ID).click()
            sleep(10)
            print("开始输入密码...")
            text(self.user_pws)
            sleep(2)
            poco(LoginPage.NEXT_BTN_ID).click()
            sleep(30)
            self.remove_pop_windows()

    def email_login(self):
        # 协议界面是否存在
        self.agreement()
        # 图片不能用poco
        if exists(Template("login_more_icon.png")):
            touch(Template("login_more_icon.png"))
        assert_exists(Template("login_mail_icon.png"), '没有看到email登录入口')
        touch(Template("login_mail_icon.png"))
        if poco(LoginPage().CLEAR_ID).exists():
            poco(LoginPage().CLEAR_ID).click()
        text(self.user_name)
        sleep(2)
        poco(LoginPage().NEXT_BTN_ID).click()
        sleep(20)
        text(self.user_pws)
        poco(LoginPage().NEXT_BTN_ID).click()
        sleep(30)
        # 调用remove_pop_windows方法
        self.remove_pop_windows()

    def google_login(self):
        # 协议界面是否存在
        self.agreement()
        if poco(text=LoginPage().GOOGLE_TEXT).exists():
            poco(text=LoginPage().GOOGLE_TEXT).click()
            sleep(20)
        else:
            print('找更多按钮，找到google入口')
        assert poco(LoginPage().GOOGLE_MAIN_TITLE_ID).get_text() == LoginPage.GOOGLE_MAIN_TITLE_TEXT, '进入google账号页面失败'
        # 计算有几个账号之前已经登录过google
        account_name_list = poco(LoginPage.GOOGLE_ACCOUNT_NAME_ID)
        print(account_name_list)
        len1 = len(account_name_list)
        print(len1)
        list1 = []
        for i in range(len(account_name_list)):
            list1.append(account_name_list[i].get_text())
            print(list1)
        # 判断账号是否之前登录过google
        if self.user_name in list1:
            j = list1.index(self.user_name)
            account_name_list[j].click()
            sleep(40)
        else:
            # 点击使用其他账号
            poco(LoginPage.GOOGLE_ACCOUNT_NEW_ID).click()
            sleep(90)
            print('点击了')
            # 点击输入框
            poco(LoginPage.GOOGLE_ACCOUNT_INPUT_ID).click()
            sleep(10)
            # 输入用户名
            text(self.user_name)
            sleep(40)
            # assert poco(LoginPage.GOOGLE_ACCOUNT_INPUT_ID).get_text() == self.user_name, '输入账号失败请检查'
            sleep(30)
            print('用户名输入成功，进到输入密码页了####')
            # 输入密码
            # poco('identifierId').click()
            text(self.user_pws)
            sleep(50)
            poco(LoginPage.GOOGLE_ACCOUNT_AGREE_ID).click()
            sleep(60)
        # 调用remove_pop_windows方法
        self.remove_pop_windows()

    def twitter_login(self):
        # 协议界面是否存在
        self.agreement()
        # 图片不能用poco
        if exists(Template('login_twitter_icon.png')):
            touch(Template('login_twitter_icon.png'))
        else:
            touch(Template("login_more_icon.png"))
            touch(Template('login_twitter_icon.png'))
        sleep(20)
        # 进入Twitter第三方登录页面输入用户名和密码
        assert poco('username_or_email').exists(), '没有进入到Twitter第三方登录页面'
        poco('username_or_email').click()
        sleep(1)
        text(self.user_name)
        sleep(5)
        poco(name='android.widget.EditText')[1].click()
        sleep(2)
        text(self.user_pws)
        sleep(2)
        # poco(text = 'Log in').click()
        sleep(10)
        poco('allow').click()
        sleep(30)
        # 调用remove_pop_windows方法
        self.remove_pop_windows()
    
    def instagram_login(self):
        ## 协议界面是否存在
        self.agreement()
        # 图片不能用poco
        if exists(Template('login_instagram_icon.png')):
            touch(Template('login_instagram_icon.png'))
        else:
            touch(Template("login_more_icon.png"))
            touch(Template('login_instagram_icon.png'))
        sleep(30)
        poco(text="Phone number, username, or email").click()
        sleep(1)
        text(self.user_name)
        sleep(5)
        assert_equal(poco(text="Phone number, username, or email").get_text(), self.user_name, msg='用户名输入失败')
        sleep(10)
        poco.click([0.5, 0.7])
        poco(text="Password").click()
        sleep(2)
        text(self.user_pws)
        sleep(30)
        self.remove_pop_windows()
