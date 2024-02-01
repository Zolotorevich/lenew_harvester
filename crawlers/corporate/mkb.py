"""Московский кредитный банк

Crawlers:
    News: https://mkb.ru/news
    Invest: https://ir.mkb.ru/investor-relations/news
"""

from crawlers.abstract import Crawler, News
from debug import debug


class MKB(Crawler):
    """News: https://mkb.ru/news"""
    
    category: str = 'mkb'
    url: str = 'https://mkb.ru/news'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'МКБ News'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)
        debug.dump_to_file(soup, terminate=False)

        # # Find news
        # news_container = soup.select('.timeline h3')

        # for news in news_container:
            
        #     # Find url
        #     url = news.parent.get('href')
            
        #     # Get info
        #     info = {
        #         'category': self.category,
        #         'title': news.get_text(),
        #         'url': url,
        #     }

        #     # Save result
        #     self.payload.append(News(**info))

class Invest(MKB):
    """Invest news: https://ir.mkb.ru/investor-relations/news"""
    
    category: str = 'mkb'
    url: str = 'https://ir.mkb.ru/investor-relations/news'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'МКБ Invest News'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)
        debug.dump_to_file(soup, filename='dump1.html', terminate=False)