#!/usr/bin/env python
# coding: utf-8

# In[80]:


#Write a program to create a 5 dimensional array with all zeros and ones#
import numpy as np
b=np.shape=(1,1,1,1,1)
a=np.random.randint(2,size=b)


# In[84]:


a


# In[118]:


a


# In[ ]:


#
2) Write a program to create an array of 10 zeros,10 ones, and 10 fives in row 1 2 and 3 which create a new array of shape (3,10)


# In[131]:


a=np.zeros((2,2,2,2,2))
a


# In[132]:


a.ndim


# In[127]:


b=np.ones((3,2,2,2,2))
b


# In[136]:


#3) Write a program to create a 3x4 matrix filled with values from 10 to 21.

a=np.arange(10,22).reshape(3,4)
a


# In[141]:


#4) Write a  program to create a 10x10 zero matrix with elements on the main diagonal equal to 0,1,2,3,4,5,6,7,8,9,

a=np.diag([0,1,2,3,4,5,6,7,8,9])
a


# In[150]:


#5)Write a program to create a 4x4 array. Create an array from below array by swapping first and last, second and third columns.
a=np.arange(1,17).reshape(4,4)
print(a)
print(a[:,::-1])


# In[151]:


#6) Write a program to reverse an array (the first element becomes the last).
#Given array:
#[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ]

a=np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
a[::-1]


# In[155]:


#) Write a program to access all the elements greater than 30 and less than 80 and multiples of 5 from an array of shape 10,10 .Elements range from 1 to 100
a=np.arange(1,101).reshape(10,10)
y=(a>30) & (a<80) & (a%5==0)
a[y]


# In[186]:


#8) Write a program to create a 2D array with 1 on the border and 0 inside.
a=np.zeros((5,5))
a[0:1]=1
a[-1:]=1
a[:,0:1]=1
a[:,-1:]=1
a


# In[225]:


#9) Write a program to create a checkerboard pattern .Don't use default array function
#Checkerboard pattern:                                                   
#[[0 1 0 1 0 1 0 1]                                                      
 #[1 0 1 0 1 0 1 0]                                                      
 #[0 1 0 1 0 1 0 1]                                                      
 #[1 0 1 0 1 0 1 0]                                                      
 #[0 1 0 1 0 1 0 1]                                                      
 #[1 0 1 0 1 0 1 0]        

a=np.zeros((8,8))
a[1::2, ::2] = 1
a[::2, 1::2] = 1
a


# In[206]:


#10) Write a program to find common values between two arrays.
#Expected Output:
#array1: [10 20 40 60]
#array2: [10, 30, 40,50]

a=np.array([10,20,40,60])
b=np.array([10,30,40,50])
a[a==b]


# In[212]:


#11) Write a program to create an array 2d array and then reshape into 1d array
a=np.arange(1,10).reshape(3,3)
print('2d ',a)
print('single dimension',a.reshape(9,))


# In[ ]:


#
12) Write a user defined function for creating a 1 or 2d array from scratch without using array functions

