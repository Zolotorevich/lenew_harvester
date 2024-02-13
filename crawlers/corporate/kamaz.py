"""KAMAZ [KMAZ]

Crawlers:
    News: https://kamaz.ru/press/releases/
"""

from crawlers.abstract import Crawler, News
from debug import debug


class kamaz(Crawler):
    """Parent class"""

    category: str = 'kamaz'

    def __str__(self) -> str:
        return 'KAMAZ Parent Class'

class All_News(kamaz):
    """KAMAZ: Новости"""

    url: str = 'https://kamaz.ru/press/releases/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'KAMAZ Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news-list-item')

        for news in news_container:

            title_container = news.find('div', class_='title')
            
            # Get info
            info = {
                'category': self.category,
                'title': title_container.get_text(),
                'url': 'https://kamaz.ru' + title_container.find('a').get('href'),
                'preview': news.find('div', class_='text').get_text(),
            }

            # Save result
            self.payload.append(News(**info))