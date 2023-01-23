#Arithmetic Operators
d = 20
e = 5

print("Addition of d and e is ",d+e)

print("Substraction of d and e is ",d-e)

print("Multiplication of d and e is ",d*e)

print("Division of d by e is {}".format(d/e))

print("Modulus of d/e is ",d%e)

print("Floor divion of d/e is ",d//e)

print("2 Power d id ",d**2)


#Relational(Comparision) Operators
print(d<e)

print(d>e)

print(d>=e)

print(d<=e)

print(d==e)

print(d!=e)


#Assignment Operators
f = 100
print(f)

f += 10 #Same as, f= f+10
print(f)

f *= 10 #Same as, f= f*10
print(f)

f **= 2 #Same as, f= f**2
print(f)


#Bitwise Operators
g= 60
h = 13

print("Bitwise AND of g and h is ", g&h)

print("Bitwise OR of g and h is ", g|h)

print("Bitwise XOR of g and h is ", g^h)

print("Bitwise NOT of g is ", ~g)


#Logical Operator
i = 10
j = 20

if (i>5 and j<15):
    print("Yes")
else:
    print("No")

if (i>5 or j<15):
    print("Yes")
else:
    print("No")

print(i>j and i<20)
print(i>j or i<20)


#Membership Operators (in, not in)
L = [10,20,30,40]

print(20 in L)
print(200 not in L)


#Identity Operators (is, is not)
k=10
print(k is 11)
print(k is not 11)


#DECISION MAKING

#If statement
m= 15
if (m>10):
    print("a is greaker")

#if ...else statement
n=305
o=405
if n>o:
    print("n is greater")
else:
    print("o is greater")

p=5001
if p%2==0:
    print("Even number")
else:
    print("odd number")


#Nested if statement
q= 49
if (q>40):
    if q>50:
        print("q is greater than 50.")
    else:
        print("q is less than 50.")
else:
    print("q is less than 40.")


# elif statement
r=15
s=20

if r>s:
    print("r is greater than s.")
elif r == s:
    print("r is equal to s.")
elif r<s:
    print("r is less than s.")





#LOOPS

#Types of loops
#- For loop
#- While loop
#- Nested loop


#For Loop

for letter in 'Expert':
    print("Current letter is:", letter)

#range() function

for x in range(10):
    print(x)

for y in range(15,20):
    print(y)

for z in range(5):
    print("Hello world")

for t in range(10,101,10):
    print(t)

count = 0
while (count < 6):
    print("The count is:",count)
    count = count+1

table = 8
while table < 81:
    print(table)
    table+=8

for i in range(1,6):
    for j in range (1,i+1):
        print(i, end="")
    print()







