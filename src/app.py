from .content import SteamFreeWeekend, SteamGiveaways, EpicGamesGiveaways
from .scraping import SteamApiScraper, SteamWebScraper, EpicWebScraper
from .logger import Logger
from .misc import TimeTracker
from .cache import Cache
from typing import Callable


class DataObtainer:
    logger = Logger()

    @classmethod
    def _obtain_data_from_server(cls, giveaway_class: type, scraper_class: type) -> dict:
        try:
            giveaway_obj = giveaway_class(scraper_class())
            return giveaway_obj.content
        except Exception as e:
            cls.logger.log_exception(msg=f"Error in obtaining data: {e}")
            return {}

    @classmethod
    def _data_from_server(cls, giveaway_type: SteamFreeWeekend | SteamGiveaways | EpicGamesGiveaways,
                          scraper_type: SteamApiScraper | SteamWebScraper | EpicWebScraper) -> dict[str, list]:
        try:
            return cls._obtain_data_from_server(giveaway_class=giveaway_type, scraper_class=scraper_type)
        except Exception as e:
            cls.logger.log_exception(f"Error in {giveaway_type.__name__}: {e}")
            return {giveaway_type.identifier: list()}

    @classmethod
    def _steam_free_weekend(cls) -> dict[str, list]:
        return cls._data_from_server(SteamFreeWeekend, SteamApiScraper)

    @classmethod
    def _steam_giveaway(cls) -> dict[str, list]:
        return cls._data_from_server(SteamGiveaways, SteamWebScraper)

    @classmethod
    def _epic_games_giveaway(cls) -> dict[str, list]:
        return cls._data_from_server(EpicGamesGiveaways, EpicWebScraper)


class AppBase(DataObtainer):
    @staticmethod
    def _process_promotion(promo_key: str, cache: Cache, method_to_call_server: Callable, result: dict):
        data_in_cache: None | list = cache.find_data(promo_key)

        if data_in_cache is None:
            data_from_server: dict[str, list] = method_to_call_server()

            promo_details: list = data_from_server[promo_key]
            print(promo_key, promo_details)

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
        if not TimeTracker.is_within_same_day(Cache.last_updated_datetime):
            Cache.reset()

        # processing
        if steam_free_weekend:
            cls._process_promotion(promo_key=SteamFreeWeekend.identifier, cache=Cache,
                                   method_to_call_server=cls._steam_free_weekend, result=result)

        if steam_giveaways:
            cls._process_promotion(promo_key=SteamGiveaways.identifier, cache=Cache,
                                   method_to_call_server=cls._steam_giveaway, result=result)

        if epic_games_giveaways:
            cls._process_promotion(promo_key=EpicGamesGiveaways.identifier, cache=Cache,
                                   method_to_call_server=cls._epic_games_giveaway, result=result)

        return result
