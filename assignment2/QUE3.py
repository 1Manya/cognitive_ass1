import random
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=[random.randint(100,900)for i in range(100)]
print("list of number",num)
#i -all odd num
odd_num=[n for n in num if n%2!=0]
print("odd number's list",odd_num)
print("count of odd number:",len(odd_num))

#ii -all even num
even_num=[n for n in num if n%2==0]
print("even number's  list:",even_num)
print("count of even number:",len(even_num))
#iii - prime number 
prime_num=[n for n in num if is_prime(n)]
print("all prime number's list:",prime_num)
print("count of prime number=",len(prime_num))