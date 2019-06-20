# Source: Chapter01/The Basics/p65.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Inserting an object into an existing list
# Eclipse project: HeadFirstPython

'''
Created on May 4, 2019

@author: ramiro
'''

# insert: The insert method inserts an object into an existing list before
# a specified index value. This lets you insert the object at the start of
# an existing list or anywhere within the list. It is not possible to insert
# at the end of the list, as that is what the append method does:

# Python list insert() method    
# Parameters   - index: position where an object needs to be inserted
#              - object: this is the ojbect to be inserted in the list 
# Return value - This method does not return any value.

# languages list
language = ['French', 'English', 'German']

# another list of languages
object = 2048

language.insert(1, object)

# Extended List
print('Languages list after applying insert() method:\n', language)

# Output
# Languages list after applying insert() method:
#  ['French', 2048, 'English', 'German']