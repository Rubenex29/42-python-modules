import alchemy.elements as elements
import alchemy

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")

print("alchemy.elements.create_fire():", elements.create_fire())
print("alchemy.elements.create_water():", elements.create_water())
print("alchemy.elements.create_earth():", elements.create_earth())
print("alchemy.elements.create_air():", elements.create_air())

print("\nTesting package-level access (controlled by __init__.py):")

print("alchemy.create_fire():", alchemy.create_fire())
print("alchemy.create_water():", alchemy.create_water())

try:
    print("alchemy.create_earth():", alchemy.create_earth())
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    print("alchemy.create_air():", alchemy.create_air())
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
