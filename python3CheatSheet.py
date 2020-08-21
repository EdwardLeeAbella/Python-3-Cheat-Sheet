#Python 3 version crash sheet
import math
import random


#Hello world
print("Hello World")

# Strings
print('this is a string')
print("This is also a string")
print("""This is a long Strings
 long string   """)

# Number types in python
# int, float, complex
int1 = 4141242 # this is int
float1 = 321.22 # this is float
complex1 = 3 + 5.7j # this is complex number

# Arithmetic
#Operations : + - * / % //
int2 = 2
float2 = 6.0
complex2 = 12 + 0j
#addition
int2 + float2 #int + float
#subtraction
float2 - int2
#multiplication
int2 * 7
#division
complex2 / float2

#Booleans : True = 1 and False = 0
int3 = 3
int4 = 5
int3 == int4
int3 != int4

# If, then, else
insert = input("Enter your name : ")
if len(insert) <= 6:
    print("Your name is too short")
    print("Enter again a name")
else:
    print("Next")

#functions
def function():
    pass
def function1():
    print("This is a function")
    print("inside a function")
print("this is outside the function")

def volume(r):
    """Returns the value of a sphere with radius r"""
    volOfSphere = (4.0/3.0) * math.pi * r**3
    return volOfSphere
volume(2)

#loops
#For loops
for i in range(1, 10):
    print(i)
    #print out 1 to 10
#While loops
while True: #Boolean
    for i in range(1, 6):
        print(i)
    break # break the while loop after above instruction

#Data structures of python: dictionary, list, tuples

#lists = ordered data
list1 = [2]
list1.append(4)
list1.append(1)
list1.append(3)
#list1.append(args) adds an element to the list
#list1[2:3] slicing the elements from indices 2 to 3

#Dictionaries contains key = input and a value = output
post = {'user_id': 209, 'message': 'edadawdada', 'language': 'english'}
#unpack dict
for key in post.keys():
    value = post[key]
    print(key, "=", value)

#another way to unpack dict
c = {}
c["Edward"] = 25
c["Maegan"] = 23
for key, value in c.items():
    print("Key: ")
    print(key)
    print("Value: ")
    print(value)
    print()

#tuples collection of the in ordered elements (immutable)
tuples1 = 1, 2, 3
print(tuples1)
#age, country, knows_python
survey1 = (27, "vietnam", True)
#unpack tuples
age, country, knows_python = survey1
print("Age = ", age)
print("Country =", country)
print("knows python", knows_python)

# Classes and object

#Creating a class called Robot
class Robot:
    # Declaring the args by using init function
    def __init__(self, name, age, loveInterest):
        self.name = name
        self.loveone = loveInterest
        self.age = age

    def introduce_self(self):
        print("My name is : " + self.name)
        print("My age is : " + self.age)
        print("My love is : " + self.loveone)

# Creating an object of the class Robot
r1 = Robot("Edward", "22", "Maegan")
r1.introduce_self()
# Another object of the class Robot
r2 = Robot("Maegan", "22", "Edward")
r2.introduce_self()
























