class SecurePlant:
    def __init__(self, name, height, age) -> None:
        print(f"Plant created: {name}")
        self.name = name
        self.height = 0
        self.set_height(height)
        self.age = 0
        self.set_age(age)

    def set_height(self, height) -> None:
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
        else:
            print(f"Height updated: {height}cm [OK]")
            self.height = height

    def set_age(self, age) -> None:
        if (age < 0):
            print(f"Invalid operation attempted: height {age}cm [REJECTED]")
        else:
            print(f"Height updated: {age}cm [OK]")
            self.age = age

    def get_height(self) -> int:
        return (self.height)

    def get_age(self) -> int:
        return (self.age)


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm" +
          f", {plant.get_age()} days)")


ft_garden_security()
