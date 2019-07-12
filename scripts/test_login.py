import os
import sys
sys.path.append(os.getcwd())

from page.page_login import PageLogin
import pytest


def get_data():
    return [("13800001111", "123456"), ("13800001112", "0000")]


class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test_login(self, phone, pwd):
        # 调用登录业务方法
        self.login.page_login(phone, pwd)
