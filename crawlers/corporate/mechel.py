"""Мечел [MTLR]

Crawlers:
    News: https://mechel.ru/press/news/
"""

from crawlers.abstract import Crawler, News


class mechel(Crawler):
    """Parent class"""

    category: str = 'mechel'

    def __str__(self) -> str:
        return 'Мечел Parent Class'

class All_News(mechel):
    """Мечел: Новости"""

    url: str = 'https://mechel.ru/press/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Мечел Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.release-card-body')

        for news in news_container:
            title = news.find('h4')
            
            # Get info
            info = {
                'category': self.category,
                'title': title.get_text(),
                'url': 'https://mechel.ru' + title.find('a').get('href'),
                'preview': news.find('div', class_='release-card-text').get_text(),
            }

            # Save result
            self.payload.append(News(**info))