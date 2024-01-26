"""Parent classes for all Crawlers"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

import feedparser
import requests
from bs4 import BeautifulSoup


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
        return f'{self.category} | {self.title} | {self.url} | {self.preview}'


class Crawler(ABC):
    """Abstract crawler

    Attributes:
        url: website page address
        payload: collected data in News() objects

    Methods:
        __str__: crawler name
        collect: get data from website or other source
        request_and_parse_HTML: get HTML by requests + BeautifulSoup
        request_RSS: get RSS feed
    """

    url: str
    payload: list[News] = []

    @abstractmethod
    def __str__(self) -> str:
        """Return crawler name"""

    @abstractmethod
    def collect(self) -> None:
        """Collect data and store in payload"""

    @staticmethod
    def request_and_parse_HTML(url: str,
                     encoding: str='utf-8',
                     timeout_in_sec: int=20,
                     headers: Optional[dict[str, str]]=None) -> BeautifulSoup:
        """Get website from requests and parse HTML using BeautifulSoup

        Args:
            url: website page address
            encoding: page encoding, def: utf-8
            timeout_in_sec: total timeout for reqest, def: 20
            headers: request headers {User-Agent, Content-Type}

        Returns:
            BeautifulSoup object

        Raises:
            ConnectionError: if website returns any code other than 200
        """

        # Set default headers if None provided
        headers = headers or {
                                'User-Agent': 'Mozilla/5.0',
                                'Content-Type': 'text/html;',
                            }

        # Send request
        response = requests.get(url, headers=headers, timeout=timeout_in_sec)

        # Check return code
        if response.status_code != 200:
            raise ConnectionError(f'Fail to load {url}')

        # Apply encoding
        response.encoding = encoding

        return BeautifulSoup(response.text, 'html.parser')

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