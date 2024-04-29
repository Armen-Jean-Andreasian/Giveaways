from .content import SteamFreeWeekend, SteamGiveaways, EpicGamesGiveaways
from .scraping import SteamApiScraper, SteamWebScraper, EpicWebScraper
from .logger import Logger
from .misc import TimeTracker
from .cache import Cache


class AppBase:
    logger = Logger().logger

    @classmethod
    def _obtain_data_from_server(cls, giveaway_class: type, scraper_class: type) -> dict:
        giveaway_obj = giveaway_class(scraper_class())
        return giveaway_obj.content

    @classmethod
    def _steam_free_weekend(cls):
        """Obtains data of Steam giveaways from Steam API"""
        try:
            # trying to obtain data
            return cls._obtain_data_from_server(giveaway_class=SteamFreeWeekend, scraper_class=SteamApiScraper)
        except Exception as e:
            # logging possible errors
            cls.logger.error(f"Error in Steam Free Weekend deals: {e}")

    @classmethod
    def _steam_giveaway(cls):
        """Obtains data of Steam giveaways from Steam website"""
        try:
            return cls._obtain_data_from_server(giveaway_class=SteamGiveaways, scraper_class=SteamWebScraper)
        except Exception as e:
            cls.logger.error(f"Error in Steam Giveaways: {e}")

    @classmethod
    def _epic_games_giveaway(cls):
        try:
            return cls._obtain_data_from_server(giveaway_class=EpicGamesGiveaways, scraper_class=EpicWebScraper)
        except Exception as e:
            cls.logger.error(f"Error in Epic Games Giveaways: {e}")


class App(AppBase):
    """
    Main class of the app.
    It holds _cache class attribute which gets filled partially. In the end of the day (by USA time) it resets.

    The class provides one method: get_deals.
    If an error occurs it's being logged, but no errors will be risen.

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
        if steam_free_weekend:  # if was requested
            if Cache.find_data(SteamFreeWeekend.identifier) is None:  # if data is not found in cache
                steam_fw_data = cls._steam_free_weekend()  # obtaining
                # saving to cache
                Cache.save_data(giveaway_identifier=SteamFreeWeekend.identifier, giveaway_content=steam_fw_data)

            # including the value from cache to result
            result.update(Cache.find_data(giveaway_identifier=SteamFreeWeekend.identifier))

        if steam_giveaways:
            if Cache.find_data(giveaway_identifier=SteamGiveaways.identifier) is None:
                steam_gw_data = cls._steam_giveaway()
                Cache.save_data(giveaway_identifier=SteamGiveaways.identifier, giveaway_content=steam_gw_data)
            result.update(Cache.find_data(giveaway_identifier=SteamGiveaways.identifier))

        if epic_games_giveaways:
            if Cache.find_data(EpicGamesGiveaways.identifier) is None:
                epic_games_data = cls._epic_games_giveaway()
                Cache.save_data(giveaway_identifier=EpicGamesGiveaways.identifier, giveaway_content=epic_games_data)
            result.update(Cache.find_data(giveaway_identifier=EpicGamesGiveaways.identifier))

        return result
