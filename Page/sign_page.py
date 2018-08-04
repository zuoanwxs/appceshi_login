from Base.Base import Base
import Page

class Sign_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_accout(self):
        # 点击注册页面已有账号
        self.click_element(Page.exits_account_id)