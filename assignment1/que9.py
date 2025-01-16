#9.1
import random
mylist=[]
for i in range(1,6):
    x=random.randint(1,100)
    mylist.append(x)
print(mylist)    
#9.2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
random_num= random.randint(1,100)
print("random number is :",random_num)
if is_prime(random_num):
    print("random number is prime \n")
else:
    print("random number is not prime.") 

#9.3 rolling a die
def roll_die():
    return random.randint(1,6)
print("you rolled a ",roll_die()) 

#9.4 shuffle a list of number 
def shuffle_list(num):
    random.shuffle(num)
    return num
num=[1,2,3,4,5,6,7,8,9]
print("original list",num)
print("shuffled list",shuffle_list(num))

#9.5 random selection 
def select(items):
    return random.choice(items)
items=["apple","banana","dragonfriut","orange "]
print("randomly selected item:",select(items))

#9.6 password
import string
def gen_password(length):
    characters= string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(characters))
    for i in range(length):
        return password
    
length=int(input("enter length"))
print("generated password is:",gen_password(length))

#9.7 shuffle cards 
def pick_card():
    suits=["hearts","diamonds","clubs","spades"]
    ranks=["2","3","4","5","6","7","8","9","10","jack","queen","king","Ace"]
    rank=random.choice(ranks)
    suit=random.choice(suits)
    return f"{rank} of {suit}"
print("randomly picked card:",pick_card())