#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#functions space is allocated in the memory location
"""
function in 2 parts
1.function header
2.function body

syntax : def fun_name(var1,var2 ......):
            documentation of string
            statement block
            return expression/values
            
no arguments no return value:
eg:
    def fun():----------------callee
        for i in range(10):
            print("abcde")
    fun()---------------------caller



argumentspassed with return value:
eg:
    def add(x,y):
        return x+y
        
    a=10
    b=20
    operation=add-----------------------function name assigned to a variable
    print(operation(a,b))----------------function calling
    
    
    
































"""


# In[6]:


#global variable

var="h1"
def abc():
    global var2
    var2="good morning !!"
    print("in the function var1 is ",var)

abc()
print("out side the function var2",var2)
print("var1 is ",var)


# In[8]:


#modifying global variable

var1="h1"

def abc():
    global var1
    var1="good morning !!"
    print("in the function var1 is ",var1)

abc()
print("out side the function var2",var1)
var1="verygood"
print(" outside function after modifying var1 is ",var1)


# In[19]:


#to demonstrate access on variables inner and outer functions

#var1="hi"
def outer_fun():
    outer_var=11
    def inner_fun():
        inner_var=22
        print("inner variable",inner_var)
    inner_fun()
    print("outer variable",outer_var)

outer_fun()        
        


# In[23]:


#wa function and return its cubation formation

def cube(n):
    return n**3
n=int(input())
print("cube of {} is {} ".format(n,cube(n)))


# In[28]:


#factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
n=int(input())
print("factorial of {} is {}".format(n,fact(n)))


# In[37]:




def abc(x):
    print("hi,all"+"x",x)
    
abc("5")
abc(5)

#abc(5,15)   


# In[44]:


#wa function to understand a mismatch parameters 
def fun(i):
    print("orange",i)
    
    
