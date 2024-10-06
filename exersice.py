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

#     Exersice 3

questoins = [
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4]
    ["Which language used to make Facebook","Python","HTML","PHP","Javascript","None",4] 
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questoin)):
    questoin = questoins[i]
    print(f"\n\nQuestions for Rs. {levels[i]}")
    print(f"a. {questoin[1]}          b. {questoin[2]}")
    print(f"c. {questoin[3]}          d. {questoin[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == questoin[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000 
        elif (i == 9):
            money = 320000
        elif(i ==14):
            money = 10000000
    else:
        print("Wrong answer!")
        break 

print("Your take home money is {money}")

#     Exersice 4

st = input("Enter message:")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding:")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  

