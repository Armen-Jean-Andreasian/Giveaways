from abc import ABC, abstractmethod
from .request import get_url


class ApiScraper(ABC):
    @staticmethod
    @abstractmethod
    def get_api(url: str,
                headers: dict = None,
                cookies: dict = None,
                params: dict = None):
        ...


class SteamApiScraper(ApiScraper):
    @staticmethod
    def get_api(url: str,
                headers: dict = None,
                cookies: dict = None,
                params: dict = None):
        # Steam API doesn't require auth
        return get_url(url=url, params=params, headers=headers, cookies=cookies)
