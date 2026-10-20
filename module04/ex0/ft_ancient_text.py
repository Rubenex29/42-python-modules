def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    file = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    content = file.read()
    print(content)
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


main()
