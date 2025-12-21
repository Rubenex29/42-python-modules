class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount=1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def show(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return ("(blooming)")

    def show(self) -> None:
        print(f"- {self.name}: {self.height}cm, " +
              f"{self.color} flowers {self.bloom()}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height_cm, age, color, prize_points):
        super().__init__(name, height_cm, age, color)
        self.prize_points = prize_points

    def show(self) -> None:
        print(f"- {self.name}: {self.height}cm, " +
              f"{self.color} flowers {self.bloom()}, " +
              f"Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def calculate_plant_types(self):
            regular = sum(1 for p in self.plants if type(p) is Plant)
            flowering = sum(1 for p in self.plants
                            if type(p) is FloweringPlant)
            prize = sum(1 for p in self.plants if type(p) is PrizeFlower)
            return regular, flowering, prize

    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"{self.name} is helping all plants grow...")
        for p in self.plants:
            growth_amount = 1
            p.grow(growth_amount)
            self.total_growth += growth_amount

    def print_report(self):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            p.show()
        status = GardenManager.GardenStats(self.plants)
        regular, flowering, prize = status.calculate_plant_types()
        print(f"\nPlants added: {regular + flowering + prize}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers\n")

    def calculate_score(self) -> int:
        total = 0
        for plant in self.plants:
            if type(plant) is PrizeFlower:
                total += plant.prize_points
            total += plant.height + plant.age
        return (total)

    def validation_heights(self):
        for plant in self.plants:
            if plant.height < 0:
                return (False)
        return (True)

    def print_system_summary(self, gardens_list):
        score_strings = []
        for garden in gardens_list:
            text = f"{garden.name}: {garden.calculate_score()}"
            score_strings.append(text)
        print("Garden Scores - ", end = "")
        total = len(score_strings)
        i = 0
        for text in score_strings:
            i += 1
            print(f"{text}", end = "")
            if (i < total):
                print(", ", end = "")
        print("")

    @classmethod
    def get_total_gardens(cls):
        print(f"Total gardens managed: {cls.total_gardens}")


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    garden = GardenManager("Alice")
    oak = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 15, "red")
    sunf = PrizeFlower("Sunflower", 50, 20, "yellow", 10)
    garden.add_plant(oak)
    garden.add_plant(rose)
    garden.add_plant(sunf)
    print("")
    garden.grow_all()
    garden.print_report()
    Bob = GardenManager("Bob")
    gardens_list = [garden, Bob]
    garden.print_system_summary(gardens_list)
    garden.get_total_gardens()
main()