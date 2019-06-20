# Source: Chapter01/The Basics/p63.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Removing objects from a list using pop()
# Eclipse project: HeadFirstPython

'''
Created on May 3, 2019

@author: ramiro
'''

# pop: takes an object’s value as its sole argument
# The pop method removes and returns an object from an existing list based on
# the object’s index value. If you invoke pop without specifying an index value,
# the last object in the list is removed and returned. If you specify an index 
# value, the object in that location is removed and returned. 
# If a list is empty or you invoke pop with a nonexistent index value, 
# the interpreter raises an error IndexError: pop index out of range.

# Python list pop() method    
# Parameters   - obj: this is the object to be removed from the list
# Return value - This method returns the removed object. Object returned by pop
#                can be assigned to a variable. in which case it is retained.
#                If the returned object is not assigned to a variable, 
#                memory is reclaimed and the object disappears.

mix = ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
print ('Original list\n', mix)
mix.pop(3)
print ('List after removing object with index 3\n', mix)

# Important
# Notice that the following code :
# mix = ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
# print ('Original list\n', mix)
# print ('Value of removed object with index 3\n', mix.pop(3) )
# 
# at line 36 prints the value of the returned object, as shown below:
# Original list
#  ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
# List after removing object with index 3
#  1984
#  
# The reason why pop() method behaves differently than remove() method is
# because pop() method returns an object. In line 29 the returned object
# (the removed object) is lost because mix.pop(3) is not assigned to
# a variable, but this is irrelevant because we are interested in line 30 
# to print the state of the list after applying pop() method.
