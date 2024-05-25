# Password-Generator

# Q. Create a password 10.generator that can input the number of letters in your password should have,
# the number of symbols and the number of numbers and create a basic level password. and then in other programme
# you can modify it to advanced level or hard level password.
# Example...
# How many letters do you want in your password?
# 4.constants
# How many numbers you want?
# 2
# How many symbols you want?
# 2
# Password : EMVz%*34


import random as rm
import string as str

print('''
********************************************************
------------ WELCOME TO PASSWORD GENERATOR -------------
********************************************************
''')
lett=int(input('How many letters you want in your password? '))
l=str.ascii_letters
random_letters=rm.sample(l,lett)

num=int(input("How many numbers you want in your password? "))
n=str.digits
random_number=rm.sample(n,num)

sym=int(input("How many symbols or special characters you want in your password? "))
s=str.punctuation
random_symbol=rm.sample(s,sym)

pw=''.join(random_letters+random_number+random_symbol)
pwl=list(pw)
rm.shuffle(pwl)

password=''.join(pwl)
print(f'your password is: {password}')

#**************************************************************************************************
# another method:::

# import random as rm
#
# l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#
# s=["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=",
#    ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
#
# n=['0','1','2','3','4.constants','5','6','7','8','9']
#
# letters=int(input('How many letters you want in your password? '))
# symbols=int(input('How many symbols you want in your password? '))
# numbers=int(input('How many numbers you want in your password? '))
#
# password_list=[]
# for i in range(1,letters+1):
#     char1= rm.choice(l)
#     password_list += char1
#
# for j in range(1,symbols+1):
#     char2= rm.choice(s)
#     password_list += char2
#
# for k in range(1,numbers+1):
#     char3 = rm.choice(n)
#     password_list += char3
#
# rm.shuffle(password_list)
# password=''
# for char in password_list:
#     password += char
#
# print(f'your password is: {password}')
