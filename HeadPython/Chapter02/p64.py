# Source: Chapter01/The Basics/p64.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Extending a list with objects
# Eclipse project: HeadFirstPython

'''
Created on May 4, 2019

@author: ramiro
'''

# extend: The extend method takes a second list and adds each of its objects
# to an existing list. This method is very useful for combining two lists 
# into one:


# Python list extend() method    
# Parameters   - obj: this is an object list to be added to the end of another
#                list.
# Return value - This method does not return any value.

# languages list
language = ['French', 'English', 'German']

# another list of languages
language1 = ['Spanish', 'Portuguese']

language.extend(language1)

# Extended List
print('Languages list after applying extend() method:\n', language)