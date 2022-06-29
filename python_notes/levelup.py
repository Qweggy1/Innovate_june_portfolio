import random
# _______________________________________________________
                #Beginning

# print("Level up!")

# int() #creates an integer data type 
# float() #creates a decimal point data type
# # str() #string

# print(int(5.4)) # Will always round up
# print(int("54"))
# print(type(int("54"))) # What class type is it
# ______________________________________________________
                #Casting
# balance = 547

# deposit = int(input("How much do you want to deposit? "))      # `` forcing an interger to be typed

# balance +=deposit

# print(f"You have {balance}")
#______________________________________________________
                # Truthy and Falsy

#Falsy values are empty the number 0 or data type none or booleon False are all Falsy, "empty space" is a charecter in python this would be Truthy. 

#Everything else is truthy

# print("What is your name? ")
# name = input()

# if name:
#     print(f"Welcome {name} to Innovate")
# else:
#     print("Incorrect Log In")

#______________________________________________________
                #Not and In Operator

# allowed=["Blake","John","Laura","Kristian","Alana"]
# name=input("What is your name? ")

# while name not in allowed: #not in will check list for names in allowed
#     print("Your name isnt here? ")
#     print("Say again?")
#     name=input("What is your name? ")

# print("You can come in!")
#______________________________________________________
                #Try/Accept

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     print(num1 + num2) # This is contanation, incorrect in this aspect. 
# add_up()

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(int(num1) + int(num2)) 

# Try and Accept Similar to IF WHATIF AND ELSE
# 
#Except would give our own personal error message.
#     except:
#         print("Please use numbers and no letters only!")
#         print("Try again? ")
#         add_up()

# add_up()
#______________________________________________________
                #Scope - global/local variable

# light = False

# def light_switch():
#     if light:
#         print("Whoa! It's bright in here")  #THIS WILL NOT RUN AND ERROR OF LIGHT REFERENCED BEFOR ASSIGNMENT
#         light = False <--- New Variable not reading from line 76 
#     else:
#         print("Who turned out the lights")
#         light = True

# light_switch()
# light_switch()

# light = False

# def light_switch():
#     global light # <--- It needs a Global Variable
#     if light:
#         print("Whoa! It's bright in here")  
#         light = False
#     else:
#         print("Who turned out the lights")
#         light = True

# light_switch()
# light_switch()
# _______________________________________________________
                #Lists and Tuples
#Lists and typles are are a collection of values

# List []
# Tuple () - Can not be changed

# even_nums =[2,4,6,8,10] <--- [] This is a list
# even_nums.insert(0,0)
# print(even_nums)

# odd_nums=(1,3,5,7,9) <--- () This is a tuple

# odd_nums.append(11) # <-- This is a tuple by using () and not [] so therefore can not be changed. If changed to [] it would run as this is know a list. 
# _______________________________________________________
                #Slice Notation

# fav_genre =[
#     "Drum and Bass",
#     "Techno",
#     "Trance",
#     "Rock",
#     "Dance",
#     "Pop"

# ]

#  print(fav_genre[1:2:1])# < Slice Notation Start:Stop:Step

# start:stop:step
# print(fav_genre[1]) #this is an index position - it is the start value
# print(fav_genre[1:2:1]) #this is actually what is happening - starting at one, stopping short of 2, and stepping by 1 at a time
#  make a string Variable
#  if it reads forwards the same as backwards
#  if it does say YES if it doesn't say no
#  print(fav_genre[::])

# test = "madam"
# if test == test[::-1]:
#     print(f"Yes! {test} is a palindrome")
# else:
#     print("It is not a palindrome")
#________________________________________________________
                #while True

# This is a while loop that compares a variable and runs under a condition.

# num=random.randint(1,50)

# while num%2==0:
#     print("This even lets go again")
#     num=random.randint(1,50)

# #if the number is odd, the while loop will never run

# print("Oh its odd, try again")

# while True:
#     num=random.randint(1,50)
#     print(num)
#     if num%2==0:
#         print("Its an even number! lets go again")
#         continue
#     else:
#         print("Oh its odd try again ?")
#         break

# # This while loop will always initialise It might go straight to the else/break - but it will have started.
#________________________________________________________