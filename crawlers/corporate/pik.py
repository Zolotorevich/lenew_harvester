"""ПИК [PIKK]

Crawlers:
    News: https://pik-group.ru/about/news-and-reports/news
"""

from crawlers.abstract import Crawler, News


class pik(Crawler):
    """Parent class"""

    category: str = 'pik'

    def __str__(self) -> str:
        return 'ПИК Parent Class'

class All_News(pik):
    """ПИК: Новости"""

    url: str = 'https://pik-group.ru/about/news-and-reports/news'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'ПИК Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('div[class*="news__NewsWrapper-"]')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('span').get_text(),
                'url': 'https://pik-group.ru' + news.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))