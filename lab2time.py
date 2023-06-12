import random 
from merge import merge_sort
from insertion import insertion_sort
import time

def insert_time(data):
    start_time= time.time_ns()
    insertion_sort(data)
    end_time=time.time_ns()
    time_taken=end_time- start_time
    return time_taken

def merge_time(data,n):
    start_time1= time.time_ns()
    merge_sort(data,0,n-1)
    end_time1=time.time_ns()
    time_taken1=end_time1- start_time1
    return time_taken1

for i in range(1,11):
    n=i*1000
    data=[random.randint(1, n) for _  in range(n)]
    print(insert_time(data))
    print(merge_time(data,n))
