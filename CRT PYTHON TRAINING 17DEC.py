#!/usr/bin/env python
# coding: utf-8

# In[3]:




class Fruits:
    def taste(self):
        raise NotImplementatedError()
    def rich(self):
        raise NotImplementatedError()
    def color(self):
        raise NotImplementatedError()
class Mango(Fruits):
    
    def taste(self):
        return "sweet"
    def rich(self):
        return "Vitamin-A"
    def color(self):
        return "Golden yellow"
    
class Orange(Fruits):
    
    def taste(self):
        return "sour"
    def rich(self):
        return "Vitamin C"
    def color(self):
        return "Orange"
Alphanso=Mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())
O=Orange()
print(O.taste(),O.rich(),O.color())
    
    


# In[6]:


import keyword as kw
print(kw.kwlist)


# In[ ]:


#meta classes
        class of a class

        instance    instance


# In[12]:


#polymorphism--->(means change of state of object)
#program to interviene polymorphism on a complex number 
class Complex():
    def __init__(self):
        self.r=0
        self.i=0
    def setvalue(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c):
        temp=Complex()
        temp.r=self.r+c.r
        temp.i=self.i+c.i
        return temp     
    def display(self):
        print("(",self.r,"+",self.i,"i)")

c1=Complex()
c1.setvalue(1,2)
c2=Complex()
c2.setvalue(3,4)
c3=c1+c2
c3.display()       


# operator -------------------->function name
# + --------------------------->__add__
# - --------------------------->__sub__
# += --------------------------->__iadd__
# -= ---------------------------->__isub__
# * ----------------------------->__mul__
# *= ----------------------------->__imul__
# / ----------------------------->__truediv__
# /= ----------------------------->__idiv__
# ** ----------------------------->__pow__
# **= ----------------------------->__ipow__
# % ------------------------------->__mod__
# %= ------------------------------->__imod__
# >> ------------------------------->__rshift__
# >>= ------------------------------->__irshift__
# &  --------------------------------->__and__
# &= --------------------------------->__iand__
# 
# 
# | ---------------------------------->__or__
# |=---------------------------------->__ior__
# 
# ^ --------------------------------->__xor__
# ^=--------------------------------->__ixor__
# ~ ---------------------------------> __invert__
# ~= ---------------------------------> __iinvert__
# 
# > ----------------------------------> __gt__
# < ----------------------------------> __lt__
# >= ----------------------------------> __ge__
# <= ----------------------------------> __le__
# 
# << ---------------------------->__lshift__
# 
# 

# In[21]:


#program that has abstract class to derive 2 classes 
#rectangle and triangle from polygon class
#write the methods to get their details and dimensions and calculate the area

class Polygon:
    def getdata(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()
        
class Rectangle(Polygon):
    
       
        
    def area(self):
        print("Area of rectangle",self.length*self.breadth)
        
    
    def getdata(self):
        self.length=float(input("enter the length of rectangle:"))
        self.breadth=float(input("enter the breadth of rectangle:"))
        self.area()
        
    
    
    
class Triangle(Polygon):
    
       
        
    def area(self):
        print("Area of Triangle",0.5*self.length*self.breadth)
        
    
    def getdata(self):
        self.length=float(input("enter the height of triangle:"))
        self.breadth=float(input("enter the breadth of triangle:"))
        self.area()
        
    
R=Rectangle()
R.getdata()

t=Triangle()
t.getdata()


# In[23]:


#encapsulation public memebers

class pub:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        
    def Num(self):
        print("roll no is ",self.rno)
        

p=pub("SAI",3011)
p.Num()


# In[24]:



class pub:
        
    def Num(self):
        
        print("roll no is ",self.rno)
        
    def display(self):
        print("name  is ",self.name)
        print("roll no is ",self.rno)
        
        
        
        
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        self.display()
        

p=pub("SAI",3011)
p.Num()


# In[33]:


#method overload the call method (__call__ )
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,o):
        return self.num*o
        
x=multi(10)
x.__call__(5)
print(x(5))


# In[43]:


#method override  get item and set item method
class Mylist:
    def __init__(self,List):
            self.List=List
        
    def __getitem__(self,index):
            return self.List[index]
        
    def __setitem__(self,index,num):
        self.List[index]=num
        
    def __len__(self):
        return len(self.List)
    
    def  display(self):
        print(self.List)
    
l=Mylist([1,2,3,4,5,6,7,8,9])
l.display()
index=int(input("enter the index of the list "))
print(l[index])
index=int(input("enter the index of the list "))
num=int(input("enter the position u want to modify:"))
l[index]=num
l.display()
print(" the length of list:",len(l))


# In[55]:


#special methods or miscelleneous functions in overloading

class number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self.num)
    def __oct__(self):
        return oct(self.num)
    
    def __setitem__(self,num):
        self.num=num
    

n=number(-14)
print(n.display())
n=abs(n)
print("converting to float ",float(n))
print("converting to hex ",hex(n))

print("converting to hex ",hex(n).replace("0x",""))
print("converting to hex ",hex(n)[2:])
print("converting to oct ",oct(n))



# In[67]:


#to visualize inheritance flow

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",(self.name))
        print("age is ",(self.age))
        
class Teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
        
    def display(self):
        person.display(self)
        print(" experience",self.exp)
        print("research area=",self.rarea)
        
        
        
