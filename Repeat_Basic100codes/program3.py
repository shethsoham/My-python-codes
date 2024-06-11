# How to get time of a Python program's execution


import time

def my_func():
    start_time = time.time()
    s = 0 
    for i in range (0,n):
        s = i + s
    end_time = time.time()
    return s, end_time-start_time
n  = int(input("enter the number you want"))

print(my_func())