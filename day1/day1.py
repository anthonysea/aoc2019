#!/usr/bin python

total_fuel_required = 0

with open('day1input.txt', 'r') as f:
    for mass in f.readlines():
        fuel_required = (int(mass) // 3) - 2
        total_fuel_required += fuel_required

print(total_fuel_required)