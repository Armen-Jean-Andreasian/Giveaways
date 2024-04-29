from .content import SteamFreeWeekend, SteamGiveaways, EpicGamesGiveaways
from .misc import TimeTracker


class Cache:
    cache = {SteamFreeWeekend.identifier: None, SteamGiveaways.identifier: None, EpicGamesGiveaways.identifier: None}
    last_updated_datetime = TimeTracker.get_current_datetime()

    @classmethod
    def reset(cls):
        """Resets the values in cache to None"""
        for promo_name, value in cls.cache.items():
            cls.cache[promo_name] = None
        return cls

    @classmethod
    def save_data(cls, giveaway_identifier: str, giveaway_content: dict):
        """Saves data to cache"""
        cls.cache[giveaway_identifier] = giveaway_content
        return cls

    @classmethod
    def find_data(cls, giveaway_identifier: str):
        return cls.cache[giveaway_identifier]
