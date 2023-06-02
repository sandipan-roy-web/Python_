#!/usr/bin/env python
# coding: utf-8

# In[12]:


from random import shuffle 


# In[5]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    


# In[6]:


def player_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        
        guess =input('pick a number 0,1,2')
        
    return int(guess)
                                      


# In[7]:


def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct')
    else:
        print('Wrong')
        print(mylist)
    
    


# In[13]:


#initial list 
mylist= [' ', '0', ' ']

#shuffle 
mixed_uplist = shuffle_list(mylist)

#user guess
guess = player_guess()

#result 
check_guess(mixed_uplist,guess)


# In[ ]:




