import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("\nInput Stream active. Enter archivist ID: ")

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status = sys.stdin.readline()
    status = status[:-1]

    sys.stdout.write(
        f"\n{{[}}STANDARD{{]}} Archive status from {archivist_id}: {status}\n"
    )

    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("{[}STANDART{]} Data transmission complete\n")
    print("\nThree-channel communication test successful.")


main()
