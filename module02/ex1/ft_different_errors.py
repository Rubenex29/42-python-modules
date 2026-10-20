def garden_operations():
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)
    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print("\nTesting KeyError...")
    dictionary_capitals = {"Lisbon": "Portugal", "Madrid": "Spain"}
    try:
        dictionary_capitals['missing\_plant']
    except KeyError as e:
        print("Caught KeyError:", e)


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


test_error_types()
