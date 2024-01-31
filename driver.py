import time

from selenium import webdriver


class Selenium_Driver():
    """Selenium driver object

    Raises:
        TimeoutError: page load timeout

    Methods:
        __init__: prepare and start driver
        get: get page HTML
        stop: stop the driver
    """

    lock:bool = False
    driver:webdriver

    def __init__(self) -> None:
        # Prepare driver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--user-agent="Mozilla/5.0"')

        # Start driver
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(20)
        
    def get(self, url:str) -> str:
        """Get page HTML

        Args:
            url: website page address

        Raises:
            TimeoutError: connection timeout, see __init__

        Returns:
            Page HTML as string
        """
        
        # Check lock and wait for it
        while self.lock:
            time.sleep(1)

        # Lock driver
        self.lock = True

        # Get page
        try:
            self.driver.get(url)
            return self.driver.page_source

        except Exception:
            raise TimeoutError('Selenium timeout')
            
        finally:
            # Unlock driver
            self.lock = False

    def stop(self):
        self.driver.quit()