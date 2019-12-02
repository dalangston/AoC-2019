# Calculate rocket fuel requirements

def fuelRequired(mass):
  return (mass//3) - 2

inputs = "p1-inputs"
totalFuel = 0

with open(inputs, "r") as rockets:
  for mass in rockets:
    totalFuel += fuelRequired(int(mass))

print(f"Total Fuel Required: {totalFuel}")
