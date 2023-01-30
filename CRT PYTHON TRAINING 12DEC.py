#!/usr/bin/env python
# coding: utf-8

# # happy number

# In[2]:


def happ(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum

num=int(input())
result=num
while(result!=1 and result !=4):
    result=happ(result)
if result==1:
    print("Happy number")
else:
    print("not happy")


# In[5]:


num=str(input())
print(int(num,17))


# In[ ]:





# In[3]:


def harshn(n):
    r=0
    sum=0
    while (n>0):
        r=n%10
        sum=sum+r
        n=n//10
        return sum
n=int(input())
s=harshn(21)
if(21%s==0):
    print("harsh")
else:
    print("not harsh")
     


# BASIC PROGRAMS
# 

# In[9]:


#WAP to convert F into c

f=float(input("enter the farenheit value:"))
c=(0.58)*f-32
print(c)


# In[15]:


#WAP  TO CHECK GIVEN NUMBER IS POSITIVE
n=int(input())
if n>0:
     n=n+10
     print(n)
     
else:
    print("Negative")


# In[9]:


#WAP TO DETERMINE THE CHARACTER ENTERD
ch=(input("enter any key:"))
print(ch.isalpha())
print(ch.isdigit())
print(ch.isidentifier())


# In[23]:


#WAP  TO FIND A TEXT PRESENT IN THE I/P SENTENCE OR NOT 
#txt="Telangana is a state"
txt=(input())
ch=(input())
if(ch in txt):
    print("present")
else:
    print("not present")
     


# In[8]:


#MISSISSIPPI
a="MISSISSIPPI"
print(a.split("S"))
print(a.lower())
for  i in reversed(a):
    print(i)
     


# In[23]:


abc="saiganesh"
abc[1]
abc[1:3]
ab="INDIA"
ab[1:3]
print(len(ab))


# In[40]:


abc=""" netherlands australia greece"""
abc1=""" netherlands australia greece"""
print(abc)
if "australia" in abc:
         print("yes its there")
print(abc==abc1)


# In[ ]:





# In[ ]:


a.


# In[ ]:





# In[45]:


#method using sum
def ls(string):
    
    return sum(l for i in string)
string='india'
print(ls(string))
    
    


# In[46]:


#counter 
def ls(str):
    c=0
    for i in str:
        c=c+1
    return c
str='SAI'
print(ls(str))

#join method and count

def ls(str):
    if not str:
        return 0
    else:
        r_str='py'
        return ((r_str).join(str).c(r_str)+1)
            
str()


# partition()-->return tuple
# find()------->return index of 1st substring 
# replace()---->replacing the substring
# split()------>
# startswith()--->
#  startswith(india)
# endswith()------>
# index()--------->

# In[50]:


str1="india is a rich country"
str1.startswith("india")


# In[51]:


#formatting strings
name='sai' #use only single quotes
country='india'
print(f'{name} is  born in {country}')


# In[60]:


#sets
m_set={1,2,3,4,5}
m_set2={1,2,3.0,4.5,"abc",(6,8,9)}
print(m_set2)
print(m_set)
print(type(m_set2))
x={}
print(type(x))
y=set()
print(type(y))


# In[68]:


#modifying a set
m_set={1,3}
m_set.add(2)#add
print(m_set)
m_set.update([2,3,4])
print(m_set)
m_set.update([5,6],{4,7})
print(m_set)


# In[96]:


m_set=set("abcdef")
print(m_set)
m_set.pop()
print(m_set)

m_set.pop()
print(m_set)

m_set.pop()
print(m_set)

m_set.pop()
print(m_set)


m_set.pop()
print(m_set)


# In[102]:


import random as r
print()


# In[127]:


n=int(input("enter the number of candies in jar:"))
k1=int(input("enter the number of candies must be inside the jar:"))
m=int(input("enter the number  of candies sold:"))

if(m>0):
     print("number of candies sold :", m)
     print("number of candies available:",n-m)
     print("to refill the remaining candies  ",m)

else:
     print("invalid input")
    

    


# In[151]:


n=int(input("enter the number:"))
l=[]
for i in range(n):
      ele=int(input())
        l.append(ele)
print(l)
c=0
for i in range(n):
    if(l[i]!=l[n-1] and l[i+1]==l[n-1]):
        c=c+l[i]
        break;
        
print(c)
     
       
     
    
    


# In[133]:


l[0]


# In[154]:


size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif(arr[i]=='0' and flag ==1):
        count=0
        flag=0
    if(count>max):
        max=count
print(max)

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




