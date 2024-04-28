import unittest
from content import SteamFreeWeekend
from scraping import SteamApiScraper


class TestSteamFreeWeekend(unittest.TestCase):
    def setUp(self):
        self.mock_api_scraper = SteamApiScraper()
        self.steam_free_weekend = SteamFreeWeekend(api_scraper=self.mock_api_scraper)

    def test_content_return_type(self):
        content: dict[list[dict]] = self.steam_free_weekend.content

        self.assertIsInstance(content, dict)
        self.assertEqual(len(content), 1)

        self.assertIn(member=self.steam_free_weekend.identifier, container=content)
        self.assertIs(expr1=type(content[self.steam_free_weekend.identifier]),
                      expr2=list if content[self.steam_free_weekend.identifier] is not None else type(None))


if __name__ == '__main__':
    unittest.main()
