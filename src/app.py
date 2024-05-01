from .web_content import SteamFreeWeekend, SteamGiveaways, EpicGamesGiveaways
from .scraping import SteamApiScraper, SteamWebScraper, EpicWebScraper
from .logger import Logger
from .helpers import TimeTracker
from .cache import LocalCache
from typing import Callable, Union

Giveaway = Union[type(SteamFreeWeekend), type(SteamGiveaways), type(EpicGamesGiveaways)]
Scraper = Union[type(SteamApiScraper), type(SteamWebScraper), type(EpicWebScraper)]


class DataObtainer:
    logger = Logger()

    @classmethod
    def _get_data_from_server(
            cls,
            giveaway_type: Giveaway,
            scraper_type: Scraper) -> dict[str, list]:

        try:
            # Instantiate the appropriate promo object based on giveaway_type
            promo = giveaway_type(scraper=scraper_type())
            return promo.content
        except Exception as e:
            cls.logger.log_exception(f"Error in {giveaway_type.__name__}: {e}")
            return {giveaway_type.identifier: list()}

    @classmethod
    def _steam_free_weekend(cls) -> dict[str, list]:
        return cls._get_data_from_server(SteamFreeWeekend, SteamApiScraper)

    @classmethod
    def _steam_giveaway(cls) -> dict[str, list]:
        return cls._get_data_from_server(SteamGiveaways, SteamWebScraper)

    @classmethod
    def _epic_games_giveaway(cls) -> dict[str, list]:
        return cls._get_data_from_server(EpicGamesGiveaways, EpicWebScraper)


class AppBase(DataObtainer):
    @staticmethod
    def _process_promotion(promo_key: str, cache: LocalCache, method_to_call_server: Callable, result: dict):
        data_in_cache: None | list = cache.find_data(promo_key)

        if data_in_cache is None:
            data_from_server: dict[str, list] = method_to_call_server()

            promo_details: list = data_from_server[promo_key]

            if promo_details:  # if the server hasn't sent an empty list
                cache.update_data(key=promo_key, value=promo_details)
        else:
            promo_details: list = data_in_cache

        # including promo data to result
        promo_container: dict = {promo_key: promo_details}
        result.update(promo_container)


class App(AppBase):
    """
    Main class of the app.
    It holds _cache class attribute which gets filled partially. In the end of the day (by USA time) it resets.

    The class provides one method: get_deals.
    If an error occurs it's being logged, but no errors will be raised.

    """

    @classmethod
    def get_deals(cls,
                  steam_free_weekend: bool = False,
                  steam_giveaways: bool = False,
                  epic_games_giveaways: bool = False) -> dict:

        # predefining the result
        result = dict()

        # if the data is outdated, resetting it
        if not TimeTracker.is_within_same_day(LocalCache.timestamp):
            LocalCache.reset()

        # processing
        if steam_free_weekend:
            cls._process_promotion(promo_key=SteamFreeWeekend.identifier, cache=LocalCache,
                                   method_to_call_server=cls._steam_free_weekend, result=result)

        if steam_giveaways:
            cls._process_promotion(promo_key=SteamGiveaways.identifier, cache=LocalCache,
                                   method_to_call_server=cls._steam_giveaway, result=result)

        if epic_games_giveaways:
            cls._process_promotion(promo_key=EpicGamesGiveaways.identifier, cache=LocalCache,
                                   method_to_call_server=cls._epic_games_giveaway, result=result)

        return result
