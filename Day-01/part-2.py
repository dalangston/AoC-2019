def fuelRequired(mass):
  fuelMass = (mass//3) - 2
  if fuelMass <= 0:
    return 0

  return fuelMass + fuelRequired(fuelMass)

inputs = "p1-inputs"
totalFuel = 0

with open(inputs, "r") as rockets:
  for mass in rockets:
    totalFuel += fuelRequired(int(mass))

print(f"Total Fuel Required: {totalFuel}")
