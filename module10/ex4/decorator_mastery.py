from datetime import datetime
from functools import wraps
import random


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Spell completed in {end_time - start_time} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", 0)
            if power < min_power:
                return f"Spell failed: Power must be at least {min_power}"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    if result != "Spell fizzled":
                        return result
                except Exception:
                    pass
                attempts += 1
                print(f"Spell failed, retrying... "
                      f"(Attempt {attempts}/{max_attempts})")
            return f"Spell failed after {max_attempts} attempts"
        return wrapper
    return decorator


# Name is valid if it’s at least 3 characters and contains only letters/spaces
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @spell_timer
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


# testing everything together
if __name__ == "__main__":
    guild = MageGuild()
    print(guild.cast_spell("Fireball", 5))  # Should fail validation
    print()
    print(guild.cast_spell("Ice Shard", 15))  # Should succeed
    print()
    print(MageGuild.validate_mage_name("Gandalf"))  # Should return True
    print(MageGuild.validate_mage_name("Al"))  # Should return False
    # Testing retry_spell with a function that randomly fails
    print("\nTesting retry_spell decorator...")

    @retry_spell(3)
    def unstable_spell():
        if random.random() < 0.5:
            return "Spell fizzled"
        return "Spell succeeded"

    print(unstable_spell())
