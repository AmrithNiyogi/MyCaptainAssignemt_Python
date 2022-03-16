# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:36:49 2022

@author: amrit
"""

#Accpeting File Name and printing extension

fname = input("Enter file name: ")

fext = fname.split(".")

print ("Extension of the file is : " + fext[-1])

a = fext[-1]

print(a)

if a == 'py':
    print("File Type: Python")
    
elif a == 'cpp':
    print("File Type: C++")

elif a == "java":
    print("File Type: Java")
    
elif a == "txt":
    print("File Type: Text")
    
elif a == "docx":
    print("File Type: Word Document")
    
elif a == "pptx":
    print("File Type: Powerpoint Presentation")
    
elif a == "jpg" or a == "jpeg":
    print("File Type: Picture")
    
elif a == "mp3":
    print("File Type: Audio")

elif a == "mp4":
    print("File Type: Video")
    
else:
    print("INVALID FILE TYPE")