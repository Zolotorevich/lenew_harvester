"""
Crawlers:
    Economy: https://www.interfax.ru/business/
"""

from crawlers.abstract import Crawler, News


class Interfax(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Interfax Parent Class'

    def collect(self, session) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session, 'windows-1251')

        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            # Find url and check if it's relative
            url = news.parent.get('href')
            if url[:1] == '/':
                url = 'https://www.interfax.ru' + url
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': url,
            }

            # Save result
            self.payload.append(News(**info))

class Economy(Interfax):
    category: str = 'economy'
    url: str = 'https://www.interfax.ru/business/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Interfax Economy'

class Main(Interfax):
    category: str = 'politics'
    url: str = 'https://www.interfax.ru/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Interfax Main page'