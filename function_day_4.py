#FUNCTIONS In Python
def pow(x,y):
    result= x**y
    print(x,"raised to the power",y, "is", result)

pow(5,3)

print("-----------------------------------")

def sum(num1, num2):
    s=num1+num2
    return s

x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
print("Sum of two numbers is: ",sum(x,y))
print("-----------------------------------")

def mult(p,q,r):
    m=p*q*r
    return m

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(mult(a,b,c))
print(mult(a,b,c))
print("-----------------------------------")

#Function without arguments and return type
def display():
    print("Hello World")

display()

#Function without argument, with return type
def display2():
    return "Hello World!!!"

print(display2())
print("-----------------------------------")


#Types of Functions
#->Pre-defined Function
#->User-defined Function
#->Anonymous Function=> they are not declared in the standard manner by using the 'def' keyword. 'lamda' keyword to create small anonymous functions.

#Anonymous function
# Syntax: lamda-> parameter_1,parameters..->:->expression
sum2=lambda N1,N2: N1+N2
X=int(input("Enter 1st number: "))
Y=int(input("Enter 2nd number: "))
print(sum2(X,Y))
print(sum2(10,40))
print("-----------------------------------")

mult2= lambda n1,n2,n3: n1*n2*n3
X=int(input("Enter 1st number: "))
Y=int(input("Enter 2nd number: "))
Z=int(input("Enter 3rd number: "))
print(mult2(X,Y,Z))
print("-----------------------------------")



#Recursive Function
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print("Factorial of number is ", end="")
print(fact(6))
print("-----------------------------------")
print("-----------------------------------")


#MODULE
import calculator

print(calculator.add3(10,20))
print(calculator.subt3(40,10))
print(calculator.mult3(100,20))
print("-----------------------------------")


#from .. import

from math import sqrt, factorial
print(sqrt(81))
print(factorial(9))
print("-----------------------------------")

import math
print(sqrt(25))
print(factorial(5))
print("-----------------------------------")

import calculator as c #Renaming imported module
print(c.add3(10,20))
print(c.subt3(40,10))
print(c.mult3(100,20))
print(dir(c))
print("-----------------------------------")


# Import built in module math
print("Math module")
import math
print(dir(math)) # to know the functions of the modules
print("-----------------------------------")


# From --- import *
from math import *
print(pow(5,3))
print(radians(30))
print(sqrt(36))
print(degrees(0.5239))
print("-----------------------------------")


#Getting current working directory
import os
print(os.getcwd())


















