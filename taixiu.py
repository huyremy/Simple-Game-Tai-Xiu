# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:21:24 2021
@author: HuyRemy 
save this file to D:/py/taixiu.py and execute
"""
# import the time module
import time
import random
#define exec full
def exec_full(filepath):
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)  
# define the countdown func.
def countdown(t):    
    while t:
        print(t, end=" \r")
        time.sleep(1)
        t -= 1
# input time in seconds
t = 6
# input guess value 0 - 1 only
y = input("0 = Tài, 1 = Xỉu. Input your guess: ")
# function call
countdown(int(t))
# Get random int
number = random.randint(0,1)
no1 = random.randint(1,6)
no2 = random.randint(1,6)
no3 = random.randint(1,6)
print()
print("-------")
print(no1)
print(no2)
print(no3)
print("-------")
no = [no1,no2,no3]
result = sum(no)
if result % 2 == 0:
    print(result,"điểm --> Tài")
else:
    print(result,"điểm --> Xỉu")
if  number==int(y):
    print("Bạn dự đoán là: ", y)
    print("Kết quả máy tính là: ",number)
    print("Trúng. Correct. Congratulations !")
    exec_full(r"D:/py/taixiu.py")
else:
    print("Bạn dự đoán là: ",y)
    print("Kết quả máy tính là: ",number)
    print("Trượt. Wrong. What's a pity !")
    exec_full(r"D:/py/taixiu.py")
