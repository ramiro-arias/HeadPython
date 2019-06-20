# Source: Chapter01/The Basics/p11_1.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# Working with dates (and times) comes up a lot, and the standard library
# provides the datetime module to help when you are working with this type
# of data. The date.today function provides today’s date:

import datetime
print("Today's date:", datetime.date.today())