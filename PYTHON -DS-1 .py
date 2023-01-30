#!/usr/bin/env python
# coding: utf-8

# In[11]:


n=int(input())
arr=input()
l=list(arr)

c=0
max=0
for i in range(n):
    if(l[i]!=l[n-1] and l[i+1]==l[n-1]):
        c=c+1
        break
print(c)


# In[13]:


n=int(input())
max=0
c=0
f=0
str=input()
arr=list(str)
for i in range(0,n):
    if(arr[i]=='1'):
        c=c+1
        f=1
    elif(arr[i]=='0' and f==1):
        c=0
        f=0
    if(c>max):
        max=c
print(max)


# In[13]:



#v=200
#w=540

#2<=w
#w%2=0
#v<w

v=int(input("enter total number of vehicles:"))
w=int(input("enter the total number of wheels:"))
for i in range(v+1):
    if((v-i)*2 +(i*4)==w):
        print("two wheeler ",v-i,"four wheeler",i)





# In[11]:



v=int(input("enter total number of vehicles:"))
w=int(input("enter the total number of wheels:"))

if(w&1==1 or w<2 or w<=v):
    print("Invalid Input")
else:
    x=((4*v)-w)//2
    
    
print("tw",x)
print("four w",v-x)


# #binary tree

# In[28]:


class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
        
def insert(root,newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
        
def inorder(root):
    if root== None:
        return 
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
        
    

    
     
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)

inorder(root)


# In[32]:


class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
        
def insert(root,newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
        
def inorder(root):
    if root == None:
        return 
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
        
    
       
def preorder(root):
    if root == None:
        return 
  
    print(root.data)
    preorder(root.lc)
    preorder(root.rc)
    
def postorder(root):
    if root ==None:
        return 
    postorder(root.lc)
    postorder(root.rc)
    print(root.data)
 




    
     
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print(" inorder ")
inorder(root)
print(" preorder ")

preorder(root)
print("Post order")
postorder(root)


# In[35]:



#meta inheritance
class Node:
    def __init__(self,key,l=None,r=None):
        self.key=key
        self.l=l
        self.r=r
        
def vot(node,dist,d):
    if node is None:
        return 
    d.setdefault(dist,[]).append(node.key)
    vot(node.l,dist-1,d)
    vot(node.r,dist+1,d)
    
    
    
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)







if __name__=="__main__":
    root=Node(1)
    root.l=Node(2)
    root.r=Node(3)
    root.r.l=Node(4)
    root.r.r=Node(5)

    root.r.l.l=Node(6)
    root.r.l.r=Node(7)

    root.r.l.r.l=Node(8)
    root.r.l.r.r=Node(9)

    pvot(root)


# In[ ]:


#i/o -n 10
#o/p- 181


# In[16]:


def sod(n):
    s=0
    while(n>0 and n!=100):
        r=n%10
        s+=r
        n=n//10
    
    if(n>=100 and n<999):
        return n//10
    elif(n>=1000 and n<9999):
        fs=n//10
        ss=n%1000
        ms=(n/10)-100
        return ms+ss+fs
    return s
    
        
        

n=int(input())
l=[]
sl=[]
for i in range(1,n+1):
    sl.append(i**2)
    t=sod(i**2)
    l.append(t)

    
print(sl)
print(l)


# In[ ]:


if n>=100 and n<999:
    return n//10

if n>=1000 and n<9999:
    t=n


# In[ ]:


#i/p:8
#10 98 3 33 12 22 21 11
##o/p:


# In[1]:


n=int(input())
l=[]
l=[int(i) for i in l]
print(l)


# In[ ]:





# In[ ]:





# In[9]:


n=int(input())
if(n<=0):
    print("Invalid input")
    quit()
l=input().split()
l=[int(i) for i in l]
ol=[]
el=[]
for i in range(0,n):
    if(l[i]&1==1):
        ol.append(l[i])
    else:
        el.append(l[i])
l=el+ol
for i in l:
    print(i,end=" ")
    
    
    
    
    
#i/p:8
#10 98 3 33 12 22 21 11


# In[21]:


