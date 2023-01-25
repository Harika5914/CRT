#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=list('12345')
a


# In[3]:


b=list(map(int,a))  #convert the str to int
print(b)
c=list(map(float,a))
print(c)


# In[6]:


l=[1,2,3,4]
print(l)
l.append(10) #to add an element
print(l)


# In[7]:


l.insert(4,7)   #insert(position of the element,value),another method to add an element
print(l)


# In[9]:


re=l.pop()
print(re)
print(l)


# In[12]:


he=l.remove(2)


# In[13]:


print(l)


# In[ ]:





# In[18]:


le=[1,2,3,4,5]
r=le.count(1)           #count the ele repeats no of times
print(r)


# In[19]:


a=[2,4,6]
b=[4,7,9]
print(a)
a.extend(b)      # combines 2 lists
print(a)


# In[20]:


c=[9,3,6,7]
c.sort()        #sort in asscending order by default
print(c)


# In[23]:


c.sort(reverse=True) #print in decending order
print(c)


# In[26]:


#tuple
t=(1,3,4,5,6,4)

re=t.count(3)
print(re)


# In[27]:


res=t.index(4)
print(res)


# In[28]:


# set  no duplicate elements ,collection of ele with diff data types
s1={1,2,3,4}
s2={3,4,5,6}
se=s1.intersection(s2)
print(se)


# In[29]:


se=s1.union(s2)
print(se)


# In[34]:


se=s1.difference(s2)
print(se)


# In[35]:


se=s2.difference(s1)
print(se)


# In[36]:


re=s1.difference_update()
print(re)


# In[40]:


#conditions  if,else,elif
a=int(input(''))
if a%2==0:
    print('even')
else:
    print('odd')


# In[41]:


# condition ? True part:false part
a=int(input())
print('even') if a%2==0 else print('odd')


# In[2]:


d=int(input(''))
if d==1:
    print('monday')
elif d==2:
    print('tuesday')
elif d==3:
    print('wednesday')
elif d==4:
    print('thursday')
elif d==5:
    print('friday')
elif d==6:
    print('saturday')
elif d==7:
    print('sunday')
else:
    print('invalid input')


# In[5]:


n=int(input(''))
if 0<n>20 & n%2==0:
    print('weired num')
elif 20<=n>30:
    print('normal num')
elif  n<=30 & n%2!=0:
    print('normal num')
else:
    print('weirn num')


# In[5]:


#dictionary
dc={'key':'value'}
print(dc)
dc['key']


# In[10]:


dc={
    'std1':{'class':'stud1','roll':'34'},
    'std2':{'class':'stud2','roll':'3'},
    'std3':{'class':'stud3','roll':'4'}
}
print(dc['std1'])


# In[8]:



dc.update({'std3':{'valu':'4','class':'54'}})
print(dc)


# In[12]:


print(dc.get('std3'))


# In[ ]:


#range
range(start,end,step_size)


# In[9]:


list=[4,5,6,7,88]
for i in list:
    print(i,end='  & ')


# In[17]:


#program
lit=[4,6,7,8]
for i in lit:
    print(i*i)


# In[27]:


l=[ ]  #user input a list
for i in range(0,7):
    a=int(input(''))
    l.append(a)
print(l)


# In[26]:


l=[ ]  #user input a list
for i in range(0,7):
  
   l.append(i)
print(l)


# In[5]:


l=[34,56,89,67]
print(list(range(0,len(l))))


# In[13]:


#program
l=[34,56,12,36]
k=35
temp=False
for i in range(0,len(l)):
    if l[i]==k:
        print(i)
        temp=True
        
if temp==False:
    print('not found')


# In[21]:


l=[x*x*x for x in range(0,10)]
print(l)


# In[22]:


l=[x for x in range(0,51) if x%2==0]
print(l)


# In[23]:


l=[x for x in range(0,51) if x%2!=0]
print(l)


# In[32]:


l=[x for x in range(0,100) if x%7==0 and x%11==0]
print(l)


# In[2]:


l=[2,3,4,5]
for i in range(len(l),-1,-1):
    print(i)
    


# In[ ]:





# In[13]:


l='1 5 6 7 8'.split()
print(l)


# In[1]:


lis=input().split()
l=list(map(int,lis))
p,n=0,0
for i in range(0,len(l)):
    if l[i]<0:
        p=p+l[i]
        
        i=i+1
    elif l[i]>0:
        n=n+l[i]
        
        i=i+1
    else:
        print('0')
print(n+p)        


# ####     

# In[ ]:




