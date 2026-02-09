from abc import ABC, abstractmethod
from typing import Any


class Strategy(ABC):
    @abstractmethod
    def execute_turn(
        self,
        hand: list[dict[str, Any]],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(
        self,
        available_targets: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        pass
