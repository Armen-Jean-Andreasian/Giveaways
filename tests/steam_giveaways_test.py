import unittest
from content import SteamGiveaways
from scraping import SteamGiveawaysScraper


class TestSteamGiveaways(unittest.TestCase):
    def setUp(self):
        self.mock_page_scraper = SteamGiveawaysScraper()
        self.steam_giveaways = SteamGiveaways(steam_giveaways_scraper=self.mock_page_scraper)

    def test_content_return_type(self):
        content: dict[list[dict]] = self.steam_giveaways.content

        self.assertIsInstance(obj=content, cls=dict)
        self.assertEqual(len(content), 1)

        self.assertIn(member=self.steam_giveaways.identifier, container=content)
        self.assertIs(expr1=type(content[self.steam_giveaways.identifier]),
                      expr2=list if content[self.steam_giveaways.identifier] is not None else type(None))


if __name__ == '__main__':
    unittest.main()
