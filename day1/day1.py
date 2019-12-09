#!/usr/bin python

total_fuel_required = 0
fuel_array = []

with open('day1input.txt', 'r') as f:
    for mass in f.readlines():
        fuel = (int(mass) // 3) - 2
        while fuel > 0:
            fuel_array.append(fuel)
            fuel = fuel // 3 - 2
        total_fuel_required += sum(fuel_array)
        fuel_array.clear()

print(fuel_array)
print(total_fuel_required)