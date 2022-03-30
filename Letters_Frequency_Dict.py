# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:44:41 2022

@author: amrit
"""

#Function to enter a string and print letters in decreasing order of 
#frequency

str1 = input("Enter a string: ")

def freq(str1):
    d = dict()
    for i in str1:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    
    print(d)    
    print("In Descending order: ")
    for j in sorted(d, key = d.get, reverse=True):
        print(j, ":",d[j])
        
    #sorted_d = sorted([(value, key) for (key, value) in d.items()])
    #print(sorted_d)


print(freq(str1))



"""
str2 = freq(str1)

print(str2)

str2 = d 

str2.sort(reverse=True)
print("In descending order: ", str2)
"""