class Student(person):
    def __init__(self,name,age,courses,marks):
        person.__init__(self,name,age)
        self.courses=courses
        self.marks=marks
    def display(self):
        person.display(self)
        print("courses=",self.courses)
        print("marks",self.marks)
        

print("----------teacher details-----------------")
t=Teacher("SAI",43,15,"CS")
t.display()
print("----------student details-----------------")
s=Student("SAM",20,"B.TECH",85)
s.display()


# In[82]:


n=(input())
print(int(n,18))


# In[71]:


st=input()
n=len(st)
print(st.center(10+n,'#'))


# In[86]:


#program to invoke __init__in multiple inheritance
class base1(object):
    def __init__(self):
        print("base class 1 ")
class base2(object):
    def __init__(self):
        print("base class 2 ")

class Derived(base1,base2):
    pass
D=Derived()
    


# In[89]:


#program to call constructor of a base class from Super class
class base1(object):
    def __init__(self):
        print("base class 1 ")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2 ")

class Derived(base1,base2):
    pass
D=Derived()
    


# In[93]:


#program to call constructor of a base class from Super class
class base1(object):
    def __init__(self):
        print("base class 1 ")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2 ")

class Derived(base1,base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class ")
D=Derived()
    


# In[101]:


#to visualize inheritance flow

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",(self.name))
        print("age is ",(self.age))
        
class Teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
        
    def display(self):
        person.display(self)
        print(" experience",self.exp)
        print("research area=",self.rarea)
        
        
        
class Student(person):
    def __init__(self,name,age,courses,marks):
        person.__init__(self,name,age)
        self.courses=courses
        self.marks=marks
    def display(self):
        person.display(self)
        print("courses=",self.courses)
        print("marks",self.marks)
        

print("----------teacher details-----------------")
t=Teacher("SAI",43,15,"CS")
t.display()
print("----------student details-----------------")
s=Student("SAM",20,"B.TECH",85)
s.display()

print(" T IS Teacher :",isinstance(t,Teacher))
print(" S is Student ",isinstance(s,Student))

print(" p is Student ",isinstance(s,Student))

print(" S is Student ",isinstance(s,int))
print(" S is Student ",isinstance(s,person))
print(" person is a subclass of teacher",issubclass(person,Teacher))
print(" teacher is a subclass of person",issubclass(Teacher,person))
print(" boolean is a subclass of",issubclass(bool,int))


# In[104]:


#multilevel
class person:
    def name(self):
        print("name is  Sai")
    
        
class Teacher(person):
    def qual(self):
        print("qualification in phd")
        
class hod(Teacher):
    def exp(self):
        print("experience is 22 yrs")

HOD=hod()
HOD.name()
HOD.qual()
HOD.exp()


# In[112]:


#multipath

class student:
    def name(self):
        print("name is  Sai")
    
        
class academic(student):
    def acad_score(self):
        print("academic score is 90%  above")
        
        
class CSE(student):
    def CSE_score(self):
        print("CSE  Score ---------------70% and above")
        
class result(academic,CSE):
    def eligibility(self):
        print("_____________eligibility to apply____________________")
        self.acad_score()
        self.CSE_score()

        
r=result()
(r.eligibility())


# In[21]:


class Student:
    name="Sai"
    __rollno=3011
    
    def get_rollno(self):
        return self.__rollno
    def set_rollno(self,number):
         self.__rollno=number
        
    
obj=Student()
print(obj.name)
#to declare a variable as private use __rollno
r=obj.get_rollno()
print(r)
print(obj.set_rollno(11))


# In[ ]:


class A:
    def m1(self):
        print("in class A")
        
class B:
    def m1(self):
        print("in class B")


# In[23]:


n=int(input())
def user():
    usr=[]
    for i in range(n):
        ele=input()
        usr.append(ele)
    return dict(usr)


k=user()
print(k)
    


# In[38]:


l=['username','passwd']
d={}
n=int(input("enter the number of users:"))
for i in range(n):
    k=input("enter user name:")
    y=input("enter password:")
    d[k]=y
    
print(d.keys())


# In[35]:


arr=[]
n=int(input("enter the number of users:"))
for i in range(n):
    k=input("enter user name:")
    y=input("enter password:")
    arr.append({k:y})

    
print((arr))


# In[44]:


l=['username','passwd']
d={}
n=int(input("enter the number of users:"))
for i in range(n):
    k=input("enter user name:")
    y=input("enter password:")
    d[k]=y
    
print(d.keys())
print(d.values())
chkusr=input("enter username to check:")
chkpswd=input("enter password to check:")

if chkusr in d.keys():
    print(chkusr,"valid user")
else:
    print(chkusr,"Invalid user")
if chkpswd in d.values():
    print(chkpswd,"valid user")
else:
    print(chkpswd,"Invalid user")
    


# In[46]:


arr=[]
n=int(input("enter the number of users:"))
for i in range(n):
    k=input("enter user name:")
    y=input("enter password:")
    arr.append({k:y})

    
print((arr))
u1=input("username:")
p1=input("Password:")
found=False
for obj in arr:
    try:
        pd=obj[u1]
        found=True
        if(pd==y):
            print("Valid Password")
        else:
            print("Invalid user")
    except:
        pass
    
if found==False:
    print("Username not found")


# In[62]:


#stack
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)


stack.popleft()

print(stack)


# In[ ]:


queue=[]


# In[ ]:





# In[61]:


s=input()
for i in range(len(s)):
    if(i&1==0):
        print(s[i],end="")
    else:
        print(" ",end="")


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




