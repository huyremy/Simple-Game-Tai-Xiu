# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:24:21 2021

@author: HuyRemy
save this file to D:/py/untilted0.py and execute
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
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end=" \r")
        time.sleep(1)
        t -= 1
# input time in seconds
t = input("Enter the time in seconds. Example 5: ")
# input guess value 0 - 1 only
y = input("Enter guess value 0 - 1 only: ")
# function call
countdown(int(t))
# Get random int
number = random.randint(0,1)
print(number)
if  number==int(y):
    print("Trúng. Correct.")
    print("Bạn dự đoán là: ", y)
    print("Kết quả máy tính là: ",number)
    exec_full(r"D:/py/untitled0.py")
else:
    print("Trượt. Wrong")
    print("Bạn dự đoán là: ",y)
    print("Kết quả máy tính là: ",number)
    exec_full(r"D:/py/untitled0.py")

          
