# Source: Chapter01/The Basics/p65a.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Inserting a list into an existing list in any position
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

# another list
dialect = ['Aymara', 'Quechua', 'Nahuatl']
pos = 1
language.insert(pos, dialect)

print('Languages list after applying insert() method:\n', language)

# What you got was that the dialect list was inserted into the language
# list. But what if you need the elements of the dialect listo inserted
# into the language list?
language = ['French', 'English', 'German']
language[pos:pos] = dialect
print('Languages list after applying insert() method:\n', language)


# Output
# Languages list after applying insert() method:
#  ['French', ['Aymara', 'Quechua', 'Nahuatl'], 'English', 'German']
# Languages list after applying insert() method:
#  ['French', 'Aymara', 'Quechua', 'Nahuatl', 'English', 'German']