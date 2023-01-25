#!/usr/bin/env python
# coding: utf-8

# In[1]:



l=[1,2,3]*3
l


# In[3]:


l='abg'*4
l


# In[5]:


#tooo: ^(XOR operator) convert into binary form   
45^49


# In[ ]:





# In[9]:


#oop
class Student:
    name=""
    roll_num=''
    branch=''
    marks=0
    attendances=0.0
    is_using_transport=False
    def view_attendence(self):
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
        
    def update_name(self,new_name):
        pass
    


# In[11]:


class Student:
    student_name='harika'
    def __init__(self,name):
        print("obj name")
        print(name)
        print(self.student_name)
s1=Student('nithisha')     #constractors   
        


# In[14]:


class Student:
    student_name='harika'
    def __init__(self,name):
        self.student_name=name
s1=Student('nithisha') 
s2=Student('satvika')
print(s1.student_name)


# In[4]:


class Student:
    student_name='harika'
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        self.student_name=new_name
s1=Student('nithisha') 
s2=Student('satvika')

print(s2.student_name)
s2.update_name('aishu')
print(s2.student_name)


# In[21]:


#program
class Bank:
    username=''
    acc_num=0
    branch=''
    def __init__(self,a,b,c):
        
    
        self.username=a
        self.acc_num=b
        self.branch=c
    
        
        print('username:',a)
        print('acc_num:',b)
        print('branch:',c)
s1=Bank('harika',123456,'rjy')  
s2=Bank('nithisha',45678,'kkd')
s3=Bank('aishu',4567890,'rjy')
print(s1.acc_num)


# In[13]:


class Bank:
    username=''
    acc_num=0
    branch=''
    __password=''
    __acc_ifc=''
    
    def __init__(self,a,b,c):
        
    
        self.username=a
        self.acc_num=b
        self.branch=c
        self.__password='random number'
        print('username:',a)
        print('acc_num:',b)
        print('branch:',c)
    def generateifc(self):
        temp=(f"ifc{self.branch}")
    
        
        print('username:',a)
        print('acc_num:',b)
        print('branch:',c)
s1=Bank('harika',123456,'rjy')  
s2=Bank('nithisha',45678,'kkd')
s3=Bank('aishu',4567890,'rjy')


# In[ ]:





# In[12]:


a=[]
a.insert(4,5)
print(a)


# In[3]:


n=int(input())
arr=[]
for i in range(n):
    a=input().split()
    if a[0]=='add':
        arr.append(int(a[1]))
    elif a[0]=='insert':
        ele=int(a[1])
        ind=int(a[2])
        arr.insert(ele,ind)
    elif a[0]=='remove':
        ele=int(a[1])
        if ele in arr:
            arr.remove(ele)
    elif a[0]=='pop':
        if len(arr)>0:
            arr.pop()
    elif a[0]=='print':
        print(arr)
    


# # 
