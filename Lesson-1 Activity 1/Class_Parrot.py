class Parrot:

    species = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

Blu = Parrot("Blu",10)
Woo = Parrot("Woo", 15)

print("The Blu speices is  {}".format(Blu.species))

print("The Woo speicies is {} and age is {}".format(Woo.species, Woo.age))