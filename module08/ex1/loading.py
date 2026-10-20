import sys


def check_environment():
    # Environment detection:
    # If `sys.prefix` equals `sys.base_prefix`, no venv is active.
    # A venv changes `sys.prefix` to point at the environment root.
    if sys.prefix == sys.base_prefix:
        print("LOADING STATUS: Failure")
        print("Checking dependencies:")
        print("[ERROR] You are in the global environment!")
        print("\nTo load the programs correctly, follow these steps:")
        print("1. Create environment: poetry install")
        print("2. Enter the Matrix: poetry run python loading.py")
        sys.exit(1)
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    # Heuristic: Poetry-created venvs commonly include these path segments.
    if "pypoetry" in sys.prefix or "virtualenvs" in sys.prefix:
        print("ENVIRONMENT: [Poetry] - Advanced dependency management active")
    else:
        print("ENVIRONMENT: [pip/venv] - Standard dependency loading active")
    print(f"PATH: {sys.prefix}\n")


check_environment()

dependencies_ok = True

# --- pandas ---
try:
    import pandas as pd
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
except ImportError:
    print("[MISSING] pandas - Install with: pip install pandas")
    dependencies_ok = False

# --- numpy ---
try:
    import numpy as np
    print(f"[OK] numpy ({np.__version__}) - Numerical computations ready")
except ImportError:
    print("[MISSING] numpy - Install with: pip install numpy")
    dependencies_ok = False

# --- matplotlib ---
try:
    import matplotlib
    import matplotlib.pyplot as plt
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ImportError:
    print("[MISSING] matplotlib - Install with: pip install matplotlib")
    dependencies_ok = False

if not dependencies_ok:
    print("\nPlease install missing dependencies before running analysis.")
    sys.exit(1)

print("\nAnalyzing Matrix data...")

data = np.random.randint(0, 100, 1000)
print(f"Processing {len(data)} data points...")
df = pd.DataFrame({
    "Energy": data
})
print("Generating visualization...\n")
plt.hist(df["Energy"], bins=20)
plt.title("Matrix Energy Distribution")
plt.xlabel("Energy Level")
plt.ylabel("Frequency")

plt.savefig("matrix_analysis.png")
print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
