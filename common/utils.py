"""
驱动对象获取方法
"""
# 1. 导包
from time import sleep
from appium import webdriver


# 3. 声明启动参数
# capabilities = {
#     "platformName": "Android",  # 平台类型(iOS 和 Android)
#     "platformVersion": "5.1",  # 手机系统版本
#     "deviceName": "模拟器",  # 设备名称
#     "appPackage": "com.android.settings",  # 待测应用的包名
#     "appActivity": ".Settings"  # 待测应用的启动名
# }
def init_driver():
    # 3. 声明启动参数
    capabilities = dict()  # 声明空字典
    capabilities['platformName'] = "Android"  # 平台类型(iOS 和 Android)
    capabilities['platformVersion'] = "5.1"  # 手机系统版本
    capabilities['deviceName'] = "模拟器"  # 设备名称
    capabilities['appPackage'] = "com.bjcsxq.chat.carfriend"  # 待测应用的包名
    capabilities['appActivity'] = ".MainActivity"  # 待测应用的启动名
    capabilities['resetKeyboard'] = True
    capabilities['unicodeKeyboard'] = True

    # 学车不 包名/启动名
    # com.bjcsxq.chat.carfriend/.MainActivity

    # 2. 实例化驱动对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

    return driver


if __name__ == '__main__':
    init_driver()
