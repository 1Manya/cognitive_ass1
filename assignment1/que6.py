#6.1
def count_vowel(s):
    vowel="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowel:
            count +=1
    return count

s=input("enter a string")
print("number of vowels",count_vowel(s))

#6.2
def reverse_string(str):
    return str[::-1]

str=input("enter string to reverse")
print("reversed string is",reverse_string(str))

#6.3
def is_palindrome(s2):
    s2=s2.lower()
    return s2==s2[::-1]

s2=input("enter string")
if is_palindrome(s2):
    print("the string is palindrome")
else :
    print("the string is not a palindrome")