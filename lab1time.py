from linear import linear_search
from binary import binary_search
import time

def create_arr(n):
    return [i for i in range(n+1)]

def linear_time(arr):
   start_time= time.time_ns()
   linear_search(arr,arr[-1])
   end_time=time.time_ns()
   time_taken=end_time - start_time

   return time_taken

def binary_time(arr):
   start_time1=time.time_ns()
   binary_search(arr,arr[-1])
   end_time1=time.time_ns()
   time_taken1=end_time1- start_time1
   return time_taken1 

for i in range(10):
   arr = create_arr(10000*i) #change to 500,000 for binary
   print(binary_time(arr))
   print(linear_time(arr))

