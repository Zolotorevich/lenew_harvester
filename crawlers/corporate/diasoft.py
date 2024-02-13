"""Диасофт [DIAS]

Crawlers:
    News: https://www.diasoft.ru/about/news/
"""

from crawlers.abstract import Crawler, News


class diasoft(Crawler):
    """Parent class"""

    category: str = 'diasoft'

    def __str__(self) -> str:
        return 'Диасофт Parent Class'

class All_News(diasoft):
    """Диасофт: Новости"""

    url: str = 'https://www.diasoft.ru/about/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Диасофт Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)
        
        # Find news
        news_container = soup.select('.news-list li')

        for news in news_container:
            title = news.find('a')

            info = {
                'category': self.category,
                'title': title.get_text(),
                'url': 'https://www.diasoft.ru' + title.get('href'),
                'preview': news.find('div', class_='news-preview').get_text(),
            }

            # Save result
            self.payload.append(News(**info))