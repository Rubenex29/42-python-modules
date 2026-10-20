def events(n: int, players):
    actions = ["killed monster", "found treasure", "leveled up"]
    player_names = []
    for i in players.keys():
        player_names.append(i)
    for i in range(n):
        player = player_names[i % 3]
        score = players[player]
        action = actions[i % 3]
        yield f"Event {i + 1}: Player {player} (level {score}) {action}"


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def find_prime(n):
    num = 2
    count = 0
    while n > count:
        for i in range(2, num - 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def main():
    print("Processing 1000 game events...\n")
    n = 1000
    players = {"Alice": 5, "Bob": 12, "Charlie": 8}
    msg = events(n, players)

    # imprime os 3 primeiros eventos
    print(next(msg))
    print(next(msg))
    print(next(msg))
    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {n}")

    count = sum(1 for score in players.values() if score > 10)
    print(f"High-level players (10+): {count}")

    treasure_count = sum(1 for event in events(n, players)
                         if "found treasure" in event)
    level_up_count = sum(1 for event in events(n, players)
                         if "leveled up" in event)
    print(f"Treasure events: {treasure_count}")
    print(f"Level up events: {level_up_count}")

    print("\nMemory usage: Constant (streaming)\n")

    print("=== Generator Demonstration ===")
    fib = fibonacci(10)
    first_ten = [str(next(fib)) for _ in range(10)]
    print("Fibonacci sequence (first 10): " + ", ".join(first_ten))
    prime = find_prime(5)
    first_five = [str(next(prime)) for _ in range(5)]
    print("Prime numbers (first 5): " + ", ".join(first_five))


main()
