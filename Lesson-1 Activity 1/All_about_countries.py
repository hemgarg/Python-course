class India():
    def capital(self):
        print("New delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington, Dc. is the capital of USA")
    def language(self):
        print("English is the most widely spoken language of the USA")
    def type(self):
        print("USA is a developed country")

obj_ind = India()
obj_USA = USA()

for country in (obj_ind, obj_USA):
    country.capital()
    country.language()
    country.type()