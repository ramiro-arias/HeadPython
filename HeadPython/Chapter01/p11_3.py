# Source: Chapter01/The Basics/p11_3.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# Can the standard library tell us what time it is? Yes. After importing 
# the time module, call the strftime function and specify how you want
# the time displayed. In this case, we are interested in the current 
# time’s hours (%H) and minutes (%M) values in 24-hour format:

import time
print("Time is now:", time.strftime("%H:%M"))