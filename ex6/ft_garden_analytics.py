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
        return "(blooming)"

    def show(self) -> None:
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers {self.bloom()}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def show(self) -> None:
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers {self.bloom()}, "
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

    @staticmethod
    def validate_heights(plants_list) -> bool:
        for plant in plants_list:
            if plant.height < 0:
                return False
        return True

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"{self.name} is helping all plants grow...")
        for p in self.plants:
            growth_amount = 1
            p.grow(growth_amount)
            self.total_growth += growth_amount

    def calculate_score(self) -> int:
        total = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                total += plant.prize_points
            total += plant.height + plant.age
        return total

    @classmethod
    def create_garden_network(cls, gardens_list):
        """Exibe o sumário de todos os jardins geridos."""
        print("Garden Scores - ", end="")
        score_strings = [f"{g.name}: {g.calculate_score()}"
                         for g in gardens_list]
        print(", ".join(score_strings))

    def print_report(self):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            p.show()
        status = GardenManager.GardenStats(self.plants)
        reg, flow, prz = status.calculate_plant_types()
        print(f"\nPlants added: {reg + flow + prz}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prz} prize flowers\n")
        is_valid = GardenManager.validate_heights(self.plants)
        print(f"Height validation test: {is_valid}")

    @classmethod
    def get_total_gardens(cls):
        print(f"Total gardens managed: {cls.total_gardens}")


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    oak = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 15, "red")
    sunf = PrizeFlower("Sunflower", 50, 20, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunf)
    print("")
    alice_garden.grow_all()
    alice_garden.print_report()
    bob_garden = GardenManager("Bob")
    gardens_list = [alice_garden, bob_garden]
    GardenManager.create_garden_network(gardens_list)
    GardenManager.get_total_gardens()

main()
