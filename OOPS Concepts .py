#!/usr/bin/env python
# coding: utf-8

# In[1]:


#class 

class MyProfile():
    def __init__(self,name,age,gender,sport):
        self.name=name
        self.age = age 
        self.gender = gender
        self.sport = sport 
        
        
    


# In[3]:


myprofile=MyProfile('Sandipan',25,'Male',True)


# In[4]:


myprofile.age


# In[14]:


#special methods 
class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages 
            
    def __str__(self):  #special method to print name of the  book and author in this self created class 
        return f'The name of the book is {self.name} and the author is {self.author}'
    
    def __len__(self):
        return self.pages


# In[15]:


b = Book('Python','Sandipan',200)


# In[16]:


print(b)


# In[17]:


len(b)


# In[24]:


class  Line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


# In[25]:


l = Line((3,2),(8,10))


# In[26]:


l.distance()


# In[27]:


l.slope()


# In[42]:


class Cylinder():
    pi = 3.14
    def __init__(self,radius =1,height = 1):
        self.radius = radius
        self.height = height
    def volume(self):
        return (self.pi* self.radius**2 * self.height)
    
    def surface_area(self):
        return (2*self.pi*self.radius*self.height) + (2*self.pi*self.radius**2)


# In[43]:


c =Cylinder(20,5)


# In[44]:


c.volume()


# In[45]:


c.surface_area()


# In[ ]:




