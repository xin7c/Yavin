# -*- encoding=utf8 -*-
__author__ = 'wanglimin'

from poco.drivers.android.uiautomation import *
poco = AndroidUiautomationPoco()


class LoginPage(object):
    AGREE_TEXT = "Agree"
    PHONE_TEXT = "PHONE"
    GOOGLE_TEXT = 'GOOGLE'
    # 底部登录按钮父节点和本级的节点
    THIRD_LOGIN_FATHER_ID = 'com.cmcm.live:id/bottom_login_layout'
    THIRD_LOGIN_NAME = 'android.widget.ImageView'
    # 更多按钮
    # LOGIN_MORE = poco(THIRD_LOGIN_FATHER_ID).child(name=THIRD_LOGIN_NAME)[2]
    CLEAR_ID = "com.cmcm.live:id/iv_clear"
    
    '''
    Phone相关
    '''
    COUNTRY_CODE_ID = "com.cmcm.live:id/tv_country_code"
    CHINA_PHONE_CODE_TEXT = "+ 86"
    CHINA_TEXT = "中国"
    NEXT_BTN_ID = "com.cmcm.live:id/btnTv"
    '''
       GOOGLE相关
    '''
    GOOGLE_TEXT = 'GOOGLE'
    GOOGLE_MAIN_TITLE_ID = 'com.google.android.gms:id/main_title'
    GOOGLE_MAIN_TITLE_TEXT = "Choose an account"
    GOOGLE_ACCOUNT_NAME_ID = 'com.google.android.gms:id/account_name'
    GOOGLE_ACCOUNT_NEW_ID = 'com.google.android.gms:id/add_account_chip_title'
    GOOGLE_ACCOUNT_INPUT_ID = 'identifierId'
    GOOGLE_ACCOUNT_AGREE_ID = 'signinconsentNext'
    '''
        instagram相关
    '''
    
    
    
    
    
    
    
    




