
from appium import webdriver

# def init_driver(package, activity):
def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 获取toast消息
    desired_caps['automationName'] = 'Uiautomator2'
    # 设置是否重置应用 默认为false-重置应用   true 不重置应用
    desired_caps['noReset'] = True
    # app的信息
    desired_caps['appPackage'] = "com.yunmall.lc"
    desired_caps['appActivity'] = "com.yunmall.ymctoc.ui.activity.MainActivity"
    # 设置中文输入
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
