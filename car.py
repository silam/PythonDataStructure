

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_capacity = 15
        self.fuel_level = 0
        
    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
    
    def drive(self):
        print('The car is moving.')
    
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")
            
    def add_fuel(self, amount):
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Fuel added!")
        else:
            print('The tank will not hold that much')

class Battery():
    def __init__(self, size=70):
        self.size = size
        self.charge_level = 0
        
    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270
            
class ElectricCar(Car):
    def __init__(self, make, model, year):
        Car.__init__(self, make, model, year)
        
        self.battery_size = 70
        self.charge_level = 0
        self.battery = Battery()
        
    def charge(self):
        self.charge_level = 100
        print("Vehicle is fully charged")
        
    def fill_tank(self):
        print("This car has no fuel tank!")


        
        