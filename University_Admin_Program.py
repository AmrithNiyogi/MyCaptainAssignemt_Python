# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:28:20 2022

@author: amrit
"""
#School Administration Program

#importing packages for writing into the file
import csv


def write_csv(infolist):
    
    """
    :infolist - argument storing the list given by user
    :Student_Information.csv - file created to store the data
    :'a' - opened in append mode
    :writer class object - csv.writer
    :csv_file.tell() - used to make sure the header is printed only when the file is created to acoid repetition of itself
    :writerow - function of writer class used to write in rows (can only take string arguments)
        a. First writer.whiterow function is used to add the headers of the file
        b. add the input given by user to file

    """
    with open("Student_Information.csv", 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Phone_No", "Email_Id", "Course", "Batch", "Semester", "Year"])
        
        writer.writerow(infolist)
        
#----------------Function end ------------------------

if __name__ == '__main__':

    condition = True
    student_num = 1
    
    while condition:
        #single space gap to given while entering information
        sinfo = input("Enter student information for student #{} in the format: (Name Age Phone_Number email_id Course Batch Semester Year): \n".format(student_num))
        
        #spliting the entered information into a list format        
        sinfo_list = sinfo.split(' ')
        
        print("\nEntered Student Information is - \nName: {} \nAge: {} \nPhone_Number: {} \nEmail_Id: {} \nCourse: {} \nBatch: {} \nSemester: {} \nYear: {}"
                  .format(sinfo_list[0], sinfo_list[1], sinfo_list[2], sinfo_list[3], sinfo_list[4], sinfo_list[5], sinfo_list[6], sinfo_list[7], 
                          sinfo_list[8]))
        
        """
            :check_info - used as a variable to check if entered information is correct or not
            Use a condition to make sure that the entered yes/no is either all in 'caps' or 'lowercase' depending on the if-statement's argument
            
        """
        check_info = input("Is entered information correct (yes/no): ")
        check_info.lower()
        
        if check_info == "yes":
        
            #calling the write_cvs function
            #string argument sinfo is first being converted to a string thenb split into a list so that the writer class functions can be used.
            write_csv(sinfo_list)
            
            """
            :check_condition - used as a variable to continue or stop the addition of new elements into the list.
            Use a condition to make sure that the entered yes/no is either all in 'caps' or 'lowercase' depending on the if-statement's argument
            
            """
            
            check_condition = input("Enter another students information (yes/no): ")
            check_condition.lower() #converting the entered information into lowercase
            
            if check_condition == "yes":
                condition = True
                student_num = student_num + 1
            elif check_condition == "no":
                condition = False
                
        elif check_info == "no":
            print("\nPlease re-enter values.")