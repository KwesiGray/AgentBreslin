print("--___WLECOME TO MY BMI CALCULATOR___--")
print("-")
print("Please Enter your name below!")
name = input("")
print("Enter your Age Below!")
age = int(input(""))

print("Enter your Height Below in meters")
height = float(input())

print ("Enter your respective weight below in Kg")
weight = float(input(""))

import time
print("--Calculating Your Body Mass Index in 5 seconds--")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
bmi = weight/height**2
print("Your name is: "+ name)
print("Your Age is: "+ str( age))
print("Your Respective Weight is: "+ str(weight),"kg")
print("Your Respective height is: "+str(height),"m")
print("Your BMI is: " + str(bmi)+"kg")

print("-------------------------------------")
print("_")
print("DOCTORS REPORT IN 5 SECONDS_ _ _")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

if(bmi<=18.5):
    print(name + " You Are UnderWeight!")
elif(bmi>19 and bmi<24.5):
    print(name+" You are in your best condition")
    
elif(bmi>25.0 and bmi<39.9):
    print(name+" You are in the OverWeight category")
        
else:
    print("YOU ARE OBESE !! "+ name)
    
print("Closing BMI Calculator in 10 Seconds")
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("----GOODBYE!----")



