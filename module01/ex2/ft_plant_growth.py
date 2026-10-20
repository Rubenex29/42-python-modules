class Plant:
    def __init__(self, name: str, height: int, age: int, g_speed: int) -> None:
        self.name = name
        self.height = height
        self.age_value = age
        self.start_height = height
        self.g_speed = g_speed

    def grow(self, amount) -> None:
        self.height += amount

    def age(self, day_count=1) -> None:
        self.age_value += day_count
        self.grow(day_count * self.g_speed)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_value} days old")

    def get_info(self) -> int:
        return (self.height - self.start_height)


def main() -> None:
    rose = Plant("Rose", 25, 30, 1)
    print("=== Day 1 ===")
    rose.show()
    print("=== Day 7 ===")
    rose.age(6)
    rose.show()
    print(f"Grown this week: +{rose.get_info()}cm")


main()
