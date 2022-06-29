import random
# print("This is my file")

# greeting = ("Hello World")

# print(greeting)

# print("This is a string for displaying charecters")

# #Booleon TRUE AND FALSE
# #Float Number with DECIMAL 1.4
# #Interger Whole Numbers 14

# print(1234+1) #this is an interger/whole number
# print(12.34) #this is a float
# print(True)
# print(False) #these are booleons True & False
# print(None) #none - blank/nul data

# print((greeting[1])) INDEX POSITION

# print(greeting[-1])

# print(greeting.upper())

# print(greeting.lower())

# print("HeLlO".capitalize())

# print("hello welcome to code nation".count("o"))

# print("Welcome to code Tnation".find("T"))

# print("The quick brown fox".replace("fox","Frog"))

# print(("The quick brown fox").strip("fox"))

# print(random.random()) #Random Float num between 0,1

# print(random.uniform(1,10)) #Random Float num between 1,10

# print(random.randint(1,10)) #Random Integer between input

# my_name="Qweggy" # Variables
# my_age=29
# student=True

# print(my_name,my_age,student)

# print("Hello my name is", my_name)
# print("I am", my_age)

# print("Hello my name is {} and I am {} years old".format(my_name, my_age)) # Older format method

# f string, new best method
# print(f"Hello my name is {my_name} and i am {my_age}")
#______________________________________________________
                        #Mathmatics


# print(5433+42821)
# print(5473982-321414) # Mathmatics using variables
# print(234*343)
# print(5**4)
# print(12%2)

# balance=1000
# print(balance)
# amount=30
                            # Basic Cash Machine
# balance=amount+balance
# balance +=amount
# print(balance)
# _____________________________________________________

# answer=input("What is your name? \n")  Input/Variables /n Escape charecter ( New Line )
# print(answer)


# IF STATEMENTS
#___________________________________
# music = "Drum & Bass"
# if music == "Classical":
#     print("Why are we listening to CLASSICAL")
# elif music == "Drum & Bass":
#     print("Yes TUNE")
#     print("Drum and bass is the best")
# else:
#     print("What is this?")
#____________________________________

# print(20%6==0) # Booleons are always active even if not stated in code
# _______________________________________________
# num=10
# num2=20

# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print("Both are equal")   
# 
# #if statements with math and mutiple variables.

# num=9
# num2=5

# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print("Both are equal")
# _______________________________________________

# place = "MCR"
# weather = "Rainy"

# if place =="MCR" and weather=="Rainy":
#     print("As is tradition")
# elif place =="MCR" and weather=="Cloudy":
#     print("Its going to rain")
# else:
#     print("Its never sunny")
# ___________________________________________________

                    #And and Or's

# day ="Monday"
# bank_hol = False
# if day == "Saturday" or day =="Sunday" or bank_hol:
#     print("Party")
# elif day =="Monday" or day =="Tuesday":
#     print("The weekend went to quickly")
# else:
#     print("When is it the weekend?")
# _____________________________________________________
                    #Functions

# def light_switch():
#     print("Who turned out the lights?")
#     print("Know its dark!")

# light_switch()

# def cash_withdrawel(amount, accnum):
#     print(f"Withdrawing {amount} from account {accnum}")

# cash_withdrawel(2345, 123456789)
# ______________________________________________________
                    #Lists

# fav_genre =[
#     "Drum and Bass",
#     "Techno",
#     "Trance",
#     "Rock",
#     "Dance",
#     "Pop"

# ]

# print(fav_genre)

# fav_genre [3] = "Metal" # Changing data in the list

# print(fav_genre) 

# print(len(fav_genre)) # Using LEN to count the items in a list

# fav_genre.append("RnB") # Adding to a list .append

# print(fav_genre)

# fav_genre.pop() # Removing from the bottom of the list

# fav_genre.pop(3) # Removing from anywhere on the list

# print(fav_genre)
# _______________________________________________________
                    #for Loops

# fav_genre =[
#     "Drum and Bass",
#     "Techno",
#     "Trance",
#     "Rock",
#     "Dance",
#     "Pop"

# ]

# for i in fav_genre: # For loop runs until it has nothing to index to
# print(i)

# for i in range(10):
#     print(i)
# Above is the same as below

                #start:stop:step
# for i in range(  0,   10,   1): 

#     #3rd number in parameter is how many it can jump to count to so 2, 4, 6, 8, the middle value is when to stop the 1st value is where it starts.

#     print(i)

# for i in range(10,-1,-1): # While loop counting down
#     print(i)
# ______________________________________________________
                #While Loops

# num = 0

# while num < 10: # Giving it a rule or it wont stop. 
#     num += 1
#     print(num)

# my_num = 28
# comp_num = random.randint(1,50) # Using random num gen to create a number between 1-50

# while my_num != comp_num:
#     print(f"The numbers {my_num} and {comp_num} do not match")
#     comp_num = random.randint(1,50)

# print(f"The numbers {my_num} and {comp_num} do match")
# _______________________________________________________
                # Activity #1

# cd = "Welcome to Code Nation today"
# print(cd)

# cdlen = len(cd)

# def cdleng():
#     if (cdlen % 2) == 0:
#         print(f"{cdlen} is even")
#     else:
#         print(f"{cdlen} is odd")

# cdleng()

# cd = "Welcome to Code Nation Todays"
# print(cd)

# print(len(cd))

# cdlen = 29

# if (cdlen % 2) == 0:
#     print(f"{cdlen} is even")
# else:
#     print(f"{cdlen} is odd")
# _________________________________________________________
                # Activity #2

# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

# for i in alpha:
#     print(i)

# answer=int(input("Type a number to see the letter!"))
# answer -=1
# print(alpha[answer])

# fav_genre =[
#     "1. Drum and Bass",
#     "2. Techno",
#     "3. Trance",
#     "4. Rock",
#     "5. Dance",
#     "6. Pop"

# ]
# print(fav_genre)

# print("What if your favorite genre out of the list? please type the corrosponding number")

