from common.base import BasePage
import time
from selenium.webdriver.common.by import By
from appium import webdriver
from common import swipe
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Log
import re,random,os



log = Log()
class workRepoMobile(BasePage):
   
    loginbtn_loc = (By.ID,"com.gdcirrus.fsitep:id/login")
    back_loc = (By.CSS_SELECTOR,'button.button-link')
    edittext_loc = (By.PARTIAL_LINK_TEXT,'信息报送')
    
    
    listtitle_loc = (By.CSS_SELECTOR,'span.item_icon')
    open_staff_loc = (By.ID,"open_staff")
    item_department_loc = (By.CSS_SELECTOR,"span.item_department")
    add_receive_loc = (By.ID,"add_receive")
    workRepoMessageTitle_loc = (By.ID,"workRepoMessageTitle")
    workRepoMessageContent_loc = (By.ID,"workRepoMessageContent")
    send_btn_loc = (By.ID,"send_btn")
    upload_img_btn_loc = (By.CSS_SELECTOR,"div#upload_img_btn")
    file_loc = (By.PARTIAL_LINK_TEXT,"文件")
    upload_doc_btn_loc =(By.ID,"upload_doc_btn")

    
     

    def work_send(self):
        """信息发送_发文"""   
        bp=BasePage(self.driver)  
        
        self.find_element(self.loginbtn_loc).click()        
        log.info("点击登录")         
        time.sleep(3)
         
        swipe.swipeUp(self.driver, n=10)
        class_text = 'className("android.widget.TextView").text("信息报送")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击信息报送")
        time.sleep(2) 
         #切换到webview
        bp.switch_to_webview()
        log.info("切换到webview")
        self.find_element(self.open_staff_loc).click() 
        log.info("点击添加联系人按钮")
        time.sleep(3) 
        
        item_titles = self.find_elements(self.listtitle_loc)    
        item_titles[1].click()
        log.info("选择执法一大队")
        time.sleep(2)        
        self.find_element(self.add_receive_loc).click() 
        log.info("点击添加按钮")
        time.sleep(3)     
        titles = ["通知关于整治高明区","紧急任务请二大队马上前往处理需要增援警力!","2018年光伏发电有关事项的通知"]
        title = random.choice(titles)
        path = r"D:\appium-master\cfg\content.txt"
        content = bp.get_content(path)
        log.info("随机读取文件中的某一行内容")
        self.find_element(self.workRepoMessageTitle_loc).clear()        
        self.find_element(self.workRepoMessageTitle_loc).send_keys(title)
        log.info("输入标题")
        self.find_element(self.workRepoMessageContent_loc).clear() 
        time.sleep(5)        
        self.find_element(self.workRepoMessageContent_loc).send_keys(content)
        log.info("输入正文内容")
        time.sleep(3)
        
        self.find_element(self.upload_img_btn_loc).click() 
        log.info("点击附件-图片")
        time.sleep(3)
        bp.switch_to_NATIVE_APP()
        class_text = 'className("android.widget.TextView").text("文件")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("选择文件")
        time.sleep(5)
        class_text = 'resourceId("android:id/title").text("图库")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("点击图库")
        time.sleep(3)
        loc_id = 'new UiSelector().resourceId("com.android.gallery:id/grid")'
        self.driver.find_element_by_android_uiautomator(loc_id).click()
        log.info("选择图片")
        time.sleep(10)
        
        swipe.swipeUp(self.driver, n=20)
        time.sleep(3)
        bp.switch_to_webview()
        log.info("切换到webview")
        self.find_element(self.upload_img_btn_loc).click() 
        log.info("点击附件-图片")
        bp.switch_to_NATIVE_APP()
        class_text = 'className("android.widget.TextView").text("相机")'
        self.driver.find_element_by_android_uiautomator(class_text).click()
        log.info("选择相机")
        time.sleep(3)

        bp.switch_to_webview()
        log.info("切换到webview")
        self.find_element(self.upload_doc_btn_loc).click() 
        log.info("点击附件-文件")
        time.sleep(3)


        self.find_element(self.send_btn_loc).click() 
        log.info("点击发送")
        time.sleep(5)

    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64()
    
        
     
    
        
        
        
        



