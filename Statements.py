#!/usr/bin/env python
# coding: utf-8

# In[1]:


st = 'Print only the words that start with s in this sentence'


# In[3]:


st1=st.split(' ')
st1


# In[10]:


for word in st1:
  if word.startswith('s'):
      print(word)


# In[11]:


for i in range(0,11):
    if i%2==0:
        print(i)


# In[17]:


[i  for i in range(1,50) if i%3==0]


# In[19]:


for word in st.split():
    if word[0].lower() =='s':
        print(word)


# In[20]:


[word for word in st.split() if word[0].lower() == 's']


# In[21]:


total=len(st)
if total%2==0:
    print('even')
else:
    print('odd')


# In[23]:


st1 = 'Create a list of the first letters of every word in this string'

[word[0] for word in  st1.split()]
   


# In[ ]:




