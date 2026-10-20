def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")

def test_watering_system():
    plants = ["tomato", "lettuce", "carrots"]
    print("== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plants)
    print("Testing with error...")
    plants = ["tomato", ""]
    water_plants(plants)
    print("Cleanup always happens, even with errors!")
test_watering_system()