"""Parent classes for all Crawlers"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

import feedparser
import requests
from bs4 import BeautifulSoup

from driver import Selenium_Driver


@dataclass
class News():
    """Crawler payload objects"""

    category: str
    title: str
    url: str
    preview: Optional[str] = ''

    def __setattr__(self, __name: str, __value: Any) -> None:
        """Strip title and preview text"""
        
        if __name == 'title' or __name == 'preview':
            __value = __value.strip()

        self.__dict__[__name] = __value

    def __str__(self) -> str:
        return f'{self.title} | {self.preview} | {self.url} | {self.category}'


class Crawler(ABC):
    """Abstract crawler

    Methods:
        __str__: crawler name
        collect: get data from website or other source
        request_and_parse_HTML: get HTML by requests + BeautifulSoup
        selenium_and_parse_HTML: get HTML by Selenium + BeautifulSoup
        request_RSS: get RSS feed
    """

    session = requests.Session()
    driver = Selenium_Driver()

    @abstractmethod
    def __str__(self) -> str:
        """Return crawler name"""

    @abstractmethod
    def collect(self) -> None:
        """Collect data and store in payload"""

    def request_and_parse_HTML(self,
                     url: str,
                     encoding: str='utf-8',
                     timeout_in_sec: int=20,
                     headers: Optional[dict[str, str]]=None) -> BeautifulSoup:
        """Get website from requests and parse HTML using BeautifulSoup

        Args:
            url: website page address
            encoding: page encoding, def: utf-8
            timeout_in_sec: total timeout for reqest, def: 20
            headers: request headers {User-Agent, Content-Type}

        Raises:
            ConnectionError: website returns any code other than 200
            requests.ConnectionError: any network error
            requests.ReadTimeout: connection timeout

        Returns:
            HTML as BeautifulSoup object
        """

        # Set default headers if None provided
        headers = headers or {
                                'User-Agent': 'Mozilla/5.0',
                                'Content-Type': 'text/html;',
                            }

        # Send request
        response = self.session.get(url, headers=headers, timeout=timeout_in_sec)

        # Check return code
        if response.status_code != 200:
            raise ConnectionError(f'Fail to load {url}')

        # Apply encoding
        response.encoding = encoding

        return BeautifulSoup(response.text, 'html.parser')

    def selenium_and_parse_HTML(self, url:str) -> BeautifulSoup:
        """Get website HTML by Selenium and parse HTML using BeautifulSoup

        Args:
            url: website page address

        Returns:
            HTML as BeautifulSoup object
        """
        
        return BeautifulSoup(self.driver.get(url), 'html.parser')

    @staticmethod
    def request_RSS(url: str) -> feedparser.util.FeedParserDict:
        """Get RSS and return dict or None if RSS not found

        Args:
            url: RSS feed URL

        Returns:
            feedparser {dict}

        Raises:
            AttributeError: RSS unavailable
        """
        
        feed = feedparser.parse(url)
        getattr(feed, 'status')
        return feed