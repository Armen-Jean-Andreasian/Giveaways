from src.app import App
from utils.profiling import execution_time_decorator_factory, memory_usage_decorator_factory
from src.cache import LocalCache


@execution_time_decorator_factory(return_delta=True, print_delta=True)
def measure_time_deals_long() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@execution_time_decorator_factory(return_delta=True, print_delta=True)
def measure_time_deals_instant() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@memory_usage_decorator_factory(return_delta=True, print_delta=True)
def measure_memory_long() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@memory_usage_decorator_factory(return_delta=True, print_delta=True)
def measure_memory_instant() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


if __name__ == '__main__':
    measurement_L1 = measure_time_deals_long()
    measurement_I1 = measure_time_deals_instant()
    measurement_I2 = measure_time_deals_instant()

    LocalCache.reset()  # clearing cache manually to trigger another circle

    measurement_L2 = measure_memory_long()
    measurement_I3 = measure_memory_instant()
    measurement_I4 = measure_memory_instant()
