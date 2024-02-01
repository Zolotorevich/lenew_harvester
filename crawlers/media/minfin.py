"""ЦБ РФ

Crawlers:
    All_News: https://minfin.gov.ru/ru/press-center/
"""

from crawlers.abstract import Crawler, News


class CBR(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Минфин Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news_title')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://minfin.gov.ru' + news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class All_News(CBR):
    """economy: https://minfin.gov.ru/ru/press-center/"""
    
    category: str = 'economy'
    url: str = 'https://minfin.gov.ru/ru/press-center/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Минфин новости'