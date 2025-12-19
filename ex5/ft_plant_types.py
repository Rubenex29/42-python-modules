class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm" +
              f", {self.age}days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm" +
              f", {self.age}days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        shade = 31.2 * self.height * self.trunk_diameter
        print(f"{self.name} provides {shade} sqaure metersof shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f"{self.harvest_season} harvest")

    def nutrition(self) -> None:
        if self.nutritional_value == 45:
            print(f"{self.name} is rich in vitamin C")
        elif self.nutritional_value == 60:
            print(f"{self.name} is rich in vitamin A")
        elif self.nutritional_value == 80:
            print(f"{self.name} is rich in iron")
        else:
            print(f"{self.name} provides general nutrients")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.show()
    flower1.bloom()
    print("")
    flower2 = Flower("Lily", 35, 15, "white")
    flower2.show()
    flower2.bloom()
    print("\n----------------------------------------\n")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.show()
    tree1.produce_shade()
    print("")
    tree2 = Tree("Pine", 300, 1200, 40)
    tree2.show()
    tree2.produce_shade()
    print("\n----------------------------------------\n")
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", 45)
    vegetable1.show()
    vegetable1.nutrition()
    print("")
    vegetable2 = Vegetable("Carrot", 30, 120, "autumn", 80)
    vegetable2.show()
    vegetable2.nutrition()


ft_plant_types()
