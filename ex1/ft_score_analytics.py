import sys


def check():
    if (len(sys.argv) < 2):
        print("No scores provided. Usage: " +
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return False, []
    numbers = []
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            numbers.append(num)
        except ValueError as e:
            print(f"Value Error: {e}")
            return False, []
    return True, numbers


def main():
    print("=== Player Score Analytics ===")
    ok, numbers = check()
    if (ok):
        print(f"Scores processed: {numbers}")
        print(f"Total players {len(sys.argv[1:])}")
        print(f"Total score: {sum(numbers)}")
        print(f"Average score: {sum(numbers) / len(numbers)}")
        print(f"High score: {max(numbers)}")
        print(f"Low score: {min(numbers)}")
        print(f"Score range: {max(numbers) - min(numbers)}")


main()
