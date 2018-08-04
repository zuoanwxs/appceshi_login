import sys, os, pytest
sys.path.append(os.getcwd())

from Page.page import Page
from Base.Read_Data import Read_Data
from Base.get_driver import init_driver


def yml_data():
    data_list = []
    data = Read_Data("login_data.yml").get_data()
    for i in data.keys():
        data_list.append((i, data.get(i).get("name"), data.get(i).get("passwd"),
                         data.get(i).get("tag"), data.get(i).get("get_mes"),
                          data.get(i).get("expect_message")))
    return data_list



class Test_Login:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(init_driver())

    def teardown_class(self):
        self.page_obj.driver.quit()
    @pytest.mark.parametrize("test_num, name, passwd, tag, get_mes, expect_data", yml_data())
    def test_login(self,test_num, name, passwd, tag, get_mes, expect_data):
        # 登录
        """
        登陆步骤：
            1.点击我
            2.点击已有账户
            3.登陆页面输入登陆信息
            if 登录成功：
                退出操作
            if 登录失败：
                继续输入
        :param name:
        :param passwd:
        :param expect_data:
        :param tag:判断是否是登陆成功用例
        :return:
        """
        # 点击我
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号
        self.page_obj.get_sign_page_obj().click_exits_accout()
        # 登陆操作
        self.page_obj.get_login_page_obj().login(name, passwd)
        if tag:
            try:
                # 全部订单是否存在
                all_order = self.page_obj.get_person_page_obj().get_all_order_status()
                # 点击设置按钮
                self.page_obj.get_person_page_obj().click_setiing_btn()
                # 退出操作
                self.page_obj.get_setting_page_obj().click_logout_btn()
                # 断言全部订单
                assert all_order
            except:
                # 关闭登陆页面
                self.page_obj.get_login_page_obj().close_login_page()
                assert False
        else:
            try:
                # 获取toast消息
                toast_message = self.page_obj.get_login_page_obj().get_toast(get_mes)
                # 登陆按钮是否存在
                login_btn = self.page_obj.get_login_page_obj().login_btn_status()
                # 判断提示信息
                assert toast_message == expect_data and login_btn
            finally:
                # 关闭当前登陆页面
                self.page_obj.get_login_page_obj().close_login_page()


