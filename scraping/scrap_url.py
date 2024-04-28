from abc import ABC, abstractmethod
from .request import get_url


# abstractions
class PageScraper(ABC):
    ...


class PageScraperRequests(PageScraper):
    @staticmethod
    def get_url(url: str,
                headers: dict = None,
                cookies: dict = None,
                params: dict = None):
        return get_url(url=url, params=params, headers=headers, cookies=cookies)


class PageScraperSelenium(PageScraper):
    ...


# implementations
class SteamGiveawaysScraper(PageScraperRequests):
    ...
