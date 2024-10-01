#     Day 1

print("Hello World")
print(5)

#     Day 3

import pandas  # This is an example of external module
import hashlib  # This is an example of built in module

print("Hi")

# Dont worry about how to use these modules just yet!
pandas.read_csv("one.csv")
m = hashlib.sha256()

#     Day 4

print("Hello World", 7)
print(5)
print("Bye")
print(17*13)

#     Day 6

a = complex(8, 2)
b = True
c = "Harry"
d = None
print(a)
print(b)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))


list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)


#     Day 7

print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(5%3)
print(2**4)

#     Day 9

a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)

#     Day 10

a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)

print(int(x) + int(y))

#     Day 11

name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)

#     Day 12 

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

#     Day 13

# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

#     Day 14

a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")

applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

#     Day 16

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

#     Day 17

name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k + 1)
  
for k in range(1, 20001):
  print(k)

for k in range(1, 12, 3):
  print(k)

#     Day 18

i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")
 
# syntax for do while loop in other language like C , C++ , Java 
# do {
#   loop body;
# }while(condition);

#     Day 19


for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break

#     Day 20

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
gmean1 = (a*b)/(a+b)
print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
gmean2 = (c*d)/(c+d)
print(gmean2)

#     Day 21

def average(a, b, c=1):
  print("The average is ", (a + b + c) / 2)


def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  return 7
  return sum / len(numbers)


average(4, 6)
average(b=9)

c = average(5, 6, 7, 1)
print(c)


 def name(**name):  
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")

#     Day 22

marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3])                # Negative index
print(marks[len(marks)-3])      # Positive index
print(marks[5-3])               # Positive index
print(marks[2])                 # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#     Day 23

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m)
print(l)
 
#     Day 24

tup = (1, 2, 76, 342, 32, "green", True)
tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

#     Day 25

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

#     Day 28

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))

#     Day 29

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)

#     Day 30

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

"""
def fibonacci(n):
  if (n == 0):
    return 0
  elif(n == 1):
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
"""
