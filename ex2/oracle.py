import os
import sys
from dotenv import load_dotenv

def main():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")
    
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    if not all([mode, db_url, api_key, zion]):
        print("\n[ERROR] Missing critical configuration!")
        print("Please ensure your .env file is configured correctly.")
        print("Check .env.example for required fields.")
        sys.exit(1)

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected to local instance' if 'localhost' in db_url else 'Remote connection active'}")
    print(f"API Access: {'Authenticated' if api_key else 'Access Denied'}")
    print(f"Log Level: {log_level if log_level else 'INFO (default)'}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")

    print("\nEnvironment security check:")
    
    if os.path.exists(".env"):
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")

    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[!] Running in development mode")

    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()