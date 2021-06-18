#!/usr/bin/env python
# coding: utf-8

# #### Assignment for For Loops
# 
# 1. From range n to m, print all the numbers divisible by 5 and 7 both
# 
# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# 
#     Given:
#     number_of_terms = 5
#     
#     So series will become 2 + 22 + 222 + 2222 + 22222
#     
#     Expected output: 24690
#     
#     Hint: 'a'*2 = 'aa'

# In[6]:


# Task 1: divisible by 5 and 7 both
for j in range(5, 500):
    if j%5==0 and j%7==0:
        print(j, end=" ")


# In[5]:


# Task 2:
terms = int(input("Please enter the terms" ))
sum = 0
for i in range (1, terms+1):
    new_val = '2'*i
    #print(new_val)
    sum+=int(new_val)

print(sum)


# #### Assignment for While Loops
# 
# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)
# 
# 
# 4.  Write a loop to find the factorial of any number
# 
#     The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.
# 
#     For example: calculate the factorial of 5
# 
#     5! = 5 × 4 × 3 × 2 × 1 = 120
#     Expected output:
# 
#     120
# 
# 5. input: python language is best programming language
#     output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

# In[12]:


# Task 3:
sum = 0
while True:
    user_input = int(input("Enter number: "))
    sum += user_input
    quit_confirm = input("Press q to exit / or Enter to continue: ")
    if quit_confirm == 'q':
        break

print("Sum = {}". format(sum))


# In[7]:


# Task 4: Factorial number
number = int(input("Enter number:"))
factorial = 1
while number>0:
    factorial = factorial * number
    number = number - 1
print(factorial)


# In[2]:


# Task 5: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e
test_str = 'python language is best programming language'
res = test_str.split() 
ln = len(res)
i=0
sep=" "
final_str=""
while i < ln:
    word = res[i]
    i = i+1
    
    idx, r = 0, len(word) - 1
    while idx <= r:
        if not idx % 2 :
           final_str = final_str + word[idx].upper()
        else:
           final_str = final_str + word[idx].lower() 
        
        if(idx != r):
            final_str = final_str+'-'
        else:
            final_str = final_str+' '
            
        idx = idx+1
    #print(word)
    
print(final_str)


# In[ ]:




