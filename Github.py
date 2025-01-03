#TUPLES 
Mytuple=("apple","cherry","batman","superman")
print(Mytuple[2:5])
if "superman" in Mytuple:
    print("YES")
print(Mytuple)
y=list(Mytuple)#this is one method of adding something after the tuple has been created
y[1]="kiwi"
Mytuple=tuple(y)
print(Mytuple)
print(Mytuple * 2)


#MY OWN PROBLEM
ruits=["apple","berry","orange","guava"]
odd_places=[]

for i in range(len(fruits)):
    print(i)
    if i % 2 == 0:
        odd_places.append(fruits[i])

print(odd_places)


#ABOUT LISTS 
ylist=["apple","banana","soft"]
Mylist[2]="lemon"#changes list items 
Mylist.append("guava")#adds lists items 

Mylist.insert(1,"papaya")#adds list items 

Mylist1=["nutella","twix","lindor"]
Mylist.extend(Mylist1)
Mylist.remove("nutella")
Mylist.sort()
Mylist.sort()
print(Mylist)



#MY OWN PROBLEM
import random

def myfunc():
    random_number=random.randint(1,100)
    print("Rxxx")
    print(random_number)
    print("Rxxx")

for i in range(51):
    myfunc()
    print("Iter---")
    print(i)
    print("Iter---")


#step1:creats a random number 
#step2:then prints it
#step3:and then goes in loop 
#step4:again goes into and generates a random number 



#GLOBAL 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



def myfunc():
  global x #global represents the item outside it 
  x = "fantastic"

myfunc()

print("python is "+ x) 


#slicing of a string
a="hello"
print(a[1]) 


fruits = ["apple","mango","guava"]
x ,y ,z=fruits
print(x)


#FOR LOOPS
if 5 > 2:
    print("five is greater than two")


    for x in "banana":
    print(x)#loop through banana first every letter and goes back repets the process again and again this it finishes




#IF AND ELSE LOOPS 
txt="the best things in life are for free"
if "free" in txt:#for checking if some phrase is there in the sentence we use "in"
    print("YES")
else:
    print("NO") 



#STRINGS 
a=" hello, world! "
print(a.strip()) 

a="Hello, World!"
print(a.replace("H","J"))

a="Hello"
b=" World"
print(a+b)

age=str(36)
txt="My name is john and My age is" +" "+ age 
print(txt)

price = 59
txt = f"The price is {price:.1f} dollars"
print(txt)

txt=f"The price is {20 * 5} of a toy"
print(txt)    


x=5
y="sally"
print(type(x))
print(type(y))