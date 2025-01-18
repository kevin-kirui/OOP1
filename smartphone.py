# Assignment 1: Class Design

class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
    
    def charge(self, amount):
        self.battery_percentage = min(100, self.battery_percentage + amount)
        print(f"{self.brand} {self.model} charged to {self.battery_percentage}%")
    
    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_percentage, cooling_system):
        super().__init__(brand, model, battery_percentage)
        self.cooling_system = cooling_system
    
    def game_mode(self):
        print(f"{self.brand} {self.model} is now in gaming mode with {self.cooling_system} cooling.")


# Activity 2: Polymorphism

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Testing the classes
phone = Smartphone("Samsung", "Galaxy S21", 50)
phone.charge(30)
phone.call("+123456789")

gaming_phone = GamingPhone("Asus", "ROG Phone 5", 40, "Liquid Cooling")
gaming_phone.game_mode()

vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
