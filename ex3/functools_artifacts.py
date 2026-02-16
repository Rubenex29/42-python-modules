from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    result = reduce(operations[operation], spells)
    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    ice_enchant = partial(base_enchantment, power=50, element="ice")
    lightning_enchant = partial(base_enchantment, power=50, element="lightning")

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant,
    }

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        print("ola")
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:


if __name__ == "__main__":
    # Test spell_reducer
    a = [1, 2, 3, 4]
    print(spell_reducer(a, "add"))  # Should print 10
    print(spell_reducer(a, "multiply"))  # Should print 24
    print(spell_reducer(a, "max"))  # Should print 4
    print(spell_reducer(a, "min"))  # Should print 1
    print()

    # Test partial_enchanter
    def base_enchantment(element, power, target):
        return f"Enchants {target} with {power} power of {element}"
    enchanter = partial_enchanter(base_enchantment)
    print(enchanter["fire_enchant"](target="Sword"))
    print(enchanter["ice_enchant"](target="Shield"))
    print(enchanter["lightning_enchant"](target="Armor"))

    # Test memoized_fibonacci
    print(memoized_fibonacci(10))
    print(memoized_fibonacci(10))
