from content import SteamFreeWeekend, SteamGiveaways
from scraping import SteamApiScraper, SteamGiveawaysScraper


class App:
    _cache = {'steam_fw': None, 'steam_gw': None}

    @classmethod
    def get_deals(cls, steam_free_weekend: bool = False, steam_giveaways: bool = False):
        temp = dict()
        temp.update(dict())

        if steam_free_weekend:
            cls._update_data(temp=temp, cache_key='steam_fw', content_obj=SteamFreeWeekend, scraper_obj=SteamApiScraper)
        if steam_giveaways:
            cls._update_data(temp=temp, cache_key='steam_gw', content_obj=SteamGiveaways,
                             scraper_obj=SteamGiveawaysScraper)

        return temp

    @classmethod
    def _update_data(cls, temp: dict, cache_key: str, content_obj, scraper_obj):
        # check in cache. if not found retrieves then saves to cache
        if cls._cache[cache_key] is None:
            free_games = content_obj(scraper_obj())
            cls._cache[cache_key] = free_games.content

        # updates the given dict
        temp.update(cls._cache[cache_key])
        return cls
