from datetime import datetime
from functools import wraps


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
                print(f"Spell failed, retrying... (Attempt {attempts}/{max_attempts})")
            return f"Spell failed after {max_attempts} attempts"
        return wrapper
    return decorator

#• Name is valid if it’s at least 3 characters and contains only letters/spaces
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)
    # apenas quero testar o power validator, então não vou usar o validate_mage_name, sem nenhuma outra função, só o power_validator, nem criar outra função, só usar o power_validator diretamente no cast_spell
    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def cast():
            return f"{spell_name} cast with power {power}"
        return cast()

# testar a classe
if __name__ == "__main__":
    guild = MageGuild()
    print(guild.cast_spell("Fireball", 5))  # Should fail validation
    print(guild.cast_spell("Ice Shard", 15))  # Should succeed
    