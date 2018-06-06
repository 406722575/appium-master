from common.base import BasePage
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import os
from common import swipe
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Log

log = Log()
class Gps_Car(BasePage):
   
    loginbtn_loc = (By.ID,"com.gdcirrus.fsitep:id/login")
    zfxu_loc = (By.CLASS_NAME,"android.widget.TextView")   
    cartype_loc =(By.CSS_SELECTOR,'.label-checkbox')
    qd_loc =(By.CLASS_NAME,'pull-right')
    carnum_loc = (By.ID,'localPicker')
    listcarnum_loc = (By.CSS_SELECTOR,'.picker-item')
    EditText_loc = (By.ID,"number")
    locationMap_loc = (By.ID,'locationMap')
    clxcjg_loc = (By.CSS_SELECTOR,'.staffName')     
    yh_loc = (By.PARTIAL_LINK_TEXT,'业户')
    wz_loc = (By.PARTIAL_LINK_TEXT,'违章')
    backhome_loc = (By.PARTIAL_LINK_TEXT,'返回主界面')
    back_loc = (By.CSS_SELECTOR,'button.button-link')
    camera_loc = (By.CSS_SELECTOR,".fa-camera")
    edittext_loc = (By.PARTIAL_LINK_TEXT,'执法查询')
    coltype_loc =(By.CSS_SELECTOR,'.label-checkbox')
    vehicleInformation_loc = (By.ID,"vehicleInformation")
    getLocationDetail_loc = (By.XPATH,"//button[text()='详情信息']")
    locationDetail_loc =(By.ID,"locationDetail")
    f_loc =(By.ID,"aboutCar") 
    
    
    def locationDetail(self):
        """GPS查询_车辆_查询位置信息"""   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")    
        
        class_text = 'className("android.widget.TextView").text("GPS查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击GPS查询")
        # 切换到webview
        bp.switch_to_webview()
        self.radio(self.cartype_loc,"客货运车辆" ) 
        log.info("选择客货运车辆") 
        self.radio(self.coltype_loc,"黄色" )
        log.info("选择黄色")  
        time.sleep(3)
        
        self.find_element(self.carnum_loc).click()
        self.radio(self.listcarnum_loc,"粤E")
        log.info("点击车牌下拉框")
        
        self.find_element(self.qd_loc).click()
        log.info("点击确定") 
        
        
        self.find_element(self.EditText_loc).click()        
        self.find_element(self.EditText_loc).send_keys(u"T9333")
        log.info("输入车牌号码") 

        
        self.find_element(self.locationDetail_loc).click()
        log.info("点击查询位置信息") 
        time.sleep(4)
        # try:
        #     self.find_element(self.clxcjg_loc).click() 
        #     log.info("点击车辆查询结果")
        # except Exception  as e:
        #     print("没有找到",format(e))
        # 切回native
        bp.switch_to_NATIVE_APP()
        swipe.swipeUp(self.driver, n=3)
        log.info("向下滑动")
        # 切换到webview
        bp.switch_to_webview()
        self.find_element(self.vehicleInformation_loc).click()
        log.info("点击车辆信息")
        
        # 切回native
        bp.switch_to_NATIVE_APP()
        
        swipe.swipeUp(self.driver, n=3)
        log.info("向下滑动")
        time.sleep(3)

        bp.switch_to_webview()
        self.find_element(self.yh_loc).click() 
        log.info("点击业户")        
        time.sleep(5) 
    
        
        self.find_element(self.back_loc).click()
        log.info("点击返回")   
        
        self.find_element(self.wz_loc).click()
        log.info("点击违章 ") 
        
        self.find_element(self.backhome_loc).click()
        log.info("点击返回主界面")     
        
        self.find_element(self.camera_loc).click()
        log.info("点击拍照")
        time.sleep(2)
        bp.adbKeyEvent()
        log.info("手机返回键")

    def locationMap(self):
        """GPS查询_车辆_查询位置图"""   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")    
        
        class_text = 'className("android.widget.TextView").text("GPS查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击GPS查询")
        # 切换到webview
        bp.switch_to_webview()
        self.radio(self.cartype_loc,"出租客运" ) 
        log.info("选择客货运车辆") 
        self.radio(self.coltype_loc,"黄色" )
        log.info("选择黄色")  
        time.sleep(3)
        
        self.find_element(self.carnum_loc).click()
        self.radio(self.listcarnum_loc,"粤E")
        log.info("点击车牌下拉框")
        
        self.find_element(self.qd_loc).click()
        log.info("点击确定") 
        
        
        self.find_element(self.EditText_loc).click()        
        self.find_element(self.EditText_loc).send_keys(u"1Y471")
        log.info("输入车牌号码") 

        
        self.find_element(self.locationMap_loc).click()
        log.info("点击查询位置图") 
        time.sleep(3)
        self.find_element(self.getLocationDetail_loc).click()        
        log.info("点击详情信息") 
        time.sleep(3)
        # try:
        #     self.find_element(self.clxcjg_loc).click() 
        #     log.info("点击车辆查询结果")
        # except Exception  as e:
        #     print("没有找到",format(e))
        
        self.find_element(self.vehicleInformation_loc).click()
        log.info("点击车辆信息")
        
        # # 切回native
        # bp.switch_to_NATIVE_APP()
        
        # swipe.swipeUp(self.driver, n=3)
        # log.info("向下滑动")
        # time.sleep(3)

        # bp.switch_to_webview()
        # self.find_element(self.yh_loc).click() 
        # log.info("点击业户")        
        # time.sleep(5) 
    
        
        # self.find_element(self.back_loc).click()
        # log.info("点击返回")   
        
        # self.find_element(self.wz_loc).click()
        # log.info("点击违章 ") 
        
        # self.find_element(self.backhome_loc).click()
        # log.info("点击返回主界面")     
        
        
        
    def get_finish_button_text(self):
        return self.find_element(self.cartype_loc).text
        
                

    
        
        
        
        



