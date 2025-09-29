import whr_core


__version__ = whr_core.__version__


class Base:
    def __init__(self, config: dict = None, w2: float = 10.0, virtual_games: int = 2):
        if config is not None:
            if "w2" in config:
                w2 = config["w2"]
            if "virtual_games" in config:
                virtual_games = config["virtual_games"]
        self.core = whr_core.Base(w2, virtual_games)

    def print_ordered_ratings(self):
        self.core.print_ordered_ratings()

    def get_ordered_ratings(self) -> list:
        return self.core.get_ordered_ratings()

    def log_likelihood(self) -> float:
        return self.core.log_likelihood()

    def ratings_for_player(self, name: str) -> list:
        return self.core.ratings_for_player(name)

    def create_games(self, games: list):
        self.core.create_games(games)

    def create_game(
        self, white: str, black: str, winner: str, time_step: int
    ):
        self.core.create_game(white, black, winner, time_step)

    def iterate_until_converge(self, verbose: bool = True):
        self.core.iterate_until_converge(verbose)

    def iterate(self, count: int):
        self.core.iterate(count)
