import math


def main():
    print("=== Game Coordinate System ===\n")
    d0 = (0, 0, 0)
    d1 = (10, 20, 5)
    print(f"Position created: {d1}")
    squared_diff = (d1[0] - d0[0])**2 + (d1[1] - d0[1])**2 + (d1[2] - d0[2])**2
    distance = math.sqrt(squared_diff)
    print(f"Distance between {d0} and {d1}: {distance:.2f}\n")
    s = "3,4,0"
    s1 = s.split(",")
    x = int(s1[0])
    y = int(s1[1])
    z = int(s1[2])
    d1 = (x, y, z)
    print(f'Parsing coordinates: "{s}"')
    print(f"Parsed position: {d1}")
    squared_diff = (d1[0] - d0[0])**2 + (d1[1] - d0[1])**2 + (d1[2] - d0[2])**2
    distance = math.sqrt(squared_diff)
    print(f"Distance between {d0} and {d1}: {distance:.1f}\n")
    invalid = ("abc,def,gh")
    print(f'Parsing invalid coordenates: "{invalid}"')
    try:
        s = invalid.split(",")
        x = int(s[0])
        y = int(s[1])
        z = int(s[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e} ")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
