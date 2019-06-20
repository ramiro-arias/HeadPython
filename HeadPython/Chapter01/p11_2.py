# Source: Chapter01/The Basics/p11_2.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# You can access the day, month, and year values separately by appending
# an attribute access onto the call to date.today:

import datetime
print ("Day:  ", datetime.date.today().day)
print ("Month:", datetime.date.today().month)
print ("Year: ", datetime.date.today().year)