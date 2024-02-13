"""Выборгский судозавод [VSYD]

Crawlers:
    News: http://vyborgshipyard.ru/ru/rubric/na-russkom
    Korabel: search Korabel website
"""

from crawlers.abstract import Crawler, News
from crawlers.search.korabel import Search_Korabel


class viborgsky_sudzavod(Crawler):
    """Parent class"""

    category: str = 'viborgsky_sudzavod'

    def __str__(self) -> str:
        return 'Выборгский судозавод Parent Class'

class All_News(viborgsky_sudzavod):
    """Выборгский судозавод: Новости"""

    url: str = 'http://vyborgshipyard.ru/ru/rubric/na-russkom'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Выборгский судозавод Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('h3')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': self.url + news.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class Korabel(viborgsky_sudzavod, Search_Korabel):
    """Search Korabel"""

    search_query: str = 'vyborgshipyard'
    payload: list[News] = []

    def __str__(self) -> str:
        return f'Search Korabel: {self.search_query}'