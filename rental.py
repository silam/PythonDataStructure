from car import Car, ElectricCar

gas_fleet = []
electric_fleet = []


for _ in range(500):
    car = Car('ford', 'focus', 2016)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElectricCar('nissan', 'leaf', 2016)
    electric_fleet.append(ecar)

print("Gas Car: " +  str(len(gas_fleet)))
print("Electric Car: " + str(len(electric_fleet)))