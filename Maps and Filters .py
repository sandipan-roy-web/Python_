#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square(num):
    return num**2


# In[2]:


num=[3,5,9]


# In[3]:


list(map(square,num))


# In[9]:


def  print_even(name):
    if len(name)%2==0:
        return name
    else:
        return name[0]


# In[10]:


my_name=['sandipan','austin','rahul','ani']


# In[11]:


list(map(print_even,my_name))


# In[12]:


#filters
def even_check(num):
     return num%2==0
    


# In[13]:


ll=[1,2,3,4,5,6,7,8,9]


# In[14]:


list(filter(even_check,ll))


# In[16]:


#lambda expressions 
list(map(lambda x: x**2,ll))


# In[17]:


list(map(lambda x : x[0],my_name))


# In[ ]:




