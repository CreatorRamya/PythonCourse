class Vehicle:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

model1X = Vehicle(250, 18)

print("Model max speed:" ,model1X.max_speed)
print("Model mileage:", model1X.mileage)