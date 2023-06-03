#!/usr/bin/env python
# coding: utf-8

# In[3]:


def checkEven(number):
    even_number=[]
    for num in  number:
        if num%2==0:
            even_number.append(num)
    
    return even_number


# In[4]:


checkEven([1,2,5])


# In[7]:


checkEven([1,3,5])


# In[8]:


#tuple unpacking in a function 

Emp_hours=[('Ram',1000),('Sham',10000),('Abhinay',10)]

def employee_month(Emp_hours):
    emp_month= ''
    hours = 0
    for emp ,hour in Emp_hours:
        if hour>hours:
            hours=hour
            emp_month=emp
    return emp_month,hours



    


# In[14]:


name, ho = employee_month(Emp_hours)
print(name)


# In[15]:


print(ho)


# In[20]:


def ran_check(num,low,high):
    if num>=low and num<=high :
        print(f'number {num} is in the range between {low} and {high}')
    else:
        print(f'The number {num}is not in the range between {low} and {high}' )


# In[21]:


ran_check(2,8,9)


# In[22]:


ran_check(1,1,5)


# In[46]:


S='Hello Mr. Rogers, how are you this fine Tuesday?'

    


# In[84]:


def check_cases(s):
    d = {"upper": 0, "lower": 0}
    for word in s:
        if word.isupper():
            d['upper'] += 1
        elif word.islower():
            d['lower'] += 1
        else:
            pass
    print("The number of upper case characters =" ,d['upper'])
    print("The number of lower case characters =", d['lower'])


            
    


# In[85]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
check_cases(s)


# In[91]:


def unique_check(m_lis):
    x=[]
    for a in m_lis:
        if a not in x:
            x.append(a)
            
    return x


# In[92]:


lis=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
res=listunique_check(lis)
print(res)


# In[93]:


list(set(lis))


# In[94]:


def mult_num(mylist):
    prod=1
    for num in mylist:
        prod = prod*num
        
    return prod 


# In[96]:


l=[1,2,3,-5]
mult_num(l)


# In[97]:


#palindrome 
def check_reverse(st):
    return st[::-1]==st


# In[98]:


check_reverse('bab')


# In[99]:


check_reverse('dad')


# In[101]:


check_reverse('sand')


# In[ ]:




