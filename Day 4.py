#!/usr/bin/env python
# coding: utf-8

# 1) use string functions to count the occurrence of 'y' in a word given by user.
# 
# 2) take input of a string and print it's even indexed characters
# 
# 3)create a program to swap case. Using string functions
# Input : EdUyEaR
# Output :.  eDuYeAr

# In[9]:


# task 1
word = input("Please enter the word: ")

y_count = word.count('y')
print("In the given word the occurrences of 'y' is {} times".format(y_count))


# In[10]:


# task 2
word = input("Please enter the string: ")
evn_idx_chars = word[2::2]
print("Even indexed characters of the given string is: {}".format(evn_idx_chars))


# In[11]:


# task 3
#word = "EdUyEaR"
word = input("Please enter the input: ")
#print(dir(str))
after_swap = word.swapcase()
print("After the swap case output is: {}".format(after_swap))

