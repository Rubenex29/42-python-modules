def list_comprehension(players):
    more_2000 = [
        name
        for name, info in players.items()
        if info["score"] > 2000
    ]
    print(f"High scorers (>2000): {more_2000}")

    scores = [info["score"] for info in players.values()]
    doubled = [
        s
        for s in set(scores)
        if scores.count(s) > 1
    ]
    print(f"Scores doubled: {doubled}")

    active = [
        name
        for name, info in players.items()
        if info["active"]
    ]
    print(f"Active players: {active}")


def dict_comprehension(players):
    players_scores = {
        name: info["score"]
        for name, info in players.items()
    }
    print(f"Player scores: {players_scores}")

    category_count = {
        "high": 0,
        "medium": 0,
        "low": 0
    }
    for info in players.values():
        cat = info["category"]
        category_count[cat] += 1

    print(f"Score categories: {category_count}")

    achievments = {
        name: len(info["achievments"])
        for name, info in players.items()
    }
    print(f"Achievement counts: {achievments}")


def set_comprehension(players):
    players2 = [
        "alice",
        "bob",
        "charlie",
        "diana",
        "alice",
        "bob",
        "alice"
    ]
    unique_players = {name for name in players2}
    print(f"Unique players: {unique_players}")

    unique_achievments = {
        ach
        for info in players.values()
        for ach in info["achievments"]
    }
    print(f"Unique achievments: {unique_achievments}")

    unique_regions = {
        info["region"]
        for info in players.values()
    }
    print(f"Active regions: {unique_regions}")


def combined(players):
    print(f"Total players: {len(players)}")

    unique_achievments = {
        ach
        for info in players.values()
        for ach in info["achievments"]
    }
    print(
        f"Total unique achievements: "
        f"{len(unique_achievments)}"
    )

    total = 0
    for item in players.values():
        total += item["score"]

    print(f"Average score {total / len(players)}")


def main():
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    players = {
        "alice": {
            "score": 2300,
            "category": "high",
            "achievments": [
                "first_kill",
                "level_10",
                "boss_slayer"
            ],
            "active": True,
            "region": "north"
        },
        "bob": {
            "score": 1800,
            "category": "low",
            "achievments": [
                "first_kill",
                "level_5"
            ],
            "active": True,
            "region": "east"
        },
        "charlie": {
            "score": 2150,
            "category": "medium",
            "achievments": [
                "level_10",
                "boss_slayer"
            ],
            "active": True,
            "region": "central"
        },
        "diana": {
            "score": 2150,
            "category": "medium",
            "achievments": [
                "level_10",
                "boss_slayer"
            ],
            "active": False,
            "region": "north"
        }
    }

    list_comprehension(players)

    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players)

    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)

    print("\n=== Combined Analysis ===")
    combined(players)


main()
