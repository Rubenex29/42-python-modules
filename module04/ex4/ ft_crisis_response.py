def crisis_handler(file):
    try:
        with open(file, "r") as f:
            content = f.read()
        print(f"SUCCESS: Archive recovered - '{content}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archive.txt")
    print("STATUS: Crisis handled, system stable\n")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    crisis_handler("classified_vault.txt")
    print("STATUS: Crisis handled, security maintained\n")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")
    print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


main()
