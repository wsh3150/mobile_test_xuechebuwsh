"""
登录测试用例
"""
from common.utils import init_driver
from page.page_factory import PageFactory


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        """驱动对象的获取"""
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 工厂类实例化

    def teardown_class(self):
        """退出驱动对象"""

    def test_login(self):
        """登录测试方法"""
        self.page_factory.home_page.mine()  # 点击我的
        self.page_factory.mine_page.click_login()  # 点击登录/注册
        self.page_factory.login_page.input_func('15535853634')  # 输入账号
        self.page_factory.login_page.input_func('zxc727397')  # 输入密码
        self.page_factory.login_page.click_login_btn()  # 点击登录按钮
        self.page_factory.login_page.click_con_btn()  # 点击签到确定按钮
        nick_name = self.page_factory.login_page.get_nick_name()  # 获取昵称
        print('昵称是', nick_name)
        # 断言判断结果
