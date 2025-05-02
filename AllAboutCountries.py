class Congo():
    def capital(self):
        print("The capital of Congo is Kinshasa.")

    def places(self):
        print("Zongo is a waterfall place to visit in Congo, which is really pretty!")

    def language(self):
        print("French is the common and national language that everyone speak.")

class India():
    def capital(self):
        print("India's capital is New Delhi.")

    def places(self):
        print("Mysore is a beautiful palace to visit in India.")

    def language(self):
        print("Hindi is the national language of India and also mostly spoken.")

obj_cong = Congo()
obj_ind = India()

for country in (obj_cong, obj_ind):
    country.capital()
    country.language()
    country.places()
    