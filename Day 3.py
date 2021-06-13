#!/usr/bin/env python
# coding: utf-8

# #### Assignment
# AGE CALCULATOR:
# 1. Calculate Age of a person - User should enter the year of birth and the program should output the age

# In[6]:


birth_yr = int(input("Please enter your birth year"))

curr_yr = 2021

age = curr_yr - birth_yr
print("Your age is {}".format(age))


# SIMPLE CALCULATOR:
# 2. get 2 numbers from the user and print the result of Addition, Subtraction, Multiplication, and floor division, decimal deivision, remainder, power of the input numbers

# In[12]:


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

add = num1 + num2
print("Addition is: {}".format(add))

sub = num1 - num2
print("Subtraction is: {}".format(sub))

mul = num1 * num2
print("Multiplication is: {}".format(mul))

floor_div = num1 // num2
print("Floor Division is: {}".format(floor_div))

dec_div = num1 / num2
print("Decimal Division is: {}".format(dec_div))

rem = num1 % num2
print("Remainder is: {}".format(rem))

power = num1 ** num2
print("Power of the numbers is: {}".format(power))

