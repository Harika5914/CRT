#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Animal:
    def cat_bark(self):
        print('cat barks')
    def dog_bark(self):
        print('dog barks')
    def cow_bark(self):
        print('cow barks')
class Cat(Animal):
    def cat_bark(self):
        print('meowwwww........meowwwww')
class Dog(Animal):
    def dog_bark(self):
        print('bowww boww boww')
    def talk(self):
        print(' hehehe')
class Cow(Animal):
    def cow_bark(self):
        print('............')
obj=Cow()
obj.cow_bark()
obj1=Dog()
obj1.talk()


# In[2]:


from abc import ABC,abstractmethod


# In[3]:


class Area(ABC):
    @abstractmethod
    def calulate_area(self):
        pass
        #print('in calculate area')
class Square(Area):
    def calulate_area(self):
        print('in square method')
class Rectangle(Area):
    pass
ob=Square()
ob.calulate_area()
    
    


# In[4]:


class Perimeter(ABC):
    @abstractmethod
    def calulate_diameter(self):
        pass
    def calulate_area(self):
        pass
    def radius(self):
        pass
class Square(Perimeter):
    def calulate_diameter(self):
        print('in square')
    def calulate_area(self):
        pass
    def radius(self):
        pass
class Rectangle(Perimeter):
    def calulate_diameter(self):
        pass
    def calulate_area(self):
        print('in rectangle area')
    def radius(self):
        print('radius')
obj=Rectangle()
obj.calulate_area()


# In[1]:


#shift
print(1<<2)
#16 8 4 2 1
#0 0 0 0 1==1
#0 0 1 0 0==4


# In[2]:


print(7<<3)


# In[3]:


print(11<<3)  #now 11*2=22 ,22*2=44, 44*2=88 lelf shift


# In[4]:


print(7>>1)  #7/2=3


# In[5]:


print(7>>2) #7/2=3  3/2= 1    right shift


# In[ ]:




