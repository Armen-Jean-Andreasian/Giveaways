from abc import ABC, abstractmethod
from .requests_ import get_url
from .selenium_ import SeleniumScraper
import time


# abstraction level 0: what's a scraper
class Scraper(ABC):
    @staticmethod
    @abstractmethod
    def get(*args, **kwargs):
        ...


# abstraction level 1 : what type of scrapers are there
class WebPageScraper(Scraper, ABC):
    # webpage scrapers can use a directs requests_ to the source, or a third-party tool
    ...


class ApiScraper(Scraper):
    # api scrapers use direct requests to the source
    @staticmethod
    @abstractmethod
    def get(url: str, headers: dict = None, cookies: dict = None, params: dict = None):
        ...


# abstraction level 2 : what tools those scrapers use?
class WebpageScraperRequests(WebPageScraper, ABC):
    # implementation of a webpage scraper using requests library
    @staticmethod
    def get(url: str, headers: dict = None, cookies: dict = None, params: dict = None):
        return get_url(url=url, params=params, headers=headers, cookies=cookies)


class ApiScraperRequests(ApiScraper, ABC):
    # implementation of an api scraper using requests library
    @staticmethod
    def get(url: str, headers: dict = None, cookies: dict = None, params: dict = None):
        # as the behaviors match with the scraper of webpage working on requests
        return WebpageScraperRequests.get(url=url, params=params, headers=headers, cookies=cookies)


class WebpageScraperSelenium(WebPageScraper, ABC):
    # implementation of a webpage scraper using selenium_ library
    def __init__(self):
        self.scraper = SeleniumScraper()

    def get(self, url: str, wait: int = 5) -> str:
        self.scraper.get(url)
        time.sleep(wait)

        html_code = self.scraper.page_source
        self.scraper.quit()
        return html_code


# implementations
class SteamWebScraper(WebpageScraperRequests):
    # steam website is not protected
    ...


class EpicWebScraper(WebpageScraperSelenium):
    # Epic Games is protected with CloudFlare.
    ...


class SteamApiScraper(ApiScraperRequests):
    # Steam API doesn't require auth
    ...
