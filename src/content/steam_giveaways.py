from bs4 import BeautifulSoup
from typing import TYPE_CHECKING
from .content_types import ScrapableContent
from src.models import ResponseModel

if TYPE_CHECKING:
    from src.scraping import SteamWebScraper


class SteamGiveaways(ScrapableContent):
    identifier = "steam_giveaways"

    url = "https://store.steampowered.com/search/results"
    params = {
        'force_infinite': '1',
        'maxprice': 'free',
        'specials': '1',
    }

    def __init__(self, scraper: 'SteamWebScraper'):
        self.steam_giveaways_scraper = scraper
        # noinspection PyTypeChecker
        self.response: bytes = None
        # noinspection PyTypeChecker
        self.result: dict[str:list] = None

    def _fetch_content(self):
        self.response = self.steam_giveaways_scraper.get(url=self.url, params=self.params).content
        return self

    def _analyze_response(self):
        soup = BeautifulSoup(self.response, 'html.parser')
        game_elements = soup.find_all('a', class_='search_result_row')

        for game_element in game_elements:
            game_name = game_element.find('span', class_='title').text.strip()
            game_url = game_element['href']

            # 'https://store.steampowered.com/app/235900/RPG_Maker_XP/?snr=1_7_7_2300_150_1'

            game_id = game_url.split(sep='/')[4]
            rectangle_img_url = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game_id}/header.jpg"

            # saving to dictionary
            response: dict = ResponseModel.prototype(
                game_name=game_name,
                game_id=game_id,
                game_url=game_url,
                rectangle_img_url=rectangle_img_url
            )

            # appending dict with the game to the value of self.results
            self.result[self.identifier].append(response)
        return self

    @property
    def content(self) -> dict[str:list]:
        """Executes the circle and returns the final result."""
        return super().content()
