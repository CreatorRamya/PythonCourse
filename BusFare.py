class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_info(self):
        return f"Vehicle Name: {self.name}, Capacity: {self.capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, capacity, fare_per_passenger):
        super().__init__(name, capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self):
        return self.capacity * self.fare_per_passenger

    def get_info(self):
        base_info = super().get_info()
        total_fare = self.calculate_total_fare()
        return f"{base_info}, Fare per Passenger: ${self.fare_per_passenger}, Total Fare: ${total_fare}"


def main():
    my_bus = Bus("City Express", 50, 2.5)

    print(my_bus.get_info())


if __name__ == "__main__":
    main()
