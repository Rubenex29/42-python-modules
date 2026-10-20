class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class HealthError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 10

    def add_plant(self, name):
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 5, "sun": 8}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plant(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")
                self.plants[plant]["water"] += 1
                self.water_tank -= 1
                print(f"watering {plant} success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self):
        try:
            for plant in self.plants:
                if self.plants[plant]["water"] > 10:
                    raise HealthError("Water level" +
                                    f" {self.plants[plant]["water"]} is too high (max 10)")
                elif self.plants[plant]["water"] < 1:
                    raise HealthError("Water level" +
                                    f" {self.plants[plant]["water"]} is too low (min 1)")
                elif self.plants[plant]["sun"] < 2:
                    raise HealthError("Sunlight hours" +
                                    f" {self.plants[plant]["sun"]} is too low (min 2)") 
                elif self.plants[plant]["sun"] > 12:
                    raise HealthError("Sunlight hours" +
                                    f" {self.plants[plant]["sun"]} is too high (max 12)")
                print(f"{plant}: healthy (water: {self.plants[plant]["water"]}" +
                      f", sun: {self.plants[plant]["sun"]})")
        except HealthError as e:
            print(f"Error checking {plant}: {e}")


def main():
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant("")
    print("\nWatering plants...")
    garden.water_plant()
    print("\nChecking plant health...")
    garden.check_health()
    print("\nTesting error recovery...")
    garden.water_tank = 0
    garden.water_plant()
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")

main()