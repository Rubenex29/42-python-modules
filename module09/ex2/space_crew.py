from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import List
import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime.datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(
        min_length=1,
        max_length=12
    )
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        has_captain = any(
            member.rank == Rank.captain for member in self.crew
        )
        has_commander = any(
            member.rank == Rank.commander for member in self.crew
        )
        if not has_commander and not has_captain:
            raise ValueError(
                "Must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced_count = sum(
                1
                for member in self.crew
                if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main():
    mission_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 900,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 44,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 39,
                "specialization": "Navigation",
                "years_experience": 12,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 32,
                "specialization": "Engineering",
                "years_experience": 8,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 2500.0,
    }

    try:
        mission = SpaceMission(**mission_data)
    except Exception as error:
        print("Validation error:")
        print(error)
        return

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - " +
              f"{member.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission_data["crew"] = [
            {
                "member_id": "CM001",
                "name": "Bob",
                "rank": "lieutenant",
                "age": 30,
                "specialization": "Nav",
                "years_experience": 6,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "Ana",
                "rank": "officer",
                "age": 28,
                "specialization": "Eng",
                "years_experience": 5,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Leo",
                "rank": "cadet",
                "age": 22,
                "specialization": "Comms",
                "years_experience": 1,
                "is_active": True,
            },
        ]
        mission = SpaceMission(**mission_data)
    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
