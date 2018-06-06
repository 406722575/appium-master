#coding=utf-8
import re
import sys
sys.path.append("C:/Users/Nic/Desktop/appium-master")


lis = ['粤Y752J8', '粤E64V15', '粤E19524', '粤E0Y041', '粤E17955', '粤Y285H8', '粤Y341K5', '粤Y39470', '粤Y29153', '粤Y37302', '粤Y2Y950', '粤Y33244']

y = ",".join(lis)


# reg = re.compile(r'(粤E)')
a = re.findall("粤E\w+",y)
# print(a[0])
# for i in a:
#     print(i)
# print(a)




# import linecache    
# import random  
  
# for i in range(1):#for循环几次  
#     a = random.randint(1, 5) #1-9中生成随机数    
#     #从文件poem.txt中对读取第a行的数据  
#     theline = linecache.getline(r'C:\Users\Nic\Desktop\appium-master\cfg\t.txt',a)  
#     print (theline) 

import os
import linecache

def get_content(path):
    '''读取缓存中文件内容，以字符串形式返回'''
    if os.path.exists(path):
        content = ''
        cache_data = linecache.getlines(path)
        for line in range(len(cache_data)):
            content += cache_data[line]
        return content
    else:
        print('the path [{}] is not exist!'.format(path))

def main():
    path = r'C:\Users\Nic\Desktop\appium-master\cfg\t.txt'
    content = get_content(path)
    print(content)

# if __name__ == '__main__':
#     main()


print(fin.read())

