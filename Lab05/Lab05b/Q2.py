#Q2
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."
#Q2.1
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
    
if __name__ == '__main__':
    vehicle = Vehicle("School Volvo", 180, 12)
    print(f"Vehicle Name: {vehicle.name} Speed: {vehicle.max_speed} Mileage: {vehicle.mileage} ")
#Q2.2 Class Inheritance
    bus = Bus("School Bus", 180, 12)
    print(bus.seating_capacity())
