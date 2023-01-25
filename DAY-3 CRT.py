#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={
    'key1':'value1'
}
d.update({'key2':'user name'})
d.update({'key3':'cse'})
d.update({'key4':' name'})
for i in d:
    print(i)


# In[2]:


d={
    'key1':'value1'
}
d.update({'key2':'user name'})
d.update({'key3':'cse'})
d.update({'key4':' name'})
for i in d:
    print(d[i])


# In[3]:


l=[]    #user input dictionary values imp
for i in range(2):
    d={
        
        'key1':input(),
        'key2':input()
    }
    l.append(d)
print(l)    


# In[4]:


l=[]    #user input dictionary values imp
d={}
for i in range(4):
    d.update({
        'key1':input(),
        'key2':input()
    })
    l.append(d)
print(l)    


# In[5]:


db={'qwe@example.com':'ertyu',
   'ghj@gmail.com':'yuio',
   'opkl@xml.com':'vbnm',
   'uioopj@gmail.com':'asdfg'}  
print(db)
username=input( )
password =input( )

for i in db:
    if i==username:
        if password==db[i]:
            print('correct')
        else:
            print('wrong')
        break
    else:
        print('not found')
    break    


# In[7]:


db=[
    {'qwe@example.com':'ertyu'},
   {'ghj@gmail.com':'yuio'},
   {'opkl@xml.com':'vbnm'},
   {'uioopj@gmail.com':'asdfg'}]
print(db)
username=input( )
password=input( )
temp={username:password}

if temp in db:
    print('found')
else:
    print('not found')


# In[8]:


row=3
col=3
arr=[]
for i in range(row):
    element=[]
    for j in range(col):
        element.append(int(input(' ')))
    arr.append(element)
print(arr)    


# In[9]:


# sum of matrix imp
row=3
col=3
arr=[]
for i in range(row):
    temp=input('').split()
    ele=list(map(int,temp))
    arr.append(ele)
print(arr)    
arr1=[]
for i in range(row):
    temp=input('').split()
    ele=list(map(int,temp))
    arr1.append(ele)
print(arr1)    
res=[[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        res[i][j]=arr[i][j]+arr1[i][j]
print(res)        


# In[10]:


a=[[2,3,4,5],
  [5,6,7,8],
  [7,8,9,1]]
print(a[0])


# In[1]:


temp=[]
a=input('').split()
b=list(map(int,a))
print(a)
print(b)


# In[2]:


#sliceing
l=[1,2,3,4,55,66,7]
print(l)
l[0:6]
print(l[:5])
print(l[::2])
print(l[::-1])
print(l[5])
l[-4]


# In[ ]:





# In[14]:


#strings and methods
s="hello world"
print(s)
print(s.capitalize())


# In[15]:


res=s.split()
print(res)


# In[16]:


'-'.join(res)


# In[17]:


print(s.title())


# In[23]:


s1="Hello world"
s2="HII"
print(s2.lower())
print(s1.upper())


# In[31]:


#common methods in string and list
res=s1.isdigit( )      #check wherther is number
print(s1.isdecimal())
print(res)


# In[25]:


re=s1.swapcase() #prints lower as upper and upper as lower
print(re)


# In[29]:


n="dfghj"
print(n.isalpha())


# In[30]:


first="mr.x"
age=89
last="year old"
print("mr.x {} year old".format(age))   #format method 


# In[33]:


num=5
print('the square of {} is{} '.format(num,num*num))


# In[37]:


num=8.9
print('the square of {:10}is{:.3f}'.format(num,num*num))


# In[40]:


print(f'the square of {num} is {num*num:.8f}')


# In[43]:


#exception handlings         try,except
a=int(input())
b=int(input())
try:
    
    print(a/b)
except:
    print('b cannot be 0')
print('after the error')    


# In[55]:


#program
a=int(input())
b=int(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    try:
        print(a/b)
    except:
        print('b not be 0')
else:
    print('enter correct value')


# In[66]:



try:
    for i in range(6):
        int(input())
except :
    print('enter only integers')


# In[67]:


print(eval('1+3/5*9'))


# In[70]:


# regular functions 
def addition(num1,num2):
    r=num1+num2
    return r
print(addition(1,6))


# In[81]:


def primary(num):
    count=0
    for i in range(1,num+1):
        if num%i!=0:
            print(' prime')
            break
        else:
            print('not prime')
print(primary(8))            


# In[ ]:


""""#prime numbers log
import math
n=23
#method 1
for i in range(1,num+1):  #23 iterations
    pass
#method2
for i in range(2,num): #21
    pass
#method3
for i in range(2,num//2):  #10 iterations
    pass
#method4

for i in range(2,int(num**0.5)+1):  #3 iteration
    pass
""""


# In[84]:


#default value funtions         
def add(num1,num2=0):    #to avoid error if we enter add(1)then num2 takes 0 as default value
    return num1+num2
a=10
b=10
res=add(a)
print(res)


# In[87]:


#keyword argument function
def add(num1,num2):    
    print(num2)
    print(num1)
add(num2=9,num1=10)


# In[89]:


add(4,num1=0)  #IT shows error because multiple values for argument 'num1'


# In[91]:


#variable length argument
def add(*abc): # takes any no of vriables
    print(abc)
add('hell',8,0.9)    


# In[93]:


def add(*abc):
    res1=1
    for i in abc:
        res1+=i
    return res1
print(add(10,2,9,5))


# In[95]:


def add(a,b,*abc):
    print(a)
    print(b)
    print(abc)
print(add(10,2,9,5))


# In[96]:


#recuurtion is calling itself
def check(n):
    print(n)
    if n>0:
        check(n-1)
check(5)        


# In[ ]:




