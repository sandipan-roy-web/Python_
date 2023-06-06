#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(num1,num2):
    print(num1+num2)


# In[2]:


add(10,30)


# In[13]:


try:
    res = 10+10
    print(res)
        
except:
    print('Error has occured')
finally:
    print('Execution complete')


# In[14]:


try:
    res = 10+'10'
    print(res)
        
except:
    print('Error has occured')
finally:
    print('Execution complete')


# In[17]:


try:
    f =open('testfile.txt','r')
    f.write('Everything looks great')
except OSError:
    print('OOPs ,Something is wrong here')
finally:
    print('Execution complete')


# In[27]:


#using exceptions in a function 
def ask_for_int():
    while True:
        try:
            res=int(input('Enter a number: '))
            print(res)
            break
        except:
            print('OOPS Value entered is not a number')
            continue
        finally:
            print('Thanks for trying ')


# In[29]:


ask_for_int()


# 
