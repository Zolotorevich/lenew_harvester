"""Novabev [BELU]

Crawlers:
    News: https://novabev.com/press-room/lenta/
"""

from crawlers.abstract import Crawler, News


class novabev(Crawler):
    """Parent class"""

    category: str = 'novabev'

    def __str__(self) -> str:
        return 'Novabev Parent Class'

class All_News(novabev):
    """Novabev: Новости"""

    url: str = 'https://novabev.com/press-room/lenta/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Novabev Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.lenta-item')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://novabev.com' + news.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))
