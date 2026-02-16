def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)

    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list) -> callable:
    def sequence_spell(*args, **kwargs):
        results = []
        for spell in spells:
            result = spell(*args, **kwargs)
            results.append(result)
        return results
    return sequence_spell


if __name__ == "__main__":
    # Example spells
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    # Test spell_combiner
    combined_spell = spell_combiner(fireball, heal)
    print("Testing spell combiner...")
    print("Combined spell result:", combined_spell("Dragon"))
    print()

    # Test power_amplifier
    def base_spell():
        return 10

    amplified_spell = power_amplifier(base_spell, 3)
    print("Testing power amplifier...")
    print("Original: 10, Amplified:", amplified_spell())
    print()

    # Test conditional_caster
    def condition(target):
        if target:
            return True
        return False

    conditional_spell = conditional_caster(condition, fireball)
    print("Testing conditional caster...")
    print("Conditional spell result:", conditional_spell("Dragon"))
    print("Conditional spell result:", conditional_spell("Goblin"))
    print()

    # Test spell_sequence
    sequence = spell_sequence([fireball, heal])
    print("Testing spell sequence...")
    print("Sequence spell result:", sequence("Dragon"))