d={}
k=['NAME','AGE','BRANCH']
v=['ABC','100','CSE']
d={
    k[i]:v[i] for i in range(0,len(k))
}
print(d)
#print(d[])
outsource=zip(k,v)
abc=dict(outsource)
print(abc)


# In[22]:


k=input().split()
v=input().split()
os=dict(zip(k,v))
print(os)


# In[ ]:


#write a program to store a sparse matrix
#into dictionary


# In[26]:


#l=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
fr=[int(i) for i in input().split()]
sr=[int(i) for i in input().split()]
tr=[int(i) for i in input().split()]
l=[fr,sr,tr]
print(l)

d={
    i+1 :l[i] for i in range(0,len(l))
}
print(d)


# In[27]:


a=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
d={}

for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j]!=0):
            d[i,j]=a[i][j]
                   
print(d)


# In[30]:


a=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
d={}
for i in range(len(a)):
    print("\n")
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
        if a[i][j]!=0:
            d[i,j]=a[i][j]
            
print(d)
        


# In[38]:


str="123456"
l=list(str)
for i in l:
    print(i,end=" ")


# In[ ]:


#write a non repeated character in string
#ex:I/P:'INFINITY' O/P: 


# In[52]:


str=input().lower()
for i in range(len(str)):
    if(str.count(str[i])==1):
        print((str[i].upper()).lower(),end=" ")


# In[50]:


n=input()
c=0
mi=999
m=''
ch=''
for i in range(len(n)):
    m=n[i]
    c=0
    for j in range(len(n)):
        if m==n[j]:
            c+=1
    if c<mi:
        mi=c
        ch=m
print(ch)


# In[55]:


str=input().lower()
for i in str:
    c=0
    for j in str:
        if i==j:
            c+=1
        if c>1:
            break
    if c==1:
        print((i.upper()).lower(),end=" ")


# In[57]:


class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class Slist:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        pv=self.headval
        while pv is not None:
            print(pv.val)
            pv=pv.next
            
        
l=Slist()
l.headval=Node(1)
e2=Node(3)
e3=Node(5)
l.headval.next=e2
e2.next=e3

l.listprint()    

        


# In[59]:


class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class Slist:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        pv=self.headval
        while pv is not None:
            print(pv.val)
            pv=pv.next
    def push(self,nn):
        nn=Node(nn)
        nn.next=self.headval
        self.head=nn
    def insertnext(self,prenode,nn):
        if prenode is None:
            print("the previous node")
            return 
        nn=Node(nn)
        nn.next=prenode.next
        prenode.next=nn
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=nn
            return 
        last =self.head
        while(last.next):
            last=last.next
            last.next=nn
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
        
        
            
if __name__ =='__main__' :      
    l=Slist()
    l.headval=Node(1)
    e2=Node(3)
    e3=Node(5)
    e4=Node(8)
    l.headval.next=e2
    e2.next=e3
    e3.next=e4

    l.listprint()    

        


# In[3]:


import heapq as h

l=[4,6,1,-2,46,8,99,-13,61,22,100]
h.heapify(l)
print(l)


# In[ ]:


class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
        
def insert(root,newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
        
def inorder(root):
    if root== None:
        return 
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
        
    

    
     
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)

inorder(root)


# In[ ]:


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


# In[11]:


class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
        
def insert(root,newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
        
def inorder(root):
    if root== None:
        return 
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
        
    

    
     
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)

inorder(root)


# In[49]:


class bst:
    def __init__(self,val):
        self.val=val
        self.lc=None
        self.rc=None
def insert(root,val):
    if root is None:
        root=bst(val)
        return root
    if val<root.val:
        root.lc=insert(root.lc,val)
    else:
        root.rc=insert(root.rc,val)
    return root
            
def inorder(root):
    if root==None:
        return 
    inorder(root.lc)
    print(root.val)
    inorder(root.rc)
def 
        

        
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)

inorder(root)


# In[55]:


class Node:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)




r=Node(50)
r=insert(r, 30)
r=insert(r, 20)
r=insert(r, 40)
r=insert(r, 70)
insert(r, 60)
insert(r, 80)
inorder(r)


# In[57]:


class bst:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
        
