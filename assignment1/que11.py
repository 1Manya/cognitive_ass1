#11.1
import math
def cal_sqroot(num):
    if num<0:
        return "error! square root of negative number is not real"
    else:
        return math.sqrt(num)
num =float(input("enter number"))
result=cal_sqroot(num)
if isinstance(result, str):
    print(result)
else:
    print("square root of number is :",result)    


#11.2
import datetime
def current_date_time():
    current_date_time=datetime.datetime.now()
    print("current date and time:",current_date_time)

current_date_time()

#11.3
import os
def list_file_in_current_directory():
    files=os.listdir()
    print("files in current directory :")
    for file in files:
        print(file)

list_file_in_current_directory()