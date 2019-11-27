"""
登录测试用例
"""
import allure
import pytest

from base.base_page import BasePage
from common.utils import init_driver
from page.page_factory import PageFactory
from tools.read_yaml import build_login_data


class TestLogin(object):
    """登录测试类"""

    def setup(self):
        """驱动对象的获取"""
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 工厂类实例化
        self.base_page = BasePage(self.driver)

    def teardown(self):
        """退出驱动对象"""
        self.driver.quit()

    @pytest.mark.parametrize('name,pwd,expect,is_success', build_login_data())
    @allure.MASTER_HELPER.step(title='登陆测试')
    def test_login(self, name, pwd, expect, is_success):
        """登录测试方法"""

        if is_success:
            allure.MASTER_HELPER.attach('正向用例测试', '点击我的，点击登录，输入账号密码，点击登录按钮')
            # 正向测试
            self.page_factory.home_page.click_mine()  # 点击我的
            self.page_factory.mine_page.click_login()  # 点击登录/注册
            self.page_factory.login_page.input_username(name)  # 输入账号
            self.page_factory.login_page.input_password(pwd)  # 输入密码
            self.page_factory.login_page.click_login_btn()  # 点击登录按钮
            self.page_factory.login_page.click_con_btn()  # 点击签到确定按钮
            nick_name = self.page_factory.login_page.get_nick_name()  # 获取昵称
            print('昵称是:', nick_name)
            # assert expect in nick_name  # 断言判断结果
            try:
                assert expect in nick_name  # 断言判断结果
            except Exception as e:
                self.driver.get_screenshot_as_file('./screenshot/bug.png')
                with open('./screenshot/bug.png', 'rb')as f:
                    allure.MASTER_HELPER.attach('断言失败截图', f.read(), allure.MASTER_HELPER.attach_type.PNG)

                raise e  # 主动抛出异常,恢复用例执行状态
        else:
            # 反向测试
            # self.page_factory.home_page.click_mine()  # 点击我的
            # self.page_factory.mine_page.click_login()  # 点击登录/注册
            # self.page_factory.login_page.input_username(name)  # 输入账号
            # self.page_factory.login_page.input_password(pwd)  # 输入密码
            # self.page_factory.login_page.click_login_btn()  # 点击登录按钮
            # message = self.page_factory.login_page.get_toast()
            # assert expect in message

            self.page_factory.home_page.click_mine()  # 点击我的
            self.page_factory.mine_page.click_login()  # 点击登录/注册
            self.page_factory.login_page.input_username(name)  # 输入账号
            self.page_factory.login_page.input_password(pwd)  # 输入密码
            self.page_factory.login_page.click_login_btn()  # 点击登录按钮

            result = self.page_factory.login_page.get_login_btn_attr('clickable')  # 获取登录按钮属性值
            print('获取的属性值为', result)
            assert expect == result  # 断言判断结果
