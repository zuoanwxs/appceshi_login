from Base.Base import Base
import Page

class Login_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name, passwd):
        # 登陆操作
        self.input_element(Page.login_name_id, name)
        self.input_element(Page.login_passwd_id, passwd)
        self.click_element(Page.login_btn_id)
    def login_btn_status(self):
        # 判断登录按钮是否存在
        try:
            self.search_element(Page.login_btn_id)
            return True
        except:
            return False
    def close_login_page(self):
        # 关闭登陆页面
        self.click_element(Page.login_close_page_id)