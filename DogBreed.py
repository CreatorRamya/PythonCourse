class Dog:
    species = "Canis lupus familiaris"
    
    def __init__(self, name, breed):
    
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 30)

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

print("Dog 1 Details:")
dog1.display_info()

print("Dog 2 Details:")
dog2.display_info()
