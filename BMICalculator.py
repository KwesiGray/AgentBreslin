print("--___WLECOME TO MY BMI CALCULATOR___--")
print("-")
print("Please Enter your name below.")
name = input("")
print("Enter your Age Below.")
age = int(input(""))

print("Enter your Height Below in meters.")
height = float(input())

print ("Enter your respective weight below in Kg.")
weight = float(input(""))

import time
print("----Calculating Your Body Mass Index in 5 seconds----")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
bmi = weight/height**2
print("Your Name is: "+ name)
print("Your Age is: "+ str( age))
print("Your Respective Weight is: "+ str(weight),"kg")
print("Your Respective Height is: "+str(height),"m")
print("Your B.M.I is: " + str(bmi)+"kg")

print("-------------------------------------")
print("_")
print("-DOCTORS REPORT IN 5 SECONDS_ _ _ _")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

if(bmi<=18.5):
    print(name + " You Are UnderWeight!")
    print("A Good Blanced Diet is Recommended")
elif(bmi>19 and bmi<24.5):
    print(name+" You are in your Best Condition")
    print("Keep Up with the Good Healthy Living!")
    
elif(bmi>25.0 and bmi<39.9):
    print(name+" You are in the OverWeight category")
    print("A Daily Exercising Routine is Recomended!! ")
        
else:
    print("YOU ARE OBESE !! "+ name)
    print("You need the Doctor ASAP!")
    
print("Closing BMI Calculator in 10 Seconds")
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("----!----")



