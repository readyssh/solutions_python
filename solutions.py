'''
print("---------- Attendence problem ------------")

print("Enter your Attendence to see  :"))
num = int(input("Enter your percentage :"))

if num > 75:
    print("You are allow to sit in exam")
else:
    print("You are not allowed to sit in exam")
    var = input("Do you have a medical cause type Y for YES or N for NO :")
    if var == "Y":
       print("You are allowed")
    elif var == "N":
       print("You are not allowed")
    else:
       print("Wrong Input")

print("---------- Odd even number problem ------------")

num = int(input("Enter a number "))

if num % 2 == 0:
   print("It's a even number")
elif num % 2 == 1:
   print("It's a odd number")
else:
   print("Invalid Input")

print("---------- School grading system ------------")

num = int(input("Enter your percentange :"))

if num >= 80:
   print("You got : A grade")
elif (num < 80 and num >= 60):
   print("You got : B grade")
elif (num < 60 and num >= 50):
   print("You got : C grade")
elif (num < 50 and num >= 45):
   print("You got : D grade")
elif (num < 45 and num >= 25):
   print("You got : E grade")
elif (num <= 24):
   print("You have failed in Exam")
else:
   print("Invaild Input")


print("--------- Artimatic problems -------- ")
#1
x=2
if(x == 2):
   print("hello")
else:
   print("bye")
#2
x=2
if(x != 5):
  print("hello")
else:
  print("bye")
'''
#3
x=2
y=0
if (x != 5 ) & (y >= 5):
  print("hello")
else:
  print("bye")








































