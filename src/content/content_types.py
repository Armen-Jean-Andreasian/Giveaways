from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.scraping import ApiScraper
    from src.scraping.scrapers import PageScraper
    from src.models import HtmlStructure


class Content(ABC):
    identifier: str

    @abstractmethod
    def _analyze_response(self):
        ...

    @abstractmethod
    def _fetch_content(self):
        ...

    @abstractmethod
    def content(self) -> dict[str:list]:
        """
        Standardized property for Content class hierarchy.
        Carries the role of a lazy loader, as both `self.response` and `self.result` are not initialized.
        First, checks if self.response is fetched, if not - does it, if yes - skips the step.
        Then, checks if self.result is ready, if not - analyze the response, if yes - skip1.

        Returns the self.result which the prototype of ResponseModel filled with data.

        """
        # lazy initialization techniques

        # if content is not fetched
        # noinspection PyUnresolvedReferences
        if self.response is None:
            self._fetch_content()

        # if content is not analyzed
        # noinspection PyUnresolvedReferences
        if self.result is None:
            # noinspection PyAttributeOutsideInit
            self.result = {self.identifier: list()}
            self._analyze_response()

        return self.result


class ScrapableContent(Content, ABC):
    """
    Content that should be scraped from a website.
    It could be done using requests, selenium_, etc.
    It may be protected.
    """
    url: str
    headers: dict
    cookies: dict
    params: dict
    xpath: str
    css_selector: str
    html_structure: "HtmlStructure"

    @abstractmethod
    def __init__(self, page_scraper: "PageScraper"):
        ...


class RequestableContent(Content, ABC):
    """
    Content that is allowed to obtain.
    """
    api_url: str
    headers: dict
    cookies: dict
    params: dict

    @abstractmethod
    def __init__(self, api_scraper: "ApiScraper"):
        ...
