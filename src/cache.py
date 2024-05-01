from .web_content import SteamFreeWeekend, SteamGiveaways, EpicGamesGiveaways
from .helpers import TimeTracker
import datetime


class LocalCache:
    """
    Local key-value cache with timestamp functionality.

    This class provides a simple in-memory cache with key-value pairs, along with
    timestamp functionality similar to ORM implementations. It mimics the 
    functionality of a key-value store like Redis but operates locally within
    the application.

    Attributes:
        cache (dict): A dictionary to store key-value pairs.
        timestamp (datetime): The current datetime when the cache was last modified.
    """
    cache = {SteamFreeWeekend.identifier: None, SteamGiveaways.identifier: None, EpicGamesGiveaways.identifier: None}
    timestamp: datetime = TimeTracker.get_current_datetime()

    @classmethod
    def reset(cls):
        """Resets the values in cache to None"""
        for promo_name, value in cls.cache.items():
            cls.cache[promo_name] = None
        return cls

    @classmethod
    def update_data(cls, key: str, value: list):
        """Saves data to cache"""
        cls.cache[key] = value
        return cls

    @classmethod
    def find_data(cls, giveaway_identifier: str) -> None | list:
        return cls.cache[giveaway_identifier]
