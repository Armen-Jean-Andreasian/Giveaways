from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service


class SeleniumScraper(Chrome):
    def __init__(self,
                 # options
                 headless: bool = False,
                 start_maximized=True,
                 turn_off_controlled_by=True,
                 # binaries
                 path_to_chrome_binary: str = None,
                 path_to_chromedriver_binary: str = None
                 ):

        self.service = Service()
        self.options = ChromeOptions()

        # options
        if headless:
            self.options.add_argument("--headless")

        if start_maximized:
            self.options.add_argument("start-maximized")

        if turn_off_controlled_by:
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.options.add_experimental_option('useAutomationExtension', False)

        # binaries
        if path_to_chrome_binary:
            self.options.binary_location = path_to_chrome_binary

        if path_to_chromedriver_binary:
            self.service = Service(executable_path=path_to_chromedriver_binary)

        super().__init__(options=self.options, service=self.service)
