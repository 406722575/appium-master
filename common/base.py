from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time,os,re
import linecache    
import random  
from common.logger import Log
# '''
# 这个类主要是完成所有页面的一些公共方法的封装
# '''
log = Log()
class BasePage(object):	

	def __init__(self,appium_driver):
		self.driver = appium_driver

#重新封装单个元素定位方法
	def find_element(self,loc):
		try:
			WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print (u"%s 页面中未能找到 %s 元素" %(self,loc))

#重新封装一组元素定位方法
	def find_elements(self,loc):
		try:
			if len(self.driver.find_elements(*loc)):
				return self.driver.find_elements(*loc)
		except:
			print (u"%s 页面中未能找到 %s 元素" %(self,loc))
			
#重新封装输入方法
	def send_keys(self,loc,value,clear_first=True,click_first=True):
		try:
			if click_first:
				self.find_element(loc).click()
			if clear_first:
				self.find_element(loc).clear()
			self.find_element(loc).send_keys(value)
		except AttributeError:
			print ("%s 页面未能找到 %s 元素") %(self,loc)

#重新封装按钮点击方法
	def clickButton(self,loc,find_first=True):
		try:
			if find_first:
				self.find_element(loc)
			self.find_element(loc).click()
		except AttributeError:
			print ("%s 页面未能找到 %s 按钮" %(self,loc))

	def always_allow(self,driver, number=5):
    # """  
    # fuction:权限弹窗-始终允许
    # args:1.传driver 2.number，判断弹窗次数，默认给5次
    # 其它：
    # WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    # """
		for i in range(number):
			loc = ("xpath", "//*[@text='始终允许']")
			try:
				e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
				e.click()
			except:
				pass

	def is_toast_exist(self,driver,text,timeout=30,poll_frequency=0.5):
    # '''is toast exist, return True or False
    # :Agrs:
    #  - driver - 传driver
    #  - text   - 页面上看到的文本内容
    #  - timeout - 最大超时时间，默认30s
    #  - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    # :Usage:
    #  is_toast_exist(driver, "看到的内容")
    # '''
		try:
			toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
			WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
			print(toast_loc,"正确")
			return True
		except:
			print(toast_loc,"没有找到")
			return False
	

	# 切换到webview
	def switch_to_webview(self):
		contexts = self.driver.contexts 
		print("当换到",contexts[-1])         
		return self.driver.switch_to.context(contexts[-1])
    # 切回native
	def switch_to_NATIVE_APP(self):
		contexts = self.driver.contexts   
		print("当换到",contexts[0])       
		return self.driver.switch_to.context(contexts[0])

	def radio(self,loc,text=None):
		radios = self.find_elements(loc)
		for radio in radios:
			if radio.is_displayed() and text== radio.text:								
				time.sleep(2)
				radio.click() 
	


	#按手机返回键
	def adbKeyEvent(self):
		adb = 'adb shell input keyevent 4' 
		os.system(adb)

	def regular_expression(self,loc,text=None,radios=None):
		u"""使用正则匹配粤E"""
		radios = self.find_elements(loc)
		lists = []
		for radio in radios:
			lists.append(radio.text)            
		y = ",".join(lists)
		radio = re.findall(r"粤E\w+",y)   
		self.driver.find_element_by_xpath("//*[contains(text(),'"+radio[0].strip()+"')]").click()      
		time.sleep(5)

	def get_content(self,path):
		u"""随机读取文件中的某一行内容,txt保存为utf-8"""
		for i in range(4):#for循环几次  
			a = random.randint(1,4) #1-9中生成随机数    
			#从文件poem.txt中对读取第a行的数据 
			theline = linecache.getline(path,a)
		return theline  


	

			
	def find_Toast(self,message,timeout=20,poll_frequency = 0.01):  #查找toast值
		'''
		method explain:查找toast的值
		parameter explain：【text】给定的toast值
		Usage:
			device.find_Toast('再按一次退出iBer')
		'''
		log.info("获取toast值---'%s'" %message)
		try:
			toast_loc = ("xpath",".//*[contains(@text,'%s')]" %message)
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
			log.info("查找到toast--'%s'"%message)			
			return True
		except:
			log.info("未查找到toast--'%s'"%message)
			return False

	def get_Toast(self,message):  #查找toast值
		'''
		method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
		parameter explain：【text】查找的toast值
		Usage:
			device.get_Toast('再按一次退出iBer')
		'''
		log.info("查找toast值---'%s'" %(message))
		try:
			message = '//*[@text=\'{}\']'.format(message)
			ele = WebDriverWait(self.driver,20,0.01).until(EC.presence_of_element_located((By.XPATH,message)))
			log.info("查找到toast----%s"%message)
			return ele.get_attribute("text")
			
		except:
			log.error("未查找到toast----%s"%message)
			return False




	# #勾选前判断是否勾选
        # t =  self.find_element(self.cartype_loc).is_selected()
        # self.find_element(self.cartype_loc).click()
        # #点击后是否勾选
        # r =  self.find_element(self.cartype_loc).is_selected()
        #点击车辆类别

	# #复选框定位、勾选
    # inputs = self.find_elements(self.cartype_loc)
    # for input in inputs:
    #     if input.get_attribute('type')=='checkbox':
    #         input.click()
    #         time.sleep(2)
    
    # self.driver.find_elements_by_css_selector('input[type="checkbox"]').pop().click()

	    