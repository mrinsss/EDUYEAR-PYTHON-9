#!/usr/bin/env python
# coding: utf-8

# Common part ->  Create a list of n numbers
# 
# 
# Q1. Count even numbers and odd numbers
# 
# Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())
# 
# Q3. Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't
# 
# Q4. Print the numbers which are palindrome inside the list

# In[7]:


# Q1
n1 = 11
n2 = 31

my_list = list(range(n1, n2+1))
print(my_list)

even_cnt, odd_cnt = 0, 0

for num in my_list:  
    if num % 2 == 0:
        even_cnt += 1  
    else:
        odd_cnt += 1
          
print("Even numbers in the list: {}".format(even_cnt) )
print("Odd numbers in the list: {}".format(odd_cnt) )


# In[10]:


# Q2
minimum = maximum = my_list[0]
# now loop through from next elements
for i in my_list[1:]:
    if i < minimum: 
        minimum = i 
    else: 
        if i > maximum: 
            maximum = i            

print("Maximum number in the list: {}".format(maximum) )
print("Minimum number in the list: {}".format(minimum) )


# In[16]:


# Q3 whole list is plaindrome or not
list1 = [11,21,11]
#list1 = [1,2,12]

list2 = list1.copy()  
list2.reverse()  

if list1 == list2:
    print("Palindrome") 
else:
    print("Not Palindrome") 


# In[17]:


# Q4 numbers inside the list which are palindrome
full_list = [10, 111, 220, 498, 787, 363, 121, 133, 784, 565, 155, 141, 252] 

for i in full_list:   
    num = i 
    rev = 0
    while num > 0: 
        rev = rev * 10 + num % 10
        num = num // 10

    if rev == i: 
        print (i) 

