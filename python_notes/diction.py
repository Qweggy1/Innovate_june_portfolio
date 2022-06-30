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
# ______________________________________________________
                #Dictionaries Activity 1

# countries = {
#     "United Kingdom":"London",
#     "France":"Paris",
#     "Germany":"Berlin",
#     "Spain":"Madrid",
#     "Italy":"Rome"
# }

# # countries.setdefault("Ethiopia","Addis Ababa")
# # countries.setdefault("Peru","Lina")

# # print(countries)

# # for i in countries.items(): # multiple ways to print the list
# #     print(i)

# # print(list(countries.items()))

# # for k, v in countries.items():
# #     print(k + " : " +v)         # Another way to print

# countries.update({"United Kingdom":"English","France":"French",
#     "Germany":"German",
#     "Spain":"Spanish",
#     "Italy":"Italian",
#     "Ethiopia":"Amharic",
#     "Peru":"Spanish"})

# print(countries)
# # _______________________________________________________
#                 #Dictionaries Activity 2

# fav_songs = [{
#     "Artist":"Linkin Park",
#     "Song Name":"Numb",
#     "Genre":"Alternative Rock",
#     "Release Year":"2003"
# },
# {
#     "Artist":"Armin van Buuren",
#     "Song Name":"Blah Blah Blah", 
#     "Genre":"Electronic Dance",
#     "Release Year":"2010"
# },
# {
#     "Artist":"Radiohead",
#     "Song Name":"15 Step",
#     "Genre":"Art Rock",
#     "Release Year":"2007"
# }]

# print(fav_songs[1])

# fav_songs.append({
#     "Artist":"Radiohead",
#     "Song Name":"15 Step",   #Add a new song
#     "Genre":"Art Rock",
#     "Release Year":"2007"
# })

# print(fav_songs)

# # del (fav_songs[1]) - Ways to delete #1
# # fav_songs.pop(2) - Ways to delete #2

# print (fav_songs)