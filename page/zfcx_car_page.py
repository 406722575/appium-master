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
class Zfxc_car(BasePage):
   
    loginbtn_loc = (By.ID,"com.gdcirrus.fsitep:id/login")
    zfxu_loc = (By.CLASS_NAME,"android.widget.TextView")   
    cartype_loc =(By.CSS_SELECTOR,'.label-checkbox')
    qd_loc =(By.CLASS_NAME,'pull-right')
    carnum_loc = (By.CSS_SELECTOR,'#localPicker')
    listcarnum_loc = (By.CSS_SELECTOR,'.picker-item')
    EditText_loc = (By.ID,"vehicleNum")
    cx_loc = (By.CLASS_NAME,'button-fill')
    clxcjg_loc = (By.CSS_SELECTOR,'.staffName')     
    yh_loc = (By.PARTIAL_LINK_TEXT,'业户')
    wz_loc = (By.PARTIAL_LINK_TEXT,'违章')
    backhome_loc = (By.PARTIAL_LINK_TEXT,'返回主界面')
    back_loc = (By.CSS_SELECTOR,'button.button-link')
    camera_loc = (By.CSS_SELECTOR,".fa-camera")
    edittext_loc = (By.PARTIAL_LINK_TEXT,'执法查询')
    
    
    
    def car(self):   
        bp=BasePage(self.driver)     
        
        self.find_element(self.loginbtn_loc).click() 
        log.info("点击登录")    
        time.sleep(3) 
        class_text = 'className("android.widget.TextView").text("执法查询")'
        self.driver.find_element_by_android_uiautomator(class_text).click()   
        log.info("点击执法查询")
        # 切换到webview
        bp.switch_to_webview()
        self.radio(self.cartype_loc,"客货运车辆" )   
        log.info("选择客货运车辆")     
        self.find_element(self.carnum_loc).click() 
        log.info("点击车牌下拉框") 
        self.radio(self.listcarnum_loc,"粤")
        log.info("滑动下拉") 
        self.find_element(self.qd_loc).click()
        log.info("点击确定")  
        self.find_element(self.EditText_loc).click()        
        self.find_element(self.EditText_loc).send_keys(u"E12345")
        log.info("输入车牌号码")
        self.find_element(self.cx_loc).click()
        log.info("点击查询按钮") 
       
        self.get_Toast("无相关信息")
        
        time.sleep(4)
        self.find_element(self.clxcjg_loc).click()
        log.info("点击查询结果") 
        

        # # wait = WebDriverWait(self.driver, 10)
        # # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
        # #打印源码
        # # print(self.driver.page_source)
        # time.sleep(5)        
        # self.find_element(self.yh_loc).click()        
        # log.info("点击业户")        
        # time.sleep(5) 
        # # 切回native
        # bp.switch_to_NATIVE_APP()
        # #向下,参数1：driver 参数2：t是持续时间 参数3：滑动次数
        # swipe.swipeUp(self.driver, n=3)
        # log.info("向下滑动")         
        # swipe.swipeDown(self.driver, n=3)
        # log.info("向上滑动")         
        # self.switch_to_webview()         
        # self.find_element(self.back_loc).click()        
        # log.info("点击返回")           
        # self.find_element(self.wz_loc).click()        
        # log.info("点击违章 ")         
        # self.find_element(self.backhome_loc).click()        
        # log.info("点击返回主界面")             
        # self.find_element(self.camera_loc).click()        
        # log.info("点击拍照")
        # time.sleep(2)
        # bp.adbKeyEvent()
        # log.info("手机返回键")
        

        
                

    
        
        
        
        



