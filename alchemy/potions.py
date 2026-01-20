from .elements import create_fire, create_water, create_earth, create_air

def healing_potion():
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing Potion brewed with {fire_result} and {water_result}"

def strength_potion():
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength Potion brewed with {earth_result} and {fire_result}"

def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"

def wisdom_potion():
    all_four_results = (
        create_fire(),
        create_water(),
        create_earth(),
        create_air()
    )
    return f"Wisdom potion brewed with {', '.join(all_four_results)}"
