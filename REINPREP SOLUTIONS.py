#!/usr/bin/env python
# coding: utf-8

# In[8]:


str="HeLlo"
s=0
for i in str:
    s+=ord(i)
    
print(s)
    
    


# In[32]:


n=int(input())
str=input()
l=list(str)
c=int(input())
print(str[0:3:1])
print(str[2:5:1])
print(str[4:6:1])
        


# In[1]:


n=int(input())

str=input()
l=list(str)
c=int(input())
count=0
i=int(str[0])
j=int(str[1])
while(i<n):
    print(i,j)
    i=i+c
    j=j+c
    


# In[11]:


n=int(input())
if(n%2==0):
    str=input()
    l=list(str)
    c=int(input())
    i=1
    j=i+1
    while(i<n):
        print(i,j)
        i=i+c
        j=j+c
else:
    print("Invalid Input")

    


# In[64]:


n=int(input())
str=input()
l=list(str)
c=int(input())
print(l)

s=str(l)
for i in range(n):
    print(s[i:i+2:1])


# In[ ]:


""" 1.read n no of list elements
    2.store the n elements in list
    3.read chuncks 
    


"""


# In[4]:


n=int(input())
if(n%2==1):
    print("Invalid input")
else:
    str=input()
    l=list(str)
    c=int(input())
    j=int(l[1])
    for i in range(1,n+1,c):
        print(i,j)
        j=j+2


# In[46]:


#product functions
n=int(input())
if(n<=0):
    print("Invalid Input")
else:
    str1=input()
    l=str1.split(" ")
    il=[int(i) for i in l]
    r=1
    for i in il:
        r=r*i
    print(r)


# In[63]:


#SWAP FIRST AND LAST
""" 
    1,2,3
    3,2,1
"""
str1=input()
l=str1.split(" ")
il=[int(i) for i in l]

j=len(l)
temp=il[0]  
il[0]=il[j-1] 
il[j-1]=temp
for i in il:
    print(i,end=" ")


# In[76]:



str1=input()
l=str1.split(" ")
il=[int(i) for i in l]
print(il)
j=len(l)
temp=il[0]  
il[0]=il[j-1] 
il[j-1]=temp
print(il) 


# In[38]:



str1=input()
l=str1.split(" ")
il=[int(i) for i in l]
print(il)


# In[ ]:


def db(num):
    db(n//2)
    
print(num%2)
    
    
n=int(input())
db(n)


# In[3]:



def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num % 2, end = '')

if __name__ == '__main__':
    dec_val=int(input())
    DecimalToBinary(dec_val)


# In[4]:


p,q=7,5
j=1
c=0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%p==0 and i%q==0):
        c+=1

print(c)


# In[10]:


a,b=0,1

for i in range(0,9):
    if(i==1):
        print(1,end=" ")
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    


# In[ ]:


n=int(input())
if(n<=100 and n>=0):
    


# In[13]:


l=[]
len(l)


# In[16]:


def db(n):
    if(n>=0 and n<=100):
        if(n>=1):
            db(n//2)
            print(n%2,end='')
            
n=int(input())
db(n)
    


# In[21]:


def db1(n):
    return bin(n).replace("0b","")
            
n=int(input())
p=db1(n)
print(p)


# In[41]:


ul=[]
dl=[]
il=[]
str1=input()
l=str1.split(" ")
il=[int(i) for i in l]

for i in il:
    if i not in ul:
        ul.append(i)
    elif i not in dl:
        dl.append(i)
if(len(dl)>0):
    print("True")
else:
    print("False")


# In[43]:


l=input().split()
f=0
n=len(l)
for i in range(0,n):
    for j in range(i+1,n):
        if(l[i]==l[j]):
            f+=1
print(f>=1)


# In[ ]:


a=int(input())
b=a.split(" ")
c=set(b)
if(len(c)==len(b)):
    print(False)
else:
    print(True)


# In[5]:


str1=(input())

print(str1[::-1])


# In[7]:


n=int(input())
l=[]
for i in range(n):
    ele=int(input())
    l.append(ele)
print(min(l))
print(max(l))


# In[32]:


n=int(input())
str=input()
l=list(str.split(" "))   
l.sort()
print(l)
for i in range(n):
print(p)
k=int(input("enter the kth value"))
print(l[k-1]) 


# In[7]:


l=(input().split())
l=list(l)
n1=[int(i) for i in range(int(l[0])) ]
n1=set(n1)

n2=[input().split() for i in range(int(l[1])) ]
n2=set(n2)
u=n2.union(n1)
print(u)
    


# In[18]:


l=(input().split())
print(l)
for i in range(int(l[0])):
    nl=list(map(int,input().split()))

    
print(nl)


# In[ ]:





# In[6]:


help(set)

