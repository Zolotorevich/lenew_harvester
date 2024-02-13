"""Henderson [HNFG]

Crawlers:
    News: https://ir.henderson.ru/press-releases
"""

from crawlers.abstract import Crawler, News


class henderson(Crawler):
    """Parent class"""

    category: str = 'henderson'

    def __str__(self) -> str:
        return 'Henderson Parent Class'

class All_News(henderson):
    """Henderson: Новости"""

    url: str = 'https://ir.henderson.ru/press-releases'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Henderson Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.t-feed__link')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))