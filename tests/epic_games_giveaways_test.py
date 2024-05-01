import unittest
from src.web_content import EpicGamesGiveaways
from src.scraping import EpicWebScraper


class TestEpicGamesGiveaways(unittest.TestCase):
    def setUp(self):
        self.mock_scraper = EpicWebScraper()
        self.epic_games_giveaways = EpicGamesGiveaways(scraper=self.mock_scraper)

    def test_content_return_type(self):
        content = self.epic_games_giveaways.content
        print(content)

        self.assertIsInstance(content, dict)
        self.assertEqual(len(content), 1)

        self.assertIn(self.epic_games_giveaways.identifier, content)
        self.assertIs(type(content[self.epic_games_giveaways.identifier]), list)


if __name__ == '__main__':
    unittest.main()
