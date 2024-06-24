# 1) Intro
print("Hello World")
print(10+2)


# 2) Use of comments
#this is comment
#This is
#multi line comment
"""This is 
       multi line comment"""


# 3) Variables
x = 5
y = "Johnny"
print(x)
print(y)
print(type(x))
print(type(y))

#diff variable type
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0

#double and single quotation
d = "John"
# is the same as
e = 'John'
print(d+e)

#Case Sensitive
f = 4
F = "Sally"
print(f)
#F will not overwrite f


# 4) Variable Name
#Camel Case
myVariableName = "Hitesh"
#Pascal Case
MyVariableName = "Hitesh1"
#Snake Case
my_variable_name = "Hitesh2"


#5) Multiple value
g, h, i = "Orange", "Banana", "Cherry"
print(g)
print(h)
print(i)


#6) Unpacking collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#7) Output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x+y+z) #(+ can also be used if same data type)

x = 5
y = "John"
print(x, y) #Note that replacing , by + would throw error


#8) Global Variable (Create a variable outside of a function, and use it inside the function)
# i)
x = "awesome"
def myfunc():  #function is defined
  x = "fantastic"  #this x is only defined under function
  print("Python is " + x)

myfunc()

print("Python is " + x)

#ii)
x = "awesome"

def myfunc():
  global x  #This command destroys previous global x and command to form new global x
  x = "fantastic"
  print("Python is "+ x)

myfunc()

print("Python is " + x)


#9) Python Numbers
#i)
x = 1
y = -35.59
z = -5j #j represents the imaginary part

print(type(x))
print(type(y))
print(type(z))

#ii)
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

#iii) Random number generator
import random  #module has to be imported

print(random.randrange(1, 10))

print(type(x))
print(type(y))
print(type(z))
