# Source: Chapter01/The Basics/p62.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Removing objects from a list using remove()
# Eclipse project: HeadFirstPython

'''
Created on May 2, 2019

@author: ramiro
'''

# remove: takes an object’s value as its sole argument
# The remove method removes the first occurrence of a specified data value 
# from a list. If there are multiple occurrences, then the first such item
# is removed. If the data value is found in the list, the object that 
# contains it is removed from the list (and the list shrinks in size by one).
# This process is slow since it involves searching the item in the list
# If the data value is not in the list, the interpreter will raise a
# ValueError.

# Python list remove() method    
#                           https://www.tutorialspoint.com/python/list_remove.htm
# Parameters   - obj: this is the object to be removed from the list
# Return value - This method does not return any value but removes the given
#                object from the list

mix = ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
print ('Original list\n', mix)
mix.remove(2012)
print ('List after removing 2012\n', mix)


# Important
# Notice that the following code :
# mix = ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
# print ('Original list\n', mix)
# print ('List after removing 2012\n', mix.remove(2012) )
# 
# generates the following output:
# Original list
#  ['Python', 'C++', 'Java', 1984, 2012, 15, 2012]
# List after removing 2012
#  None
#  
# The reason why None appears is because print ('List...', mix.remove(2012) )
# proceeds to print the message, generates a line feed, and then executes the 
# remove() method, which returns nothing and print() encounters no value to 
# print and hence prints None. 
