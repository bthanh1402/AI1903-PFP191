#Q3
#Q3.1
class Vehicle: 

    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
if __name__ =='__main__':
    vehicle1 = Vehicle("School Volvo", 180, 12)
    print(f"{vehicle1.color} {vehicle1.name} Speed: {vehicle1.max_speed} Mileage: {vehicle1.mileage} ")

    vehicle2 = Vehicle("Audi Q5", 240, 18)
    print(f"{vehicle2.color} {vehicle2.name} Speed: {vehicle2.max_speed} Mileage: {vehicle2.mileage} ")
#Q3.2
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()  
        if isinstance(self, Bus): 
            total_fare += total_fare * 0.1  
        return total_fare

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
