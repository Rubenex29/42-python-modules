import sys


def main():
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    name = sys.stdin.readline()
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()

    name1 = sys.stdin.readline()
    
main()
