# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:33:20 2022

@author: amrit
"""

# Fibonacci Series Program

n = int(input("Enter Number of Terms: "))

num1 = 0
num2 = 1

count = 0

if n > 1:
    print("Fibonacci Sequence for ", n, " terms is: ")
    while count < n:
        print(num1)
        
        num3 = num1 + num2
        
        num1 = num2
        num2 = num3
        
        count = count + 1
        
elif n == 1:
    print("Fibonacci Sequence for ", n, " term is: ", num1)
    
else:
    print("Fibonacci Series doesnt exist!!")
    
