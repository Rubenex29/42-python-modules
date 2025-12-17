class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_value = age

    def grow(self):
        if self.age_value < 30:
            self.height += 2
        elif self.age_value < 100:
            self.height += 1

    def age(self):
        self.age_value += 1

    def next_day(self):
        self.grow()
        self.age()

    def get_info(self):
        print(self.name, ":", self.height, "cm,", self.age_value, "days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Start ===")
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 1 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 2 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 3 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 4 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 5 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 6 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()

print("=== Day 7 ===")
rose.next_day()
sunflower.next_day()
cactus.next_day()
rose.get_info()
sunflower.get_info()
cactus.get_info()