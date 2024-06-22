# Password-Generator

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
