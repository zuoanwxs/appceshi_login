from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.screen_size = self.driver.get_window_size()
    def search_element(self, loc, timeout=15, poll=1):
        """
        定位单个元素
        :param loc: 元祖类型(定位类型，属性值) 例：(By.ID,"ID属性值")
        :timeout: 搜索超时时间
        :poll: 搜索间隔
        :return: 返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=15, poll=1):
        """
        定位单个元素
        :param loc: 元祖类型(定位类型，属性值) 例：(By.ID,"ID属性值")
        :timeout: 搜索超时时间
        :poll: 搜索间隔
        :return: 返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll=1):
        """
        点击元素
        :param loc: 元祖类型(定位类型，属性值) 例：(By.ID,"ID属性值")
        :return:
        """
        self.search_element(loc, timeout, poll).click()

    def input_element(self, loc, text, timeout=15, poll=1):
        """
        输入内容
        :param loc: 元祖类型(定位类型，属性值) 例：(By.ID,"ID属性值")
        :param text: 输入内容
        :param timeout:
        :param poll:
        :return:
        """
        input_text = self.search_element(loc, timeout, poll)
        input_text.clear()
        input_text.send_keys(text)

    def screen_scroll(self, tag=1):
        """
        向上 向下滑动屏幕 ('width', 'height')
        :param tag: 1 向上滑动 2 向下滑动 3 向左 4 向右
        :return:
        """
        if tag == 1:
            # 屏幕向上滑动
            self.driver.swipe(self.screen_size.get("width") * 0.5,self.screen_size.get("height") * 0.8,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.3)
        elif tag == 2:
            # 屏幕向下滑动
            self.driver.swipe(self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.3,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.8)
        elif tag == 3:
            # 屏幕向左滑动
            self.driver.swipe(self.screen_size.get("width") * 0.8, self.screen_size.get("height") * 0.5,
                              self.screen_size.get("width") * 0.3, self.screen_size.get("height") * 0.5)
        else:
            # 屏幕向下滑动
            self.driver.swipe(self.screen_size.get("width") * 0.3, self.screen_size.get("height") * 0.5,
                              self.screen_size.get("width") * 0.8, self.screen_size.get("height") * 0.5)

    def get_toast(self, message):
        # 获取toast消息
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_data = self.search_element((By.XPATH, toast_xpath),poll=0.1)
        # 返回获取toast消息
        return toast_data.text