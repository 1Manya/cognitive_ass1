#5.1
lst=[]
num=int(input("enter total num is list"))
for i in range(num):
    nm=int(input("enter num "))
    lst.append(nm)
print("largest num ",max(lst))  
print("smallest num ",min(lst))

#5.2
D={1:"one",2:"two",3:"three",4:"four"}
print("value is ",D.get(2))
#5.3
list1=[]
total= 5
for i in range(1,total):
    numb=int(input("enter val"))
    list1.append(numb)

list1.sort()
print("ascending order",list1)
list1.reverse()
print("descending order",list1)

#5.4
dic1={1:"a",2:"b"}
dic2={3:"c",4:"d"}
dic3={**dic1,**dic2}
print("merging dictionary",dic3)


       
