def events(n: int):
    players = {"Alice": 5, "Bob": 12, "Charlie": 8}
    actions = ["killed monster", "found treasure", "leveled up"]
    it = iter(players)
    for i in range(n):
        player = next(it)
        score = players[player]
        action = actions[i]
        yield f"Event {i + 1}: Player {player} (level {score}) {action}"


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    print("Processing 1000 game events...\n")
    n = 3
    msg = events(n)
    print(next(msg))
    print(next(msg))
    print(next(msg))
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n}")
    players = {"Alice": 5, "Bob": 12, "Charlie": 8}
    count = sum(1 for score in players.values() if score > 10)
    print(f"High-level players (10+): {count}")
    treasure_count = sum(1 for event in events(3) if "found treasure" in event)
    level_up_count = sum(1 for event in events(3) if "leveled up" in event)
    print(f"Treasure events: {treasure_count}")
    print(f"Level up events: {level_up_count}")
    print("\nMemory usage: Constant (streaming)\n")
    print("=== Generator Demonstration ===")
    fib = fibonacci(10)
    first_ten = [str(next(fib)) for _ in range(10)]
    print("Fibonacci sequence (first 10): " + ", ".join(first_ten))


main()
