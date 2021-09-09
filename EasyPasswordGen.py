#!/bin/python3
import random

print ("=============================")
print ("|Password Generator by Redid|")
print("=============================")

chars = 'qwertyuiopasdfghjklzxcvbnm123456789#@?!-_*'

length = input('password length?')
length = int(length)

for p in range(10):
  password =  ''
  for c in range(length):
    password += random.choice(chars)
  print(password)


print ("Thanks for using!")