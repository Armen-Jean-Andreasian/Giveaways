from .content_types import ScrapableContent
from bs4 import BeautifulSoup
from src.models import ResponseModel


class EpicGamesGiveaways(ScrapableContent):
    identifier = "epic_games_giveaways"
    url = "https://store.epicgames.com/en-US/free-games"

    def __init__(self, scraper):
        self.epic_games_scraper = scraper
        # noinspection PyTypeChecker
        self.response: str = None
        # noinspection PyTypeChecker
        self.result: dict[str:list] = None

    def _fetch_content(self):
        self.response = self.epic_games_scraper.get(self.url)
        return self

    def _analyze_response(self):
        soup = BeautifulSoup(self.response, 'html.parser')
        # detecting giveaways section
        giveaways_section = soup.find_all(class_="css-1myhtyb")

        for element in giveaways_section:
            games = element.find_all(class_="css-2mlzob")
            for game in games:
                time_span = game.find(class_="css-y2j3ic").span
                # checking if the game is currently free. (if it will - we skip)
                if time_span and "Free Now" in time_span.text:
                    game_name: str = game.find(class_="css-119zqif").text
                    game_url: str = "https://store.epicgames.com/" + game.find("a")["href"]
                    rectangle_img_url: str = game.find("img")["src"]

                    response: dict = ResponseModel.prototype(
                        game_name=game_name,
                        game_url=game_url,
                        rectangle_img_url=rectangle_img_url
                    )

                    self.result[self.identifier].append(response)

    @property
    def content(self) -> dict[str:list]:
        """Executes the circle and returns the final result."""
        return super().content()

