class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


print("=== Custom Garden Errors Demo ===\n")
print("Testing PlantError...")
try:
    age = 500
    if (age > 200):
        raise PlantError("The tomato plant is wilting!\n")
    print("Plant is fine")
except PlantError as e:
    print(f"Caught PlantError: {e}")
print("Testing WaterError...")
try:
    water = 500
    if (water < 700):
        raise WaterError("Not enough water in the tank!\n")
    print("Enought water")
except WaterError as e:
    print(f"Caught WaterError: {e}")
print("Testing catching all garden errors...")
try:
    age = 500
    if (age > 200):
        raise GardenError("The tomato plant is wilting!")
    print("Plant is fine")
except GardenError as e:
    print(f"Caught GardenError: {e}")
try:
    water = 500
    if (water < 700):
        raise WaterError("Not enough water in the tank!\n")
    print("Enought water")
except GardenError as e:
    print(f"Caught GardenError: {e}")
print("All custom error types work correctly!")