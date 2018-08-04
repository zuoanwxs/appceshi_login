from Base.Base import Base
import Page

class Home_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        # 点击下方菜单栏我按钮
        self.click_element(Page.my_btn_id)