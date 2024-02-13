"""Московский кредитный банк [CBOM]

Crawlers:
    News: https://mkb.ru/news
"""

from crawlers.abstract import Crawler, News
from crawlers.search.interfax import Search_Interfax


class mkb(Crawler):
    """Parent class"""

    category: str = 'mkb'

    def __str__(self) -> str:
        return 'МКБ Parent Class'

class All_News(mkb):
    """Московский кредитный банк: Новости"""

    url: str = 'https://mkb.ru/news'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Московский кредитный банк Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('h3')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://mkb.ru' + news.parent.get('href'),
            }

            # Save result
            self.payload.append(News(**info))