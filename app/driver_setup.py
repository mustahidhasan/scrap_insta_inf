import chromedriver_autoinstaller
from selenium import webdriver


class DriverSetup:
    def __init__(self, url):
        """
        :param url: url of the website
        """
        self.FORCE_HEADLESS = None
        self.driver = None
        self.selenium_url = None
        self.url = url

    def init_driver_local_chrome(self):
        """
        Initialize driver for local chrome
        :return: None
        """
        self.FORCE_HEADLESS = True
        self.driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=self._get_option_chrome_headless())

    def _get_option_chrome_default(self):
        """
        Get default options for chrome
        :return: options
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--hide-scrollbars')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--single-process")
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument("--start-maximized")
        options.add_argument("window-size=1920,1080")

        # if self.FORCE_HEADLESS:
        #     options.add_argument('--headless')

        return options

    def _get_option_chrome_headless(self):
        """
        Get options for chrome headless
        :return: options
        """
        options = self._get_option_chrome_default()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
            " Safari/537.36")

        return options

    def _get_option_chrome_headless_mobile(self):
        """
        Get options for chrome headless mobile
        :return: options
        """
        options = self._get_option_chrome_default()
        options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        options.add_argument(
            '--user-agent=Mozilla/5.0 '
            '(iPhone; CPU iPhone OS 10_2 like Mac OS X)'
            ' AppleWebKit/602.3.12 (KHTML, like Gecko) '
            'Version/10.0 Mobile/14C92 Safari/602.1')
        options.add_argument('--window-size=412,732')
        options.add_argument("--start-maximized")
        options.add_argument("--remote-debugging-port=0")

        return options

    def close(self):
        """
        Close driver
        :return: None
        """
        self.driver.close()

    def quit(self):
        """
        Quit driver
        :return: None
        """
        self.driver.quit()

    def _delete_local_storage(self):
        """
        Delete local storage
        :return: None
        """
        self.driver.execute_script(
            'window.localStorage.clear();'
        )

    def set_driver_url(self, url=None):
        """
        Set driver url
        :param url: to be set
        :return: None
        """
        try:
            if url is None:
                self.driver.get(self.url)
            else:
                self.driver.get(url)
        except Exception as e:
            raise