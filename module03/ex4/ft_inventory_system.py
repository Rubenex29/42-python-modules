def main():
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")

    alice = dict()
    alice["sword"] = {
        "quantity": 1, "type": "weapon",
        "rarity": "rare", "value": 500
    }
    alice["potion"] = {
        "quantity": 5, "type": "consumable",
        "rarity": "common", "value": 50
    }
    alice["shield"] = {
        "quantity": 1, "type": "armor",
        "rarity": "uncommon", "value": 200
    }

    total = 0
    quantity = 0

    for name, item in alice.items():
        print(
            f"{name} ({item['type']}, {item['rarity']}): "
            f"{item['quantity']}x @ {item['value']} gold each = "
            f"{item['quantity'] * item['value']} gold"
        )
        total += item["quantity"] * item["value"]
        quantity += item["quantity"]

    print(f"\nInventory value: {total} gold")
    print(f"Item count {quantity} items")

    print(
        f"Categories: weapon({alice['sword']['quantity']}), "
        f"consumable({alice['potion']['quantity']}), "
        f"armor({alice['shield']['quantity']})\n"
    )

    print("=== Transaction: Alice gives Bob 2 potions ===")

    bob = dict()
    alice["potion"]["quantity"] = 3

    if "potion" in bob:
        bob["potion"]["quantity"] += 2
    else:
        bob["potion"] = {
            "quantity": 2, "type": "consumable",
            "rarity": "common", "value": 50
        }

    print("Transaction successful!")
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {bob['potion']['quantity']}")

    print("\n=== Inventory Analytics ===")

    total_al = sum(
        item["quantity"] * item["value"]
        for item in alice.values()
    )
    total_bob = sum(
        item["quantity"] * item["value"]
        for item in bob.values()
    )

    if total_al > total_bob:
        print(f"Most valuable player: Alice ({total_al} gold)")
    elif total_bob > total_al:
        print(f"Most valuable player: Bob ({total_bob} gold)")
    else:
        print("Alice and Bob have the same gold amount")

    al_i = len(alice)
    bob_i = len(bob)

    print("Most items: ", end="")
    if al_i > bob_i:
        print(f"Alice ({al_i} items)")
    elif bob_i > al_i:
        print(f"Bob ({bob_i} items)")
    else:
        print(
            f"Alice and Bob have the same number of items ({al_i})"
        )

    rarity_order = {
        "common": 1,
        "uncommon": 2,
        "rare": 3,
        "epic": 4,
        "legendary": 5,
    }

    max_rarity_value_alice = max(
        rarity_order[item["rarity"]]
        for item in alice.values()
    )
    rare_items_alice = [
        name
        for name, item in alice.items()
        if rarity_order[item["rarity"]] == max_rarity_value_alice
    ]

    max_rarity_value_bob = max(
        rarity_order[item["rarity"]]
        for item in bob.values()
    )
    rare_items_bob = [
        name
        for name, item in bob.items()
        if rarity_order[item["rarity"]] == max_rarity_value_bob
    ]

    print(
        f"Rarest items: "
        f"{', '.join(rare_items_alice)}, "
        f"{', '.join(rare_items_bob)}"
    )


main()
