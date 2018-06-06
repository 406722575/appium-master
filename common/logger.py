#coding=utf-8
import logging, time, os
#日志保存路径
log_path = r"D:\appium-master\log"

class Log(object):
    def __init__(self):
        #文件名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')

    def _console(self, level, message):
        #创建一个FileHandler,用于写到本地
        fh = logging.FileHandler(self.logname, "a", encoding="utf-8")#追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个StreamHandler，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        #避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()

    def debug(self, message):
        self._console("debug", message)

    def info(self, message):
        self._console("info", message)
    
    def warning(self, message):
        self._console("warning", message)

    def error(self, message):
        self._console("error", message)

            
if __name__ == "__main__":
    log = Log()
    log.info("测试开始")
    log.info("要")
    log.warning("结束")
