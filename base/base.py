from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'
        # 获取driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):  # loc类型：列表或元组
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(loc[0], loc[1]))

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()
