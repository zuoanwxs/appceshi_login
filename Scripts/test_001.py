from selenium.webdriver.common.by import By

from Base.get_driver import init_driver
from Page.page import Page
import time


page_obj = Page(init_driver())

# 点击我
page_obj.get_home_page_obj().click_my_btn()
# 点击已有账号
page_obj.get_sign_page_obj().click_exits_accout()
# 登陆操作
page_obj.get_login_page_obj().login("1111","1111")
try:
    # 获取提示消息
    to = page_obj.get_login_page_obj().search_element((By.XPATH, "//*[contains(@text,'不存在')]"),timeout=5,poll=0.1)

    print(to.text)
finally:
    time.sleep(5)
    page_obj.driver.quit()

