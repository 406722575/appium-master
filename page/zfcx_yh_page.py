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
class Zfxc_Yh(BasePage):
   
    loginbtn_loc = (By.ID,"com.gdcirrus.fsitep:id/login")
    zfxu_loc = (By.CLASS_NAME,"android.widget.TextView")  
    yh_loc = (By.PARTIAL_LINK_TEXT,'业户')
    cartype_loc =(By.CSS_SELECTOR,'.label-checkbox')
    yhmc_loc = (By.CSS_SELECTOR,".item-input")
    cx_loc = (By.PARTIAL_LINK_TEXT,'查询')
    clxcjg_loc = (By.CSS_SELECTOR,'.staffName')
    back_loc = (By.CSS_SELECTOR,'button.button-link')
    backhome_loc = (By.PARTIAL_LINK_TEXT,'返回主界面')
   
    
    
    def yh(self):   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")    
        #点击执法查询
        class_text = 'className("android.widget.TextView").text("执法查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击执法查询") 
        # 切换到webview
        bp.switch_to_webview()
        
        self.find_element(self.yh_loc).click()
        log.info("点击业户") 
        
        self.radio(self.cartype_loc,"佛山客货运业户" ) 
        log.info("选择业户类别") 
        
        self.find_element(self.yhmc_loc).click()
        self.find_element(self.yhmc_loc).send_keys(u"李明")  
        log.info("输入业户名称")  
        
        self.find_element(self.cx_loc).click()
        log.info("点击查询按钮")
        # 切回native
        bp.switch_to_NATIVE_APP()
        swipe.swipeUp(self.driver, n=60)
        swipe.swipeDown(self.driver, n=20)
        log.info("滑动操作")
        # 切换到webview
        self.switch_to_webview()
        
        self.find_element(self.clxcjg_loc).click()
        log.info("点击车辆查询结果")   
        
        self.find_element(self.back_loc).click() 
        log.info("点击返回") 
        time.sleep(2) 
        
        self.find_element(self.clxcjg_loc).click()
        log.info("点击车辆查询结果") 
        time.sleep(2)
        
        self.find_element(self.backhome_loc).click()
        log.info("点击返回主界面") 
        time.sleep(2)
        
        
    
                

    
        
        
        
        



