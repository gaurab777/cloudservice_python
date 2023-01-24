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






