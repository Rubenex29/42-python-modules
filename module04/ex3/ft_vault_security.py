def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    with open("classified_data.txt", "r") as f:
        content = f.read()
    with open("security_protocols.txt", "r") as f1:
        content1 = f1.read()
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    print(content)
    print("\nSECURE PRESERVATION:")
    print(content1)
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


main()
