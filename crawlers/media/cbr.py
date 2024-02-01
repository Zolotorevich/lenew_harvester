"""ЦБ РФ

Crawlers:
    All_News: https://cbr.ru/news/
"""

from crawlers.abstract import Crawler, News


class CBR(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'ЦБ РФ Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news_title')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://cbr.ru' + news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class All_News(CBR):
    """economy: https://cbr.ru/news/"""
    
    category: str = 'economy'
    url: str = 'https://cbr.ru/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'ЦБ РФ Новости'