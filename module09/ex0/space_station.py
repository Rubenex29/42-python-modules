import datetime
from pydantic import BaseModel, Field


"""
Available Field constraints in Pydantic 2:

- gt (greater than):
    Works with numeric types.
    The value must be strictly greater than the specified number.

- ge (greater than or equal):
    Works with numeric types.
    The value must be greater than or equal to the specified number.

- lt (less than):
    Works with numeric types.
    The value must be strictly less than the specified number.

- le (less than or equal):
    Works with numeric types.
    The value must be less than or equal to the specified number.

- min_length:
    Works with strings.
    Defines the minimum allowed length.

- max_length:
    Works with strings.
    Defines the maximum allowed length.

- pattern:
    Works with strings.
    Validates the value using a regular expression (regex).

- default_factory:
    Used with lists or dictionaries.
    Creates a new object for each instance (avoids shared mutable defaults).
"""


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime.datetime = Field(
        default_factory=datetime.datetime.now
    )
    is_operational: bool = Field(default=True)
    notes: str = Field(default="", max_length=200)


def main():
    station = SpaceStation(
        station_id="SS-01",
        name="Orbital Station Alpha",
        crew_size=5,
        power_level=85.5,
        oxygen_level=90.0,
        notes="All systems nominal."
    )
    print("Valid station created:")
    print("========================================")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    print(f"Status: {station.notes}")
    print("\n\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="SS-01",
            name="Orbital Station Alpha",
            crew_size=25,
            power_level=85.5,
            oxygen_level=90.0,
            notes="All systems nominal."
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
