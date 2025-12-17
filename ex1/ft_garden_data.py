class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_value = age
        print(self.name, ":", self.height, "cm,", self.age_value, "days old")
print("=== Garden Plant Registry ===")
Plant("Rose", 25, 30)
Plant("Sunflower", 80, 45)
Plant("Cactus", 15, 120)
