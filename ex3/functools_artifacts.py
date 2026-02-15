from functools import reduce
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


a = [1, 2, 3, 4]
print(spell_reducer(a, "add"))  # Should print 10
print(spell_reducer(a, "multiply"))  # Should print 24
print(spell_reducer(a, "max"))  # Should print 4
print(spell_reducer(a, "min"))  # Should print 1