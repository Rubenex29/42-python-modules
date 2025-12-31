def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if not plant_name:
            raise ValueError(" Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too hight (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        return f"Plant '{plant_name}' is healthy!\n"
    except ValueError as e:
        print(f"Error: {e}\n")

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    status = check_plant_health("tomato", 7, 8)
    if (status):
        print(status)
    print("Testing empty plant name...")
    check_plant_health("", 7, 8)
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 8)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 7, 0)
    print("All error raising tests completed!")
test_plant_checks()
