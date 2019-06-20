# Source: Chapter01/The Basics/p10_4.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# You can access a specifically named attribute (from the data contained
# in “environ”) using “getenv”.

import os
print("Environment variable 'IDE_PROJECT_ROOTS':\n", os.getenv('IDE_PROJECT_ROOTS'))