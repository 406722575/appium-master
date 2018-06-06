# coding=utf-8

# s = "joshua!"
# print(s[2:4])



from time import clock

def timer(f):
    def _f(*args):
        t0 = clock()
        f(*args)
        return clock() - t0
    return _f

# def delete_elem(x,index):
#     del x[index]

# x = [5]*1000000

# c = timer(delete_elem)(x, -1)
# print(c)

# b = timer(delete_elem)(x, 0)
# print(b)

# x = sorted("zdabscd")
# print(type(x))
# #将list转换成str
# y = ",".join(sorted(x))
# print(y)
# print(type(y))

# # B
# 0 1 1 2 3 5 8

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)

# d = f(5)
# print(d)

#二分法，只能用于排序后的数据
# def search(num_list, val):

#     if val not in num_list:        
#         return "输入的数字不存在列表中"
#     left = 0
#     right = len(num_list)
#     while(left <= right):
#         mid = (left+right)//2
#         if(num_list[mid] == val):
#             return mid
#         elif (num_list[mid] > val):
#             right = mid-1
#         else:
#             left = mid+1
#     return -1

# num_list = [1,3,4,5,7]
# a = search(num_list, 8)
# print(a)


#冒泡排序
# import time
# @timer
# def bubble_owrt(num_list:list):
    
    
#     for i in range(len(num_list)):
#         for j in range(1,len(num_list)-i):
#             if num_list[j] < num_list[j-1]:
#                 num_list[j], num_list[j-1] = num_list[j-1],num_list[j]
    
   
#     return num_list


# num_list = [9,3,14,5,7]
# a = bubble_owrt(num_list)
# print(a)

# class Person(object):
#     def __init__(self,name,gender):
#         self.name = "doc"+name
#         self.gender = gender
#     def say(self):
#         return ("hi,i'm  %s from %s" %(self.name, self.gender))

# class MDPerson(Person):
#     def __init__(self,name,gender,dept="Cardiac"):
#         super().__init__(name,gender)
    
#     def say(self):
#         return ("hi,i'm not %s from %s" %(self.name, self.gender))

# ed =MDPerson("Edward","Male")
# e = ed.say()
# print(e)

def mk(n):
    return lambda x:x+n
f = mk(1)
print(f(1))
