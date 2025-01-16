#8.1
def divide_numbers(num1,num2):
    try:
        result=num1/num2
        print("the result is:",result)
    except ZeroDivisionError:
        print("ERROR: divission by zero is not allowed.")


num1= float(input("enter the first number :"))
num2 =float(input("enter the second num:"))
divide_numbers(num1,num2)

#8.2
print("\n")
try:
    num=int(input("enter value"))
    print("num=",num)
except ValueError:
    print("invalid input !")
   
#8.3
def divide_num(num1,num2):
    try:
        result= num1/num2
        print("the result is",result)
    except ZeroDivisionError:
        print("error:division by zero is not allowed")
    finally:
        print("execution of try-except block is completed.")
num1=10
num2=0
divide_num(num1,num2)