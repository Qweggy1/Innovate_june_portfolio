from character import Character

spiderman=Character("Peter Parker","Spiderman")

print(f"{spiderman.name} is actually the superhero {spiderman.superhero_name}")

spiderman.set_power("Spidey Senses")
spiderman.get_power()