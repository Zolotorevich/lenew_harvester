"""Норникель [GMKN]

Crawlers:
    News: https://nornickel.ru/news-and-media/press-releases-and-news/
"""

from crawlers.abstract import Crawler, News


class nornickel(Crawler):
    """Parent class"""

    category: str = 'nornickel'

    def __str__(self) -> str:
        return 'Норникель Parent Class'

class All_News(nornickel):
    """Норникель: Новости"""

    url: str = 'https://nornickel.ru/news-and-media/press-releases-and-news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Норникель Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news-list__body')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://nornickel.ru' + news.find('a').get('href'),
                'preview': news.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))