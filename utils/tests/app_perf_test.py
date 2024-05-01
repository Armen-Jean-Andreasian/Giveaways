from src.app import App
from utils.profiling import execution_time_decorator_factory, memory_usage_decorator_factory
from src.cache import LocalCache


@execution_time_decorator_factory(return_delta=False, print_delta=True)
def measure_time_deals_long() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@execution_time_decorator_factory(return_delta=False, print_delta=True)
def measure_time_deals_instant() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@memory_usage_decorator_factory(return_delta=False, print_delta=True)
def measure_memory_long() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


@memory_usage_decorator_factory(return_delta=False, print_delta=True)
def measure_memory_instant() -> float:
    return App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)


measure_time_deals_long()
measure_time_deals_instant()
LocalCache.reset()  # clearing cache manually to trigger another circle
measure_memory_long()
measure_memory_instant()
