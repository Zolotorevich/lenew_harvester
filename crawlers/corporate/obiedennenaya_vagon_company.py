"""Объединённая Вагонная Компания [UWGN]

Crawlers:
    News: https://www.uniwagon.com/multimedia/news/
"""

from crawlers.abstract import Crawler, News


class utair(Crawler):
    """Parent class"""

    category: str = 'obiedennenaya_vagon_company'

    def __str__(self) -> str:
        return 'Объединённая Вагонная Компания Parent Class'

class All_News(utair):
    """Объединённая Вагонная Компания: Новости"""

    url: str = 'https://www.uniwagon.com/multimedia/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Объединённая Вагонная Компания Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news')

        for news in news_container:
            
            
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://www.uniwagon.com' + news.find('a').get('href'),
                'preview': news.find('div', class_='news__description').get_text(),
            }

            # Save result
            self.payload.append(News(**info))