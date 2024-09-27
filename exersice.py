#     Exersice 1

a = 50
b = 3

print("The value of", a, "+", 3, "is: ", a + b)
print("The value of", a, "-", 3, "is: ", a - b)
print("The value of", a, "*", 3, "is: ", a * b)
print("The value of", a, "/", 3, "is: ", a / b)

#     Exersice 2


import time

t =time.strftime(' %H : %M : %S ')
name = input("Enter your name: ")
hour = int(input('Using 24 hour format, Enter your current time Hour : '))
print(hour)
if hour >= 0 and hour < 12 :
    print("Good Morning Sir", name, "!")
elif hour >= 12 and hour < 17:
    print("Good Afternoon Sir", name,"!")
else:
    print("Good Night Sir", name,"!")
