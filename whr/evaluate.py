import math
from typing import Union
import whr_core
from .base import Base


class Evaluate:
    def __init__(self, base: Base):
        self.core = whr_core.Evaluate(base.core)

    def get_rating(
        self, name: str, time_step: int, ignore_null_players: bool = True
    ) -> Union[float, None]:
        ret = self.core.get_rating(name, time_step, ignore_null_players)
        if not math.isfinite(ret):
            return None
        return ret

    def evaluate_ave_log_likelihood_games(
        self, games: list, ignore_null_players: bool = True
    ) -> float:
        return self.core.evaluate_ave_log_likelihood_games(games, ignore_null_players)
