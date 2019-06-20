# Source: Chapter01/The Basics/p56.py
# Book: Head First Python (2nd Edition) - Paul Barry
# Name in the book: Working with lists
# Eclipse project: HeadFirstPython

'''
Created on May 2, 2019

@author: ramiro
'''

# We will use the shell to first define a list called vowels, then check to see if
# each letter in a word is in the vowels list. Let us define a list of vowels:
vowels = ['a', 'e', 'i', 'o', 'u']

# With vowels defined, we now need a word to check, so let’s create a
# variable called word and set it to "Milliways":
word   = 'Milliways'

print ('Vowels contained in', word)

# We can check if one object is contained within a collection with operator 'in'
for letter in word:
  if letter in vowels:
    print (letter)