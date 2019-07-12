import page
from base.base import Base


class PageLogin(Base):

    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd,pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 组合业务方法
    def page_login(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()