def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    a = seed_type.capitalize()
    if unit == "packets":
        print(a, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(a, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(a, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
