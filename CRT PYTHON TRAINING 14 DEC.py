#!/usr/bin/env python
# coding: utf-8

# In[2]:


#abecedarian series
str1=input()
l=[]
for i in range(len(str1)):
    ele=input()
    l.append(ele)
for i in l:
    print(i+str1,end="\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


#abecedarian series
str1="ABCDEFGH"
str2="ate"
for letter in str1:
    print(letter+str2,end=" ")


# In[ ]:


#patterns
"""
1.basic patterns
2.mirror image patterns
3.symmetrical patterns
4.choice of patterns  |_
                        |_
                          |_
                          
5.anti patterns/hallow patterns
        *0000                 ****
        **000                 *  *
        ***00                 *  *
        ****0                 ****
        *****
"""


# In[16]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
            


# In[18]:


n=int(input())
for i in range(n):
    for j in range(n):
        if(i<=j):
            print("*",end=" ")
    print("\n")


# In[20]:


n=int(input())
for i in range(n):
    for j in range(n):
        if(i>=j):
            print("*",end=" ")
    print("\n")


# In[25]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")
            


# In[34]:


#inverted of rightangle triangle
n=int(input())#rows
for i in range(n,0,-1):#rows -1
    for j in range(0,i):
        print(j+1,end=" ")
    print("\n")


# In[35]:


n=int(input())#rows
for i in range(n,0,-1):#rows -1
    for j in range(0,i):
        print(i,end=" ")
    print("\n")


# In[36]:


n=int(input())#rows
for i in range(n,0,-1):#rows -1
    for j in range(0,i):
        print("*",end=" ")
    print("\n")


# In[40]:


n=int(input())#rows
for i in range(n):#rows -1
    for j in range(0,i):
        print("*",end=" ")
    print("\n")


# In[ ]:





# In[42]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")


# In[66]:


n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")


# In[58]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[60]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[ ]:





# In[67]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")


# In[68]:


n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[69]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[ ]:





# In[ ]:





# In[73]:


n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(j<i):
            print(' ',end='')
        else:
            print('@',end='')
        j=j+1
    i=i+1
    print()


# In[79]:


n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(j<i):
            print(' ',end='')
        else:
            print('@',end='')
        j=j+1
    i=i+1
    print()


# In[ ]:





# In[83]:


n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[96]:


n=int(input())
for i in range(n,0,-1):
    for j in range(n+1):
      
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")

for i in range(n+1):
    for j in range(n+1):
        if(j<i):
            print(' ',end=' ')
        else:
            print("*",end=" ")
    print("\n")


# In[ ]:





# In[99]:


n=int(input())
for i in range(n,0,-1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*", end="   ")
            
    print("\n")
for i in range(n+1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*", end="   ")
            
    print("\n")


# In[109]:


n=int(input())
for i in range(n):
    for j in range(n):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end="   ")
    print("\n")


# In[129]:


n=int(input())
for i in range(n,0,-1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end="   ")
    print()
for i in range(n+1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end="   ")
    print()


# In[143]:


#rhombus or diamond pattern
n=int(input())
i=1
while i<=n:
    j=n
    while (j>=i):
            print(' ',end=" ")
            j-=1
    print('*',end=" ")
    k=1
    while(k<2*(i-1)):
        print(' ',end=' ')
        k=k+1
        
    if i==1:
        print()
    else:
        print("*")
    i+=1
i=n-1
while i>=1:
    j=n
    while j>=i:
        print(' ',end=' ')
        j-=1
    print("*",end=" ")
    k=1
    while k<2*(i-1):
            print(' ',end=' ')
            k+=1
    if i==1:
        print()
    else:
        print("*")
    i-=1

            
        


# In[209]:


#rhombus or diamond pattern
n=int(input())
i=1
while i<=n:
    j=n
    while (j>=i):
            print(' ',end=" ")
            j-=1
    print('*',end=" ")
    k=1
    while(k<2*(i-1)):
        print(' ',end=' ')
        k=k+1
        
    if i==1:
        print()
    else:
        print("*")
    i+=1
i=n-1
while i>=1:
    j=n
    while j>=i:
        print(' ',end=' ')
        j-=1
    print("*",end=" ")
    k=1
    while k<2*(i-1):
            print(' ',end=' ')
            k+=1
    if i==1:
        print()
    else:
        print("*")
    i-=1

            
        


# In[187]:


#I/Pstr="INDIA"
#O/P:
#I
#I N
#I N D
#I N D I
#I N D I A

str="India"
str1="   "
for i in range(len(str)+1):
    for j in range(i):
        print(str[j],end=" ")
    print()


# In[195]:


str="SAIGANESH"
for i in range(len(str)):
    for j in range(i):
        print(str[j],end=" ")
    print("\n")


# In[199]:


str="SAIGANESH"
for i in range(len(str)):
    for j in range(i):
        print(str[i-j],end=" ")
    print("\n")


# In[211]:


str="INDIA"
l=list(str)
for i in range(len(l)):
    for j in range(i+1):
        print(l[j],end=" ")
    print()
    
    


# In[213]:


word="INDIA"
x=""
for i in word:
    x+=i
    print(x)


# In[223]:


n=int(input())
x=A
for i in range(n):
    for j in range(i+1):
        print(x,end=" ")


# In[226]:


x=ord('A')
print(x)


# In[232]:


i,x=65,1
while(i<91):
    for j in range(x):
        if(i<91):
            print(chr(i),end=" ")
            i=i+1
    x=x+1
    print("\n")


# In[237]:


x=1
i=ord('A')
while(i<91):
    for j in range(x):
        if(i<91):
            print(chr(i),end=" ")
            i=i+1
    x=x+1
    print("\n")


# In[244]:


d={}
i=ord('A')
while(i<91):
    for j in range(1,27):
        d[j]=chr(i)
        i=i+1
print(d)


# In[239]:


d={}
type(d)


# In[247]:


n=int(input())
for i in range(n,0,-1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*", end="   ")    
    print("\n")


# In[250]:


n=int(input())
for i in range(n,0,-1):
    for j in range(n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("*",end="  ")
    print("\n")


# In[256]:


a=65
r=7
for i in range (0,r):
    for j in range(0,i+1):
        if(j<i):
            ch=chr(a)
            print(ch,end=' ')
            a+=1
    
    print("\n")


# In[267]:


a=65
r=5
m=(2*a)-2
for i in range (0,r):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")


# In[ ]:





# In[257]:


i,x=65,1
while(i<91):
    for j in range(x):
        if(i<91):
            print(chr(i),end=" ")
            i=i+1
    x=x+1
    print("\n")


# In[269]:


a=65
r=5
m=(2*r)-2
for i in range(0,r):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")


# In[ ]:


"""wap pattern 10 lines evaluating vertically right angle triangle
1
'2 5'
3 6 8 
4 7 9 10 
""" 


# In[281]:


for i in range(0,10):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
    


# In[304]:


def diff(a,b):
    return a-b

a,b=20,10
operation=diff
print(operation(a,b))


# In[324]:


n=int(input())
for x in range(1,n+1):
    k=x
    for y in range(1,x+1):
        print(k," ",end=" ")
        k+=(n-y)
    print()


# In[309]:


def name():
    for i in range(10):
        print("Sai")


name()


# In[312]:


def diff(a,b):
    c=a-b
    print(c)

a,b=20,10
diff(a,b)


# In[ ]:


#print prime numbers from range(a,b) use 1 while and for loop 
""" 
 2
 15
 2 3 5 7 11 13
"""
a=int(input("enter the  start index:"))
b=int(input("enter the  end index:"))
c=0
while(a<b):
    for i in range(1,b+1):
        if(a%i==0):
            c=c+1
        
    if(c==2):
        print(a,end=" ")
a=a+1


# In[367]:


i=int(input())
j=int(input())

c=0
while(i<j):
    for x in range(2,a//2+1):
        if(x<i):
            if(i%x==0):
                c=c+1

    if(c==2):
        print(i)
    j=j+1


# In[359]:


a=int(input())
b=int(input())
if(a<=0 or b<=0 or a>b):
    print("provide valid input")
else:
    while(a<=b):
        if(a==2):
            print(a,end=" ")
        elif(a==1):
            continue
        else:
            flag=0
            for i in range(2,a//2+1):
                if(a%i==0):
                    flag=1
                    break
            if(flag==0):
                print(a,end=" ")
        a+=1

            
            


# In[379]:





# In[405]:


n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(i==(n//2+1) or j==(n//2+1)):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[376]:


n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(i==(n//2+1) or j==(n//2+1)):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[390]:


n=int(input())
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(i==j or (j==n-i+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# In[410]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j or i==1 or i==n or j==1 or j==n or j==n-i+1 ):
            print("*",end=" ")z
        else:
            print(" ",end=" ")
    print()


# In[2]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if( i==1 or i==n or j==1 or j==n ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# In[411]:


n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(j==n-i+1):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        elif(i==1 or i==n ):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[414]:


n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1 ):
        if(j==n-i+1 ):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        elif(i==1 or i==n ):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[417]:


n=int(input("enter the size:"))
val=0
st=int(n/2+1)
if(n%2!=0):
    for i in range(1,int(n/2+2)):
        for j in range(1,val+1):
            
            
            
            
            
            
            
          print()
        val+=1
        st-=1
    val-=2
    st+=2
    for i in  range(int(n/2+2),n+1):
        for j in range(1,val+1):
            print(' ',end=" ")
        for k in range(1,str1):
            print("*",end='')
        print()
        val-=1
        st+=1
else:
    print("provides accurate input")


# In[ ]:





# In[421]:


n=int(input("Enter the size"))
val=0
st=int(n/2+1)
if n%2!=0:
    for i in range(1,int(n/2+2)):
        for j in range(1,val+1):
            print(" ",end="")
        for k in range(1,st+1):
            print("*",end=" ")
        print()
        val+=1
        st-=1
    val-=2
    st+=2
    for i in range(int(n/2+2),n+1):
        for j in range(1,val+1):
            print(" ",end="")
        for k in range(1,st+1):
            print("*",end=" ")
        print()
        val-=1
        st+=1
else:
    print("provide accurate input")


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


str="si"
l=[1,2,34]
sorted(str)


# In[416]:


n=int(input("N="))
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(j==n-i+1):
            print("*",end=" ")
        elif(i==j):
            print("*",end=" ")
        elif(i==1 or i==n):
            print("*",end=" ")
        elif(i<j and j<n-i+1):
            print("*",end=" ")
        elif(i>j and j>n-i+1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[ ]:





# In[ ]:


"""Input: a string of comma separated numbers. The numbers 5 and 8 are present in the listAssume that 8 always comes after 5.

Case 1: num1 = add all numbers which do not lie between 5 and 8 in the input.
Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
Output: sum of num1 and num2

Example: 1) 3,2,6,5,1,4,8,9
Num1 : 3+2+6+9 =20
Num2: 5148
output: 5248+20 = 5168

Answer: 13
     """


# In[9]:


arr=list(map(int,input().split(",")))
s1=s2=0
for i in range(len(arr)):
    if( i<8 and i<5 and i!=5 and i!=8 ):
        s1+=i
    else:
        s2+=i
print(s1)
print(s2)
    
    
    


# In[3]:


n=int(input("N="))
n=n//2
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(j<=n-i+1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
            

    
    for j in range(n+1,2*(n)):
        if(n+i<=j+1):
             print("*",end=" ")
        else:
            print( " ",end=" ")
    print()
for i in range(1,(n)):
    for j in range(1,n+1):
        if(j-1<=i):
            print("*",end=" ")
        else:
            print(" ", end=" ")
            

    
    for j in range(n+1,2*(n)):
        if(j>=2*n-i-1):
             print("*",end=" ")
        else:
            print( " ",end=" ")
    print()


# In[6]:


l=[2,7,1,4,9,5]
l.sort()
print(l)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