def insert(root,val):
    if root is None:
        root=bst(val)
        return root
    if val<root.val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root
def preorder(root):
    if(root is None):
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val)
        

root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)

inorder(root)
print("preorder")


# In[59]:


s1=input()
s2=input()
if(sorted(s1)==sorted)


# In[60]:


s="abc"
c=set(s)
print(c)


# In[7]:


x=int(input("enter x value:"))
y=int(input("enter y value:"))
z=int(input("enter z value:"))
if(x>y and x>z):
    print("x is greatest",x)
elif(y>x and y>z):
    print("y is greatest",y)
else:
    print("z is greatest",z)


# In[ ]:


#wp to print 
1
12
123
1234


# In[21]:


x=int(input("enter the number of rows:"))
for i in range(1,x+1):
    for j in range(i):
        print(j+1,end="")
    print()


# In[24]:


x=int(input("enter the number of rows:"))
for i in range(x):
    for j in range(i):
        print("*",end=" ")
    print()


# In[28]:


#factorial
a=int(input())
x=1
for i in range(1,a+1):
    x=x*i
print(x)
    


# In[11]:


#factorial 
def fact(n):
    if(n==0):
        return 1
    return fact(n-1)*n

n=int(input("enter the number to find factorial:"))
p=fact(n)
print("factorial of ",n,"is ",p)


# In[40]:


#fibonacci series

n=int(input())
f=0
s=1
ct=2

while(ct<n):
    c=f+s
    f=s
    s=c
    print(c)
    ct+=1
        

    


# In[57]:


f,s=0,1
n=int(input())
ct=2
print(f,s,end=" ")
while(ct<n):
    c=f+s
    f=s
    s=c
    print(c,end=" ")
    ct+=1


# In[69]:


#prime or not
a=int(input("enter the number to check prime:"))
c=0
for i in range(1,a+1):
    if(a%i==0):
        c+=1

if(c==2):
    print("prime")
else:
    print("not a prime number")


# In[94]:


l=()
(type(l))


# In[77]:


#5 avg elements of list
n=int(input("enter the size of list:"))
l=[]
for i in range(n):
    ele=int(input())
    l.append(ele)
    
print(sum(l)/n)


# In[85]:


# remove empty tuples from list
l=[(1,2,3),(),(4,5,6)]
b=[]
for i in l:
    t=0
    for j in i:
        t+=1
    if(t!=0):
        b.append(i)
        
print(b)


# In[92]:


sample_list=['Red','Green','White','Black','Pink','Yellow']

sample_list.remove(sample_list[5])
sample_list.remove(sample_list[4])
sample_list.remove(sample_list[0])
print(sample_list)


# In[ ]:





# In[96]:


n=int(input("enter the list size:"))
l=[]
for i in range(n):
    ele=input()
    l.append(ele)

l.remove(l[5])
l.remove(l[4])
l.remove(l[0])

print(l)


# In[100]:


#8
n=int(input("enter the size of tuple: "))
l=[]
for i in range(n):
    ele=int(input())
    l.append(ele)
    
t=tuple(l)
print("sum of all numbers in tuple",sum(t))
mul=1
for i in range(n):
    mul=mul*t[i]
    
print("product of all numbers",mul)


# In[121]:



n=int(input("enter the size of list: "))
l=[]
for i in range(n):
    ele=eval(input())
    l.append(ele)
    
for i in range(len(l)):
    for j in range(i+1,len(l)):
        
        print(l[i],l[j])
        print(l[j],l[i])


# In[134]:


#7 permutations list
from itertools import permutations

n=int(input("enter the size of list: "))
l=[]
for i in range(n):
    ele=eval(input())
    l.append(ele)

p=permutations(l)
for i in p:
    for j in i:
        print(j,end=" ")
    print()


# In[136]:


s1=input("enter the string:")
l=list(s1)
c=0
j=0
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if(l[i]==l[j]):
            
            


# In[1]:


s1=input("enter the string:")
l=list(s1)
ll=[]
t=0
c=0
for i in s1:
    for j in ll:
        if j==i:
            c+=1
    if s1.count(i)>1 and c==0:
        t+=1
        ll.append(i)
print(t)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




