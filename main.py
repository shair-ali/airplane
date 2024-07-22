# Airplane System Program

class Airplane:
    def __init__(self, name, capacity, fuel_capacity):
        self.name = name
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.passengers = []
        self.fuel_level = 0

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger} added to flight.")
        else:
            print("Flight is full. Cannot add passenger.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Passenger {passenger} removed from flight.")
        else:
            print("Passenger not found on flight.")

    def refuel(self, amount):
        if self.fuel_level + amount <= self.fuel_capacity:
            self.fuel_level += amount
            print(f"Refueled {amount} gallons. Current fuel level: {self.fuel_level} gallons.")
        else:
            print("Cannot refuel beyond fuel capacity.")

    def fly(self, distance):
        if self.fuel_level >= distance:
            self.fuel_level -= distance
            print(f"Flew {distance} miles. Current fuel level: {self.fuel_level} gallons.")
        else:
            print("Not enough fuel to fly.")

class Passenger:
    def __init__(self, name, seat_number):
        self.name = name
        self.seat_number = seat_number

# Create an airplane
airplane = Airplane("Boeing 737", 200, 10000)

# Create passengers
passenger1 = Passenger("theif", "A1")
passenger2 = Passenger("smuggler", "B2")
passenger3 = Passenger("police", "C3")

# Add passengers to flight
airplane.add_passenger(passenger1.name)
airplane.add_passenger(passenger2.name)
airplane.add_passenger(passenger3.name)

# Refuel airplane
airplane.refuel(5000)

# Fly airplane
airplane.fly(2000)

# Remove passenger
airplane.remove_passenger(passenger2.name)

# Print passenger list
print("Passengers on flight:")
for passenger in airplane.passengers:
    print(passenger)
