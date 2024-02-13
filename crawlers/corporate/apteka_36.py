"""Аптека 36,6 [APTK]

Crawlers:
    News: https://pharmacychain366.ru/news/press-relizy/
"""

from crawlers.abstract import Crawler, News


class apteka_36(Crawler):
    """Parent class"""

    category: str = 'apteka_36'

    def __str__(self) -> str:
        return 'Аптека 36,6 Parent Class'

class All_News(apteka_36):
    """Аптека 36,6: Новости"""

    url: str = 'https://pharmacychain366.ru/news/press-relizy/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Аптека 36,6 Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news__item')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('h3').get_text(),
                'url': 'https://pharmacychain366.ru' + news.get('href'),
                'preview': news.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))