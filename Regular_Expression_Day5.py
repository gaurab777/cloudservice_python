#REGULAR EXPRESSION

#match() Function
import re
line = "Learning Data Science"
matchObj = re.match(r'(.*)en', line)
print(matchObj)

line = "Learning Data Science"
matchObj = re.match(r'(.*) en', line)
print(matchObj)
print("-----------------------------------------------------------------")


#Use of search() function
txt = "Data Scientists are in huge demand"
x = re.search("Scientists", txt)
y = re.search("[0-9]", txt)
print(x)
print(y)
print("-----------------------------------------------------------------")


#re.match() vs re.search()
substring = "science" #pattern
string = "You are learning data science with python programming"
print(string)

#use of re.search() method
print(re.search(substring, string, re.IGNORECASE))

#use of re.match() method
print(re.match(substring, string,  ))
print("-----------------------------------------------------------------")

#use of findall() function
txt1 = "You are becoming data scientist"
txt2 = "It is raining outside"
x = re.findall("are", txt1)
y = re.findall("in", txt2)
print(x)
print(y)
print("-----------------------------------------------------------------")


#split() function
txt3="the rain in Spain"
x1 = re.split("\s", txt3) #\s matches a single whitespace character
print(x1)
print(txt3.split())
x2 = re.split("\s", txt3, 1) #split the string only at the first string
print(x2)
print("-----------------------------------------------------------------")


#sub() function
txt4 = "I am Gaurab Bam."
x3 = re.sub("\s","9",txt4)
print(x3)

x4 = re.sub("\s","y",txt4,2) #Replace only the first 2 occurences
print(x4)



