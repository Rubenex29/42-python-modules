import sys
import os
import site


# Environment detection:
# In a virtual environment, `sys.prefix` points to the venv directory,
# while `sys.base_prefix` still points to the base (global) interpreter.
# If they are equal, no venv is active.
if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in\n")
    print("Current Python:", sys.executable)
    # No venv is active, so report that explicitly and provide setup steps.
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")
    print("Then run this program again.")
else:
    # A venv is active: `sys.prefix` points to the venv root.
    print("MATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    # Use the venv directory name for a friendly label.
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    # The first site-packages path is the default install target.
    packages = site.getsitepackages()
    print(packages[0])
