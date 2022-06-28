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

# Try and #Similar to IF WHATIF AND ELSE
# 
#Except would give our own personal error message.
#     except:
#         print("Please use numbers and no letters only!")
#         print("Try again? ")
#         add_up()

# add_up()
#______________________________________________________