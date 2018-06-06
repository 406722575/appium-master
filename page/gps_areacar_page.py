from common.base import BasePage
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import os
from common import swipe
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Log
import re

log = Log()
class Gps_AreaCar(BasePage):
   
    loginbtn_loc = (By.ID,"com.gdcirrus.fsitep:id/login")
    zfxu_loc = (By.CLASS_NAME,"android.widget.TextView")   
    cartype_loc =(By.CSS_SELECTOR,'.label-checkbox')
    qd_loc =(By.CLASS_NAME,'pull-right')
    carnum_loc = (By.ID,'localPicker')
   
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
    locationDetail_loc =(By.ID,"carList")
    f_loc =(By.ID,"aboutCar") 
    areacar_loc = (By.PARTIAL_LINK_TEXT,"区域车辆")
    radius_loc = (By.ID,"radius")
    listcarnum_loc = (By.CSS_SELECTOR,'div.picker-item')
    descSpan_loc = (By.CSS_SELECTOR,"span.descSpan>span") 
    carListMap_loc = (By.ID,"carListMap")  
    locale_loc = (By.ID,"locale")   
    carlist_loc = (By.ID,"toCarList")    
    
    def area_car(self):
        """GPS查询_区域车辆_查询目标位置"""   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")   
        time.sleep(3) 
        
        class_text = 'className("android.widget.TextView").text("GPS查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击GPS查询")
        # 切换到webview
        bp.switch_to_webview()
        self.find_element(self.areacar_loc).click()
        log.info("点击区域车辆") 
        self.radio(self.cartype_loc,"客货运车辆" ) 
        log.info("选择客货运车辆")         
        time.sleep(3)
        
        self.find_element(self.radius_loc).click()
        time.sleep(2)
        self.radio(self.listcarnum_loc,"800")
        log.info("选择半径800")
        time.sleep(3)
        self.find_element(self.qd_loc).click()
        log.info("点击确定") 
  
        self.find_element(self.locationDetail_loc).click()
        log.info("点击查目标位置") 
        time.sleep(5)
        
        
        bp.switch_to_NATIVE_APP()
        swipe.swipeUp(self.driver, n=50)
        swipe.swipeDown(self.driver, n=50)
        log.info("向下滑动")
        # 切换到webview
        bp.switch_to_webview()
        # self.find_element(self.vehicleInformation_loc).click()
        # log.info("点击车辆信息")
        bp.regular_expression(self.clxcjg_loc)        
        log.info("使用正则匹配粤E")
        # 切回native
        bp.switch_to_NATIVE_APP()
        swipe.swipeUp(self.driver, n=10)
        log.info("向下滑动")
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
        time.sleep(3) 

    
        
        
    def gps_locationMap(self):
        """GPS查询_区域车辆_查询位置图"""   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")   
        time.sleep(3) 
        
        class_text = 'className("android.widget.TextView").text("GPS查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击GPS查询")
        # 切换到webview
        bp.switch_to_webview()
        self.find_element(self.areacar_loc).click()
        log.info("点击区域车辆") 
        self.radio(self.cartype_loc,"出租客运" ) 
        log.info("选择出租客运")         
        time.sleep(3)

        self.find_element(self.radius_loc).click()
        time.sleep(2)
        self.radio(self.listcarnum_loc,"1500")
        log.info("选择半径1500")
        time.sleep(3)
        self.find_element(self.qd_loc).click()
        log.info("点击确定") 

        self.find_element(self.locale_loc).click()
        time.sleep(2)
        self.radio(self.listcarnum_loc,"大沥汽车客运站")
        time.sleep(1)
        log.info("选择大沥汽车客运站") 
        time.sleep(2)
        self.find_element(self.qd_loc).click()
        log.info("点击确定")
        
        
  
        self.find_element(self.carListMap_loc).click()
        log.info("点击查目标位置") 
        time.sleep(2)
        self.find_element(self.carlist_loc).click()
        log.info("点击查看车辆列表") 
        time.sleep(2)
        
        
        # bp.switch_to_NATIVE_APP()
        # swipe.swipeUp(self.driver, n=50)
        # swipe.swipeDown(self.driver, n=50)
        # log.info("向下滑动")
        # # 切换到webview
        # bp.switch_to_webview()
        # # self.find_element(self.vehicleInformation_loc).click()
        # # log.info("点击车辆信息")
        bp.regular_expression(self.clxcjg_loc)        
        log.info("使用正则匹配粤E")
        time.sleep(10) 
        # 切回native
        bp.switch_to_NATIVE_APP()
        swipe.swipeUp(self.driver, n=10)
        log.info("向下滑动")
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
        time.sleep(3) 
        
    def get_finish_button_text(self):
        return self.find_element(self.cartype_loc).text
        
                

    
        
        
        
        



