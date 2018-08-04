from Base.Base import Base
import Page

class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def get_all_order_status(self):
        # 判断全部订单是否存在
        try:
            self.search_element(Page.all_order_xpath)
            return True
        except:
            return False

    def click_setiing_btn(self):
        # 点击设置按钮
        self.click_element(Page.setting_btn_id)