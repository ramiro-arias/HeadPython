# Source: Chapter01/The Basics/p10_3.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Up close with the standard library
# Eclipse project: HeadFirstPython

'''
Created on Apr 4, 2019

@author: ramiro
'''
# You can access your system’s environment variables, as a whole (using the
# environ attribute) or individually (using the getenv function):

import os
print("Environment variables:\n", os.environ)