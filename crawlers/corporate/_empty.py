"""ORGANIZASTION

Crawlers:
    News: 
    Invest: 
"""

from crawlers.abstract import Crawler, News
from debug import debug


class EMPTY(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'ORGANIZASTION Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news_title')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://minfin.gov.ru' + news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class All_News(EMPTY):
    """economy: """
    
    category: str = 'economy'
    url: str = ''
    payload: list[News] = []

    def __str__(self) -> str:
        return 'ORGANIZASTION News'