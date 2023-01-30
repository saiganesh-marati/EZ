#!/usr/bin/env python
# coding: utf-8

# #oops
# #class
# #object
# 

# In[3]:


#program to access a class var using class object

class abc:
    var=22
    
obj=abc()
print(obj.var)


# In[11]:


#program to access a class member using class object

class abc:
    var=22
    def  show(self,var):
        print("this is show method")
        self.var=var
        print(var)
    
obj=abc()
print(obj.var)
obj.show(31)


# In[12]:


#program  on constructor and function

class abc:
    var=22
    def __init__(self):
        print("this is constructor ")
    def  show(self,var):
        print("this is show method")
        self.var=var
        print(var)
    
obj=abc()
print(obj.var)
obj.show(31)


# In[14]:


class abc:
    def __init__(self,val,val2):#___init__------>constructor is a special method to initilase the object while creating object
        print("in class method")
        self.val,val2=val,val2#self is a face of constructor in java it is like this.val=val self is default in constructor
        print("the val is {} and val2  is {}".format(val,val2))

obj=abc(10,20)

        


# In[18]:


#differnce between class variable and object variable

class abc:
    class_var=0 #class var
    def __init__(self,var):
        
        abc.class_var+=1#this is accessing  class variable with class
        self.var=var#object variable pass the value from main to class
        print("this is a object variable",var)
        print("this is class variable ",abc.class_var)
#main        
obj=abc(10)
obj1=abc(20)
obj3=abc(30)


# In[52]:


class even:
    even=0
    def check(self,num):
        if(num&1==0):
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if(self.even==1):
            print("even",num)
        else:
            print("odd",num)

obj=even()
obj.even_odd(3)


# In[3]:


class prime:
    c=0
    def check1(self,num):
        i=2
        while(i*i<=num):
            if(num%i==0):
                self.c+=2
            i=i+1
    def isprime(self,num):
        self.check1(num)
        if(self.c==2):
            print(" not prime")
        else:
            print(" prime")
n=int(input())         
obj=prime()
obj.isprime(n)


# In[56]:


class Number:
    even=0
    el=[]
    ol=[]
    def __init__(self,num):
        self.num=num
        if(num&1==0):
        
            self.el.append(num)
        else:
            self.ol.append(num)

        
obj=Number(45)

obj1=Number(1)
obj12=Number(12)
obj2=Number(3)
obj3=Number(14)
print(obj.el)
print(obj.ol)


# In[55]:


class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if(num&1==0):
            Number.even.append(num)
        else:
            Number.odd.append(num)

            

obj1=Number(1)
obj12=Number(12)
obj2=Number(3)
obj3=Number(14)
print(Number.odd)
print(Number.even)


# In[85]:


class number:
    even=0
    global e
    global o
    e=[]
    o=[]
    
    def even_odd(self,num):
        if num%2==0:
            e.append(num)
        else:
            o.append(num)
    def show(self):
        print("even :",e)
        print("odd :",o)

ob=number()

l=input("Enter a list of numbers").split()
l=[int(i) for i in l]
i=0
for i in l:
    ob.even_odd(i)
ob.show()


# In[27]:




global i
def checkprime(num):
    c=2
    i=1
    while(i*i<=num):
        if(num%i==0):
            c+=2
        i+=1
        if(c==2):
            printprime(num)
        else:
            printnotprime(num)
def cprange(num1,num2):
    for i in range(num1,num2):
        checkprime(i)
def printprime(num):
    print("this is not prime number",num)
def printnotprime(num):
    print("this is  prime",num)
   
    
a=int(input())
b=int(input())
j=a
while(j<=b):
    checkprime(j)
    j=j+1

   


# In[ ]:





# In[ ]:



   c=0
   i=1
   def checkprime(self,num):
       while(i*i<=num):
           if(num%i==0):
               c+=1
       i+=1
       if(c==2):
           printprime(num)
       else:
           printnotprime(num)
   def cprange(self,num1,num2):
       for i in range(num1,num2):
           checkprime(i)
       
   def printprime(self,num):
       print("this is prime number",num)
   def printnotprime(self,num):
       print("this is not prime",num)
  
   
   

