from .content_types import RequestableContent
from src.models import ResponseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.scraping import SteamApiScraper


class SteamFreeWeekend(RequestableContent):
    api_url = "https://store.steampowered.com/api/featuredcategories/"
    identifier = "steam_free_weekend"

    def __init__(self, steam_api_scraper: 'SteamApiScraper'):
        """
        :param steam_api_scraper: the Scraper object for APIs. In this case SteamApiScraper, which substituted ApiScraper

        Attributes:
            - self.api_response: the response from Steam API. It is standardized.
            - self.parsed_status: keeping tracked if we analyzed the data yet
            - self.result: a list of ResponseModel's prototype dictionaries
        """
        self.steam_api_scraper: 'SteamApiScraper' = steam_api_scraper
        # noinspection PyTypeChecker
        self.api_response: dict = None
        # noinspection PyTypeChecker
        self.result: dict[str:list] = None  # {'steam_free_weekend': []}

    def _fetch_content(self):
        self.api_response = self.steam_api_scraper.get(url=self.api_url).json()
        return self

    def _analyze_response(self):
        """ Extracts data out of response saves it to self.free_weekend_result. """

        """        
        Addition:
            The method is focused on processing data from a specific API response structure.
            The data structure can vary from source to source, and the processing logic may need to adapt accordingly. 
            Also, the data processing methods may consist of millions of nested loops.
        """
        temp = []  # needed
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
                    # detecting free weekend deals
                    if capsule_dict['name'] == "Free Weekend":
                        # collecting data

                        game_url = capsule_dict['url']
                        game_id = game_url.split(sep='/')[4]

                        rectangle_img_url = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game_id}/header.jpg"
                        square_img_url = capsule_dict["header_image"]

                        # saving to dictionary.
                        response: dict = ResponseModel.prototype(
                            game_id=game_id,
                            game_url=game_url,
                            img_url_square=square_img_url,
                            rectangle_img_url=rectangle_img_url
                        )
                        # appending dict with the game to the value of self.results
                        self.result[self.identifier].append(response)

            # cleaning environment before leaving
            temp.clear()
            return self

        # in case of fire
        except Exception as _:
            raise _

    @property
    def content(self) -> dict[str, list]:
        # lazy initialization techniques
        if self.api_response is None:
            self._fetch_content()

        if self.result is None:
            self.result = {self.identifier: list()}
            self._analyze_response()

        return self.result
