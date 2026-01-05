def main():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {alice.union(bob, charlie)}")
    print(f"Total unique achievements: {len(alice.union(bob, charlie))}\n")
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    unique = (
        alice.difference(bob, charlie) |
        bob.difference(alice, charlie) |
        charlie.difference(alice, bob)
    )
    print(f"Rare achievements (1 player): {unique}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    alice_unique = alice - (alice & bob)
    bob_unique = bob - (alice & bob)
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


main()
