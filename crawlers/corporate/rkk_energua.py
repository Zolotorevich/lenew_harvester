"""РКК Энергия [RKEE]

Crawlers:
    News: 
"""

from crawlers.abstract import Crawler, News


class rkk_energua(Crawler):
    """Parent class"""

    category: str = 'rkk_energua'

    def __str__(self) -> str:
        return 'РКК Энергия Parent Class'

class All_News(rkk_energua):
    """РКК Энергия: Новости"""

    url: str = 'https://www.energia.ru/ru/news/news.html'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'РКК Энергия Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news-item')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://www.energia.ru' + news.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))