j=10 
#fun()#------------this may lead to error i.e; no parameters
fun(10)
fun(j)
fun(5+2*4//4)


# In[55]:


#program demo on key arguments
def display(str ,x,f):
    print("name is ",str)
    print("age  of ",str,"  is ",x)
    print("salary of ",str," is ",f)
    
#display("hi",5,4.3)
#display(f=6.89,x=98,str="hack")
display("Sai",20,100000)
display(str="sony",x=23,f=50000.0)


# In[59]:


#lambda functions

""" gs:
       udv= lambda(args):(exp)
       
       
       lambda has no names
       it can take n number of attributes
       it can only return 1 value
       lambda cannot access global variables 
       cannot access  variables other than their parameters list
       one expression and one output
       cannot contain multi parameters 
       doesnot  have explicit return stmts
       
       
"""

add=lambda a,b:a+b
sub=lambda a,b,c:a-b-c
print("addition of {0} {1} is {2}".format(10,20,add(10,20)))
print()


# In[67]:


#function using in lambda
def small(a,b):
    if(a<b):return a 
    else: return b
    

print(small(2,4))
add = lambda x,y:x+y
diff =lambda x,y:x-y

print("Small of two no ",small(add(-3,-2),diff(-1,2)))


# In[80]:



#lambda function as a function argument
def inc(y):
    return (lambda x:x+1)(y)
a=100
print("A =",a)
print("after incrementing ",inc(a))


# In[83]:


def fun(f,n):
    print(f(n))
twice=lambda x:x*2 #
triple=lambda x:x*3
fun(twice,4)#f,n-->twice(4)---->lambda x=4*2===>x=8
fun(triple,9)#f,n-->triple(9)--->lambda x=9*3===>x=27


# In[86]:


add =lambda x,y:x+y
m_and_add=lambda x,y,z:x*add(y,z)
print(m_and_add(3,4,5))


# In[90]:


x=lambda : sum(range(1,11))
    
print(x())


# In[93]:


def swapn(x,y):
    x,y=y,x
    print("after swapping x is {} and y is {}".format(x,y))
x=int(input("enter x value :"))
y=int(input("enter y value :"))
print("before swapping x is {} and y is {}".format(x,y))
swapn(x,y)


# In[104]:


""" wap  to return the full name of a person where 1st variable passed is first name
2nd variable is passed as last name


""" 

def fn(x,y):
     return(x+" "+(y))
        
x=input("enter the first name:")
y=input("enter the last name:")
fn(x,y)


# In[107]:


#wap 

def even(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
        
n=int(input("N="))
even(n)


# In[110]:


#even or odd 
def even(n):
    if(n&1==0):
        return 1
    else:
        return -1
        
n=int(input("N="))
e=even(n)
if(e==1):
    print(" number is even")
else:
    print(" number is odd")


# In[118]:


#wap
""" 
 p=200
 r=3
 t=roi
 si=(p*r*roi)/100
"""

def SI(p,t,r):
    return ((p*t*r)/100)



age=int(input("enter the age:"))
if(age>60):
    print("he is senior citizen  has ROI 12%")
    print(SI(p=200,t=3,r=12))
else:
    print("he is normal customer has ROI 10%:")
    print(SI(p=200,t=3,r=10))
    


# In[116]:


#fact

def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n=int(input())
print(fact(n))


# In[117]:


def roi(a):
    return 12 if a>=60 else 10
a=int(input("Enter age:"))
p=200
r=3
e=roi(a)
p=(p*r*e)/100
print("SI:",p)


# In[123]:


#even odd
def even(n):
    return 1 if n&1==0 else -1
n=int(input())
b=even(n)
print("even number") if b==1 else print("odd number")


# In[127]:


#wap exp(x,y) using recursion

def exp(x,y):
    if y==0:
        return 1
    
    return x*exp(x,y-1)
    

        


# In[129]:


def exp(x,y):
    return 1 if y==0 else  x*exp(x,y-1)
x=int(input())
y=int(input())
exp(x,y)


# In[ ]:


0 1 1 2 3 5  8


# In[2]:


#fibonacci
def fibba(n):
    if(n<2):
        return 1
    return (fibba(n-1)+fibba(n-2))

n=int(input())
for i in range(0,n):
    print("fibonacci (",i,")",fibba(i))
    


# In[51]:


##3 poles 
##4 discs

def toh(A,B,C):
    for i in A:
        if((len(B)==0)):
            B.append(i)
            C.append(i+1)
            A[0]= 0
            A[1]=0
    for i in B:
        if(len(C)!=0):
            if(C[0]>B[0]):
                temp=C[0]
                B[0]=0
                C[0]=1
                C.append(temp)
    for i in range(0,len(A),2):
        if(len(B)!=0):
            if(A[2]>B[0]):
                temp=A[2]
                print(temp)
                B.clear()
                B.append(temp)
                A[2]=0
    
            
        
                
                
    
    

n=3
d=4
A=[1,2,3,4]
B=[]
C=[]
toh(A,B,C)
print(A)
print(B)
print(C)


# In[48]:


B=[1,2,3]
B.clear()
print(B)


# In[52]:


def hanoi (n,A,B,C):
    if(n>0):
        hanoi(n-1,A,C,B)
        if A:
            C.append(A.pop())
        hanoi(n-1,B,A,C)
        

A=[1,2,3,4]
B=[]
C=[]
hanoi(len(A),A,B,C)
print(A,B,C)


# In[69]:


#check if two strings 
def solve(a,b):
    n,m=len(a),len(b)
    if(n==0 and m==0):
        return True
    if(n>1 and a[0]=='*' and m==0):
        return False
    if(n>1 and a[0]=='?' ) or(n!=0 and m!=0 and a[0]==b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0]=='*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False

x=str(input("enter the string with char:"))
y=str(input("enter the string for match:"))
print("with wild characters :",x)
print("without wild characters ::",y)
print(solve(x,y))
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


"""  i/p
        6
        2 7 1 4 9 5
        
        if(i)
        



"""


# In[ ]:


from array import *
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

    
arr1=array(i,l)

for i in l:
    if(i%2==0):
        print(i,end=" ")
for i in l:
    if(i%2!=0):
        print(i,end=" ")
    
        
    


# In[85]:


from array import *
l=[1,2,3,4]
arr1=array('i',l)
for x in arr1:
    print(x,end=" ")
    
    


# In[105]:


n=int(input())
if(n<=0):
    print("Invalid Input")
    exit
x=input().split()
if(n!=len(x)):
    exit
x=[ int(i) for i in x]
o=[]
e=[]
for i in x:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
e.sort()
o.sort()
l1=e+o

for i in l1:
    print(i,end=" ")


# In[96]:





# In[ ]:





# In[112]:


n=int(input())
if(n>0):
    str1=
str1=input()
l=str1.split(" ")
il=[]
ol=[]
el=[]
fl=[]
for i in range(0,n):
    il.append(int(l[i]))
il.sort()
for i in range(0,n):
    if(il[i]%2==0):
        el.append(il[i])
    else:
        ol.append(il[i])
fl=el+ol
for i in range(n):
    print(fl[i],end=" ")

