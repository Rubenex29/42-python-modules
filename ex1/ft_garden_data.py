class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_value = age

    def show(self) -> None:
        print(self.name, ":", self.height, "cm,", self.age_value, "days old")


def main() -> None:
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()


print("=== Garden Plant Registry ===")
main()
print("=== End of Program ===")
