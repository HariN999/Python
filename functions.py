# -*- coding: utf-8 -*-
"""Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1scvTkF7JoCVx6RBlaO9Gzi1DMLYpIHNz
"""

print(dir(str))

a='hello world'
b=a.upper()
print(b)

a='HELLO WORLD'
b=a.lower()
print(b)

a='HELLO WORLD'
b=a.swapcase()
print(b)

a='HELLO WORLD'
b=a.replace('HELLO' , 'hi ')
print(b)

a='HELLO WORLD'
b=a.title()
print(b)

a='HELLO WORLD'
print(a.count('L'))

a='124easa'
b=a.isdigit()
print(b)

a=range(10)
print(a)

a=range(10)
b=list(a)
print(b)

a=list(range(5,15,2))
print(a)

def add_numbers(a,b):
    return a+b
print(add_numbers(10,20))

#Function with Default Values

def greet(name,greeting = 'hello'):
  print(f"{greeting} , {name}")
greet('hari')

#Fuction with arguments(args) - which can take n inputs

def calculate_sum(*args):
  total = sum(args)
  return total
print("sum of 1,2,3:", calculate_sum(1,2,3))
print("sum of 1,2,3,4:", calculate_sum(1,2,3,4))

"""Creating a program and adding 2 or more features to it
predefined correct username and password
"""

correct_username='admin'
correct_password='1234'
while True:
  username=input("Enter your username:")
  password=input("Enter your password:")
  if username==correct_username and password==correct_password:
    print("Login successful")
    break
  else:
    print("Invalid username or password. please try again")

def name():
  n=input()
  return n.capitalize()
print(name())

def name():
  n=input()
  return n.isnumeric()
name()

def name():
  n=input()
  return n.isalpha()
name()

def result(n):
  if n>=40:
    return 'pass'
  else:
    return 'fail'
result(50)
