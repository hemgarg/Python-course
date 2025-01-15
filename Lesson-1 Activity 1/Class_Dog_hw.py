class Dog:
    def __init__(self,breed,colour):
        self.breed = breed
        self.colour = colour

Coco = Dog("German Shepard","White")
Archie = Dog("Golden Retriever","Light Golden")

print("Coco's breed - {} Coco's colour - {}".format(Coco.breed, Coco.colour), "\n")
print("Archies breed - {} Archies colour - {}".format(Archie.breed , Archie.colour))