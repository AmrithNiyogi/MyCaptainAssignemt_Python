# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:55:04 2022

@author: amrit
"""

#positive numbers in a given range

list_no = []

n = int(input("Enter list length: "))

print("Enter Values: ")

for i in range(0, n):
    num = int(input())
    list_no.append(num)

print(list_no)

print("Positive Numbers from ", list_no, " are: ")

for i in list_no:
    if i >= 0:
        print(i)
        