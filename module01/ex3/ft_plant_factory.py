class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount=1):
        self.height += amount

    def age_by(self, day_count=1):
        self.age += day_count


class Factory:
    def __init__(self):
        self.plant_created = 0

    def create_plant(self, name, age, height) -> Plant:
        plant = Plant(name, age, height)
        plant.grow(height)
        plant.age_by(age)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        self.plant_created += 1
        return (plant)

    def total_plants(self) -> int:
        return (self.plant_created)


def plant_factory():
    factory = Factory()
    print("=== Plant Factory Output ===")
    factory.create_plant("Rose", 30, 25)
    factory.create_plant("Oak", 365, 200)
    factory.create_plant("Cactus", 90, 5)
    factory.create_plant("Sunflower", 80, 80)
    factory.create_plant("Fern", 120, 15)
    print(f"\nTotal plants created: {factory.total_plants()}")


plant_factory()
