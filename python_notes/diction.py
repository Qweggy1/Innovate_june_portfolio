# print("This is dictionaries")
# _______________________________________________________
#                 #Dictionaries

# # They are like lists but they store key:value pairs

# my_dog = {
#     "name":"Belle",
#     "colour":"White",
#     "mood":"Happy"
# }

# my_cat = {
#     "name":"Willow",
#     "colour":"Tabby",
#     "mood":"Schizophrenia"
# }
# # selecting a value using a key instead of index.

# print(my_dog["mood"]) 

# # Dictionaries do not have a numberd index


# #keys() --- print(my_dog.keys())
# #values() - print(my_dog.values())
# #items() -- print(my_dog.items())
# #get() ---- print(my_dog.get("name"))

# # print(my_dog["legs"])
# # print(my_dog.get("legs","Its a dog it has 4, 4 legs well in most cases"))

# # print(my_dog.keys()) # messy in print
# # print(list(my_dog.keys()))

# # for i in my_dog.keys():
# #     print(i)

# my_dog.update({"legs":"4"}) #update method
# my_dog.update({"name":"Belle the fluff"})
# print(my_dog)

# my_dog.pop("mood") # pop can be used in dictionarys
# print(my_dog)