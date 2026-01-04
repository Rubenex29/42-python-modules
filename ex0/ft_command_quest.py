import sys


def main():
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(len(sys.argv) - 1):
            print(f"Argument {i + 1}: {sys.argv[i + 1]}")
    print(f"Total arguments: {len(sys.argv)}")


main()
