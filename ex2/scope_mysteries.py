def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power
    def accumulator(spell_power):
        nonlocal power
        power += spell_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def item(item_name):
        return f"{enchantment_type} {item_name}"
    return item


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    # Test mage_counter
    counter = mage_counter()
    print("Testing mage counter...")
    for _ in range(5):
        print("Counter:", counter())
    print()

    # Test spell_accumulator
    accumulator = spell_accumulator(10)
    print("Testing spell accumulator...")
    print("Initial power: 10")
    print("After adding 5:", accumulator(5))
    print("After adding 3:", accumulator(3))
    print()

    # Test enchantment_factory
    enchantment = enchantment_factory("Flaming")
    print("Testing enchantment factory...")
    print(enchantment("Sword"))
    print(enchantment("Shield"))
    print()

    # Test memory_vault
    vault = memory_vault()
    print("Testing memory vault...")
    vault["store"]("favorite_spell", "Invisibility")
    vault["store"]("weakness", "Fire")
    print("Recall favorite_spell:", vault["recall"]("favorite_spell"))
    print("Recall weakness:", vault["recall"]("weakness"))
    print("Recall non_existent_key:", vault["recall"]("non_existent_key"))