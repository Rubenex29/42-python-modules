def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    a = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return a


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda x: f"* {x} *", spells)))


def mage_stats(mages: list[dict]) -> dict:
    stats = {}
    most = max(mages, key=lambda x: x["power"])["power"]
    less = min(mages, key=lambda x: x["power"])["power"]
    avg = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
    stats.update({"max_power": most, "min_power": less, "avg_power": avg})
    return stats


if __name__ == "__main__":
    artifacts = [
        {"name": " Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92},
    ]
    mages = [
        {"name": "Gandalf", "power": 100},
        {"name": "Merlin", "power": 80},
        {"name": "Morgana", "power": 60},
    ]
    spells = ["Fireball", "Heal", "shield"]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting power_filter...")
    print(power_filter(mages, 80))
    print("\nTesting mage_stats...")
    print(mage_stats(mages))
