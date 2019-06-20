# Source: Chapter01/The Basics/p60.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Checking for membership with in
# Eclipse project: HeadFirstPython

'''
Created on May 2, 2019

@author: ramiro
'''

# As well as using the 'in' operator to check whether an object is contained
# within a collection, it is also possible to check whether an object does 
# not exist within a collection using the not in operator combination.
# Using not in allows you to append to an existing list only when you know
# that the object to be added is not already part of the list:

# Let us define a list of vowels:
vowels = ['a', 'e', 'i', 'o', 'u']

word   = 'Milliways'
found  = []                       # empty list

# We can check if one object is contained within a collection with operator 'in'
for letter in word:
  if letter in vowels:
    if letter not in found:
      found.append(letter)        # letter appended to found only once
      
print ('Vowels contained in', word)
for vowel in found:
  print (vowel)