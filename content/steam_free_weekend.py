from .content_types import RequestableContent
from models import ResponseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scraping import SteamApiScraper


class SteamFreeWeekend(RequestableContent):
    api_url = "https://store.steampowered.com/api/featuredcategories/"

    def __init__(self, api_scraper: 'SteamApiScraper'):
        """
        :param api_scraper: the Scraper object for APIs. In this case SteamApiScraper, which substituted ApiScraper

        Attributes:
            - self.api_response: the response from Steam API. It is standardized.
            - self.parsed_status: keeping tracked if we analyzed the data yet
            - self.result: a list of ResponseModel's prototype dictionaries
        """
        self.steam_api_scraper: 'SteamApiScraper' = api_scraper
        # noinspection PyTypeChecker
        self.api_response: dict = None
        # noinspection PyTypeChecker
        self.result: list = None

    def _analyze_response(self):
        """ Extracts data out of response saves it to self.free_weekend_result. """

        """        
        Addition:
            The method is focused on processing data from a specific API response structure.
            The data structure can vary from source to source, and the processing logic may need to adapt accordingly. 
            Also, the data processing methods may consist of millions of nested loops.
        """
        temp = []
        try:
            # obtaining dicts containing free weekend data
            for key in self.api_response.keys():
                if key.isdigit():
                    temp.append(self.api_response[key])

            # free weekend games' details are in 'items'
            for data_dict in temp:
                data_capsule: list[dict] = data_dict["items"]
                # data_capsule has keys: 'name', 'header_image', 'body', 'url'

                for capsule_dict in data_capsule:
                    if capsule_dict['name'] == "Free Weekend":
                        img_url_square = capsule_dict["header_image"]

                        game_url = capsule_dict['url']
                        game_id = game_url.split(sep='/')[4]

                        img_url_rect = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game_id}/header.jpg"

                        response: dict = ResponseModel.prototype(
                            game_id=game_id,
                            game_url=game_url,
                            img_url_square=img_url_square,
                            img_url_rect=img_url_rect
                        )
                        self.result.append(response)
            temp.clear()
            return self
        except Exception as _:
            raise _

    @property
    def response(self):
        if self.api_response is None:
            self.api_response = self.steam_api_scraper.get_api(url=self.api_url).json()

        if self.result is None:
            self.result = []
            self._analyze_response()

        return self.result if self.result else [None]