if __name__=="__main__":
   n=Numbers()
   n.cprange(1,10


# In[87]:


class Number:
    p=[]
    np=[]
    c=0
    def __init__(self,num):
        self.num=num
        i=1
        while(i*i<=num):
            if(num%i==0):
                self.c+=1
            i=i+1
        if(self.c==1):
            print("prime")
            self.c=0
            Number.p.append(num)
        else:
            print("not prime")
            Number.np.append(num)
                
        
                

obj1=Number(13)
obj12=Number(12)
obj2=Number(3)
obj3=Number(14)
print("prime list",Number.p)
print("not prime",Number.np)


# In[84]:


class prime:
    c=0
    def check1(self,num):
        i=1
        while(i*i<=num):
            if(num%i==0):
                self.c+=1
            i=i+1
    def isprime(self,num):
        self.check1(num)
        if(self.c==1):
            print("  prime")
            self.c=0
        else:
            print(" not prime")
            
obj=prime()
obj.isprime(13)
obj.isprime(11)

obj.isprime(24)
obj.isprime(12)


# In[98]:


#del method
#general syntax   __del__
class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the object value is ",var)
        print("the class value is ",abc.class_var)
        
    def __del__(self):
        abc.class_var-=1
        print("the object with value %d  is going out of scope ",self.var)
        print("the class value is ",abc.class_var)
        
obj=abc(10)
obj1=abc(11)
obj2=abc(12)
del obj
del obj2
del obj1
    


# __repr__---------->syntax report of the object
# __cmp__------------>compares two class object
# __len__------------->builtin method which calculates length of object
# __call__----------->it acts like a func to call its instances
# __lt__,__le__,__eq__,__ne__,__gt__,__ge__,__cmp__--------->cmp 2 objects
# __iter__--->iteration over a object
# __getitem__ used for indexing
# gs:def __getitem__(self,val/var/key):
# __setitem__  assign an item to the indexed value
# 
#         
#     

# In[108]:


#program to demo on set items and get items 

class Numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
    
numlist=Numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])


# In[115]:


#program to demo on set items and get items 

class ABC():
    def __init__(self,name,var):
        self.name=name  
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return  self.var - obj.var
obj=ABC("abcdef",10)
print("the value stored in obj is ",repr(obj))
print("length of name stored in obj",len(obj))
obj1=ABC("ghijkl",1)
val=obj.__cmp__(obj1)
if(val==0):
    print("both values are equal")
elif(val==1):
    print("1st value is less than  second")
else:
    print("2nd value is lessthan 1st")


# In[126]:


#is for illustrating  for a private method
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this is from class method =", self.__var)

obj=abc(10)
obj._abc__display()

    
    


# In[132]:


#wap to call a class method from another method of same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def add_2(self):
        self.var+=2
        self.display()
        
obj=abc(10)
obj.add_2()


# In[138]:


#program to show how  class method calls a function 
#which is define in the global name space

def scale_10(x):
    return x*10

class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is=",self.var)
    def modify(self):
        self.var=scale_10(self.var)
        
obj=abc(10)
obj.display()
obj.modify()
obj.display()
    


# #built in attributes
# 
# #for get set and delete
# 1..hasattr(obj,name)-checks obj possesses the all atributes(true or false)  values or not
# 2.getattr(obj,name[,default])
# 3.setattr(obj,name,value)
# which is used to set an attribute of the obj
# 4.delattr(obj,name)----permanant deletion 

# In[149]:


class abc:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is ",self.var)
obj=abc(10)
obj.display()
print("check whether obj has attribute var ?")
getattr(obj,'var')
setattr(obj,'var',50)
print("after the setting value var is ",obj.var)
print(hasattr(obj,'var'))
setattr(obj,'vari',10)
print("after the setting new value var is ",obj.vari)
delattr(obj,'var')
print("after deletion the attr ,var is:",obj.var)



# In[151]:


class abc:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is ",self.var)
obj=abc(10)
obj.display()
print("check whether obj has attribute var ?")
getattr(obj,'var')
setattr(obj,'var',50)
print("after the setting value var is ",obj.var)
print(hasattr(obj,'var'))
setattr(obj,'var',10)
print("after the setting new value vari is ",obj.var)
delattr(obj,'var')
setattr(obj,'var',40)
print("after deletion the attr var and setting new var is:",obj.var)



# #built in attributes in class
# 1. .__dict__  Dictionary containing the class namespace
# 2. .__doc__   If there is a class documentation class, this returns it. Otherwise, None
# 3. .__name__  Class name.
# 4. .__module__	Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# 5. .__bases__	A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

# In[161]:


class abc:
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var 1 is =",self.var1)
        print("var 2 is = ",self.var2)
obj=abc(10,12.34)
obj.display()
print("obj.__dict__ is =",obj.__dict__)
print("obj.__doc__ is =",obj.__doc__)
print("obj.__name__ is =",abc.__name__)
print("obj.__module__ is =",obj.__module__)
print("obj.__bases__ is =",abc.__bases__)


# In[ ]:


class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("enter the marks of %s in subject "))


# In[165]:


import gc
collected =gc.collect()
print("garbage collector ",collected)
print("garbage collection threshold",gc.get_threshold())


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




