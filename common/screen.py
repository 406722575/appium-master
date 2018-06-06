#coding=utf-8
from functools import wraps
import time
from common.logger import Log
from appium import webdriver

log = Log()
def getImage(function):
        @wraps(function)
        def get_ErrImage(self,*args, **kwargs):      
            try:
                result = function(self,*args, **kwargs)       
            except Exception as msg:
                contexts = self.driver.contexts 
                if len(contexts):
                    self.driver.switch_to.context(contexts[0])
                nowTime = time.strftime("%Y%m%d.%H.%M.%S")
                self.driver.get_screenshot_as_file(r'D:\\appium-master\Screenshots\\'+'%s.png' % nowTime)
                log.info("%s 截图成功"%function.__name__)
                raise msg
                self.driver.switch_to.context(contexts[-1])
                
                                            
            else:
                log.info("%s 脚本运行正常"%function.__name__)
            # return result
        return get_ErrImage




