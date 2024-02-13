"""FESCO [HNFG]

Crawlers:
    News: https://www.fesco.ru/ru/press-center/news/
"""

from crawlers.abstract import Crawler, News


class FESCO(Crawler):
    """Parent class"""

    category: str = 'fesco'

    def __str__(self) -> str:
        return 'FESCO Parent Class'

class All_News(FESCO):
    """FESCO: Новости"""

    url: str = 'https://www.fesco.ru/ru/press-center/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'FESCO Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news-list-new__item')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://www.fesco.ru' + news.find('a').get('href'),
                'preview': news.find('div', class_='news-card__preview-inner').get_text(),
            }

            # Save result
            self.payload.append(News(**info))