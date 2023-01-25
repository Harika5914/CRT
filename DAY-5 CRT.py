#!/usr/bin/env python
# coding: utf-8

# In[5]:


#inheritances
class A:
    name='harika'
    age=0
class B(A):    #single
    age=10
class C(B): #multilevel
    pass
obj=B()

print(obj.age)
print(obj.name)
obj.name='aishu'
print(obj.name)


# In[14]:


#program
class College:
    branch=""
    department='ces'
    staf='30'
    num_students=500
class Teaches(College):
    department='ece'
    staf='20'
    print('no of  staf{} in {}'.format(staf,department))
class Student(Teaches):
    num_students=200
    branch='rjy'
    staf='10'
obj=Student() 
obj1=Teaches()
obj2=College()
print(obj2.staf)
print(obj1.staf)
print(obj.num_students)


# In[15]:


#hirari
class Shopping:
    name='something'
    branches=''
    floors=0
class varity(Shopping):
    name='f'
class staff(Shopping):
    name='r'
class Manager(Shopping):
    name='h'


# In[22]:


class P1:
    def S1(self):
        print('in parent class 1')
class P2:
    def S1(self):
        print('in parent class 2')
class H(P1,P2):
    pass
obj=H()
obj.S1()


# In[23]:


class Dairyproduct:
    pass
class Milk(Dairyproduct):
    pass
class Curd(Milk):
    pass
class Buttermilk(Curd):
    pass
class Cream(Milk):
    pass


# In[5]:


from random import randint


# In[9]:


a=randint(1,10)
print(a)


# In[8]:


id=random()*1000
print(id)


# In[36]:


from random import randint,random
print('1 rock  2paper 3 scissor')

n=input()
a_score=0
b_score=0


a=input()
b=randint(1,3)

print(b)

if a==b:
    print('no one wins')

elif a==1 and b==2:
        
    if a==2 and b==1 :
        if a==3 and b==2:
            print('a wins and b lost')
            a_score=a_score+1
elif a==1 and b==3 :
    if a==2 and b==3:
        if a==3 and b==1:
            print('b wins a lost')
            b_score=b_score+1
else:
    print('enter correct value')
        


# In[38]:


class A: # runtime ploymorphism,method riding
    def method(self,a,b):
        print('sum of',a+b)
class B:
    def method(self,a,b):
        print('product is',a*b)
obj=B()
obj.method(3,5)


# In[41]:


class A: 
    def method(self,a,b):
        print('sum of',a+b)
class B:
    def method(self,a,b):
        print('product is',a*b)
    def method(self,abc):          #method overloadinng
        print('the value',abc)
obj=B()
obj.method(5)


# In[1]:


class A: 
    def method(self,a,b):
        print('sum of',a+b)
class B:
    def method(self,a,b):
        print('product is',a*b)
    def method(self,abc):          #method overloadinng
        print('the value',abc)
obj=B()
obj.method(5)   #latest method is taken ,function overloading


# In[59]:


a=int(input())
print(bin(a))
b=int(input())
print(bin(b))
c=~a^~b
print(c)
bin(c)


# In[ ]:





# In[ ]:




