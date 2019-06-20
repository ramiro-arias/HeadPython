# Source: Chapter01/The Basics/p10_1.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# The sys module exists to help you learn more about your interpreter’s system.
# Here is how to determine the identity of your underlying operating system, 
# by first importing the sys module, then accessing the platform attribute:

import sys
OS = sys.platform
print("Underlying operating system:", OS)