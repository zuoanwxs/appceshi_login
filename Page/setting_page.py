from Base.Base import Base
import Page, time

class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_logout_btn(self, tag=1):
        """
        :param tag: 1 退出 0 取消
        :return:
        """
        time.sleep(3)
        # 向上滑动屏幕
        self.screen_scroll()
        # 点击退出按钮
        self.click_element(Page.logout_btn_id)
        # 点击确认退出按钮
        if tag:
            self.click_element(Page.confirm_logout_btn_id)

