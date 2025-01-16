L=[10,20,30,40,50,60,70,80]
#i
L.append(200)
L.append(300)
print("added 200 and 300",L)
#ii
L.remove(10)
L.remove(30)
print("removed 10 and 30",L)
#iii
L.sort()
print("ascending order",L)
#iv
L.sort(reverse=True)
print("descending order",L)
