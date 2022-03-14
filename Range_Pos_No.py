# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:55:04 2022

@author: amrit
"""

#positive numbers in a given range

a = int(input("Enter starting of the range: "))
b = int(input("Enter ending of the range: "))

for i in range(a, b + 1):
    if i >= 0:
        print(i)