from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class BMW(Car):
    def start_engine(self):
        print("BMW engine started with a soft purr.")

    def drive(self):
        print("BMW is driving smoothly with comfort mode.")

class Ferrari(Car):
    def start_engine(self):
        print("Ferrari engine roars to life with power.")

    def drive(self):
        print("Ferrari is zooming at high speed in sport mode!")

def test_drive(car):
    car.start_engine()
    car.drive()

my_bmw = BMW()
my_ferrari = Ferrari()

print("Test driving BMW:")
test_drive(my_bmw)

print("\nTest driving Ferrari:")
test_drive(my_ferrari)
