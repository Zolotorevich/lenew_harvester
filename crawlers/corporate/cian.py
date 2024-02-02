"""Циан [CIAN]

Crawlers:
    All_News: https://cian.ru/novosti/company/
    Invest: https://ir.ciangroup.ru/ru/press-center/press-releases/
    Regulatory: https://ir.ciangroup.ru/ru/financials/regulatory-news/
    Media: https://ir.ciangroup.ru/ru/press-center/media/

"""

from crawlers.abstract import Crawler, News
from debug import debug


class Cian(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Циан Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)
        debug.dump_to_file(soup)

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

class All_News(Cian):
    """cian: https://cian.ru/novosti/company/"""
    
    category: str = 'cian'
    url: str = 'https://cian.ru/novosti/company/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Циан News'

class Invest(Cian):
    """cian: https://ir.ciangroup.ru/ru/press-center/press-releases/"""
    
    category: str = 'cian'
    url: str = 'https://ir.ciangroup.ru/ru/press-center/press-releases/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Циан Пресс-релизы'

class Regulatory(Cian):
    """cian: https://ir.ciangroup.ru/ru/financials/regulatory-news/"""
    
    category: str = 'cian'
    url: str = 'https://ir.ciangroup.ru/ru/financials/regulatory-news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Циан Существенные факты'

class Media(Cian):
    """cian: https://ir.ciangroup.ru/ru/press-center/media/"""
    
    category: str = 'cian'
    url: str = 'https://ir.ciangroup.ru/ru/press-center/media/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Циан СМИ о нас'