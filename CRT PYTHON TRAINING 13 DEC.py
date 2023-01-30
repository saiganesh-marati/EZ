#!/usr/bin/env python
# coding: utf-8

# In[4]:


#loops
i=0
while(i<=10):
    print(i)
    i=i+1
i=0
while(i<=10):
    print(i,end=" ") #\t -->tab space
    i=i+1


# In[ ]:





# In[9]:


#wap to add the  elements in between range using while loop
#start=3
#end=9
#sum=42

start=int(input("enter the start index:"))
end=int(input("enter the end value:"))
sum1=0
while(start<=end):
    sum1=sum1+start
    start=start+1

print("sum:",sum1)


# In[23]:


#wap to find sum of digits in a number
#123==>1+2+3=6

n=int(input("enter the number to find sum of digits:"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
    

print(temp,"sum of digits:",sum)


# # nivens number/harshed number
# #test case
# #n=21
# s(n)=3(21--->2+1==3)
# t=21/3==0(remiander==0)
# that is nivens number

# In[24]:


#nivens number
n=int(input("enter the number to check nivens number"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10

if(temp%sum==0):
    print("nivens number")
else:
    print("not a nivens number")


# In[64]:


#input :123
#output:3 2 1

n =int(input("enter the number to find reverse:"))
s=0
while(n>0):
    r=n%10
    print(r,end=" ")
    #s=s*10+r
    n=n//10
    


    


# In[63]:




"""def reverse(n):
     if(len(n)==0):
            return n
        return reverse(n[1:]) +n[0]

    """
    
num=1234
n_string=str(num)
#rev=reverse(n_string)
#print(rev)
r_num="".join(reversed(n_string))
#
#
#
#
print(r_num)


# In[59]:



#recurrsion
def reverse(n):
    if(len(n))==0:
        return n
    return reverse(n[1:])+n[0]


num=1234
n_string=str(num)
r_string=reverse(n_string)
print(r_string)


# In[ ]:


#for loops


# In[69]:


n=int(input("enter the n value:"))
sum=0
for i in range(n+1):
    sum=sum+i
    

avg=sum/n
print("sum of numbers from ",1,"till ",n,":",sum)
print("average of ",n," numbers :",avg)
    


# In[76]:


#input =5
#5*1=5

n =int(input("enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# In[85]:


#print leap years from 1900 to 2101
#leapyear1  leapyear2



for i in range(1900,2102):
    if(i%4==0):
        print(i,end=" ")
    


# In[90]:


#wap for series
"""1+1/2+1/3+1/4.......+1/n
if n=5
 print sum(1+1/2+1/3+1/4+1/5)
    """

n=int(input("enter the n value:"))
s=0
for i in range(1,n+1):
    s=s+1/i
    
print(s)
     


# In[93]:


""" 1+(1/2*2)+1/(3*3)+.......+1/(n*n)"""

n=int(input("enter the n value:"))
s=0
for i in range(1,n+1):
    s=s+1/i**2
    
print(s)


# In[99]:


""" 1+(1/2*2)+1/(3*3)+.......+1/(n*n)"""

n=int(input("enter the n value:"))
s=0
for i in range(1,n+1):
    s=s+1/i**3

print(s)


# In[100]:


str="hi"
str.capitalize()


# In[103]:


# $$$$hi$$$$
str.center(10,'$')


# In[104]:


str="ll"
substr="hehellhehell"
print(substr.count(str,0,len(substr)))


# In[107]:


str="he is my cousin"
print(str.find("my",0,len(str)))


# In[113]:


#syntax for left justification and right justification
#ljust(width,[fillchar])
str="hello"
print(str.rjust(20,'$'))
str1="hi"
print(str.ljust(20,'^'))


# In[126]:


str1="126"
str="4"
print(str.zfill(14))
print(str1.zfill(4))#zfill(width)


# In[137]:


print(ord('z'))#char to ascii
print(chr(97))#ascii to char


# In[145]:



str="hi my name is MR.Z"
print(max(str))#max will show only highest ascii value
str1=str.title()# print(str.title())'Hi My Name Is Mr.Z'
print(str1.swapcase())#'hI mY nAME iS mR.z'
print(list(enumerate(str)))


# In[ ]:


#input: str="India has won "
#output: I n d i a h a s  w o n


# In[151]:


str="India has won"
for i in str:
    print(i,end=" ")


# In[156]:


#ceaser cipher
str="India"
index=0
while(index<len(str)):
    letter=str[index]
    print(chr(ord(letter)+2),end=" ")
    index=index+1
    


# In[166]:


#abecedarian series
str1="ate"
l=['A','b','c','d','e']
for i in l:
     print(i+str1,end="\n")
 #   print(str(l))


# In[162]:


print(ord('n'))


# In[170]:


str1=input()
l=[]
for i in range(len(str1)):
    ele=input()
    l.append(ele)

for i in l:
     print(i+str1,end="\n")


# In[173]:


str=input()
str1=input()
l=list(str1)


for i in l:
     print(i+str,end="\n")


# In[185]:


#SERIES
#0,0,7,6,14,12,....N
#POS:1,2,3,4,[1,3,5,7..]
n=int(input("enter the size of n "))
s7=0
s6=0

for i  in range(1,n+1):
        if(i%2!=0):
            s7=s7+7
        else:
            s6+s6+6
if(n%2!=0):
    print('{} at accordance {}'.format(n,s7-7))
else:
    print('{} at accordance {}'.format(n,s6-6))
    


# In[192]:


n= int(input())
l=[]
for i in range(0,n+1):
    a=7*i
    l.append(a)
    b=6*i
    l.append(b)
print(l)
lt=len(l)
num=int(input("enter position: "))
for i in range(i):
    if(i==num-i):
        print(l[num])


# In[ ]:


#find 13,16 terms
#1,1,2,3,4,9,8,27,16

n=int(input())
l=[]
for i in range(1,n+1):
    a=2*i
    l.append


# In[ ]:





# In[210]:



l=[]
for i in range(0,15):
    a=2**i
    l.append(a)
    b=3**i
    l.append(b)
print("series",l)
l1=[]
for i in range(0,30):
    i=i+1
    l1.append(i)
print("position:",l1)
    

num=int(input("enter position: "))
print(l[num-1])


# In[ ]:





# In[ ]:





# In[213]:


v=int(input("enter the position:"))
if(v%2==0):
    v//=2
    print(6*(v-1))
else:
    v=v//2+1
    print(7*(v-1))

    


# In[212]:


j,k=0,0
v=int(input("enter the position:"))
l=[]
for i in range(0,22):
    if(i%2==0):
        l.append(7*j)
        j+=1
    else:
        l.append(6*k)
        k+=1
print(l)
print(f"{v} at accordance {l[v-1]} ")


# In[214]:


n=int(input())
if(n%2==0):
    print(3**((n//2)-1))
else:
     print(2**((n//2)))


# In[ ]:



"""
#input n total no of days--------------------------------7
 the next line m denotes  no of obligations--------------2
 the next line contains k obligations can cancel---------0
 0<=i<=M CONSTRAINTS  -----------------------------------3 AND 4
 
 O/P====3
"""


# In[218]:


n =int(input("enter the number of days"))
m=int(input("enter the number of obligations:"))
k=int(input())
arr=[0]*n
for i in range(m):
    arr[i]=int(input())
ans=0
arr.sort()
if(k>0):
    for i in range(k-1,m-3,1):
        ans=max(ans,arr[i]-arr[i-k-1]-1)
else:
    j=0
    while arr[j]==0:
        j=j+1
    count=0
    for i in range(1,n-1,1):
        count+=n-1
        if(j<n and (i==arr[j])):
            count=0
            j+=n-1
        ans=max(count,ans)
print(ans)


# In[ ]:





# In[9]:


str="saiganesh"
str.split()


# In[ ]:





# In[1]:


class AgeError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg


# In[2]:


age=int(input())
try:
    if(age<18):
        raise AgeError("you are not able to vote")
except AgeError as msg:
    print(msg)

print("task finished")
    


# In[ ]:


#this is the method to create  a manual or user defined exception 
"""class ExceptionName(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
        """


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




