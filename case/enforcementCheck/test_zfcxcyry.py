#coding=utf-8
import sys
sys.path.append(r"D:\appium-master")
from appium import webdriver
import unittest
from page.zfcx_cyry_page import Zfxc_Cyry
import time
from common.logger import Log
from common.screen import getImage



log = Log()


class Test(unittest.TestCase):
    """执法查询_从业人员"""
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',#可有可无
            'platformVersion': '5.1.1',
            # apk包名
            'appPackage': 'com.gdcirrus.fsitep',
            # apk的launcherActivity
            'appActivity': 'com.gdcirrus.fsitep.activity.LoginActivity',         
            #如果存在activity之间的切换可以用这个
            # 'appWaitActivity':'.MainActivity',
            'unicodeKeyboard': True,
            #隐藏手机中的软键盘
            'resetKeyboard': True,
            #启动后结束后不清空应用数据
            'noReset': True
            # 'automationName':'UIAutomator2'
            
            }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass
        
    @getImage
    def test_zfcx_cyry(self):
        """验证执法查询_从业人员功能是否正确"""
        self.driver.wait_activity(".base.ui.MainActivity", 3)
        zc = Zfxc_Cyry(self.driver)
        zc.cyry()
        

if __name__ == '__main__':
    unittest.main()