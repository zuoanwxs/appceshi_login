from selenium.webdriver.common.by import By
"""
    我的页面
"""
# 我 -按钮
my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")
"""
    注册页面
"""
# 已有账号,去登陆
exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")
"""
    登陆页面
"""
# 登陆用户名
login_name_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
# 登陆密码
login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
# 登陆按钮
login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
# 关闭登陆页面按钮
login_close_page_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
    个人中心页面
"""
# 判断个人中心全部订单是否存在
all_order_xpath = (By.XPATH, "//*[contains(@text,'全部订单')]")
# 设置按钮
setting_btn_id= (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
    设置页面
"""
logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
# 确认退出按钮
confirm_logout_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")