"""
Crawlers:
    Economy: https://1prime.ru/state_regulation/
    Finance: https://1prime.ru/finance/
    IT: https://1prime.ru/telecommunications_and_technologies/
    Business: https://1prime.ru/business/
    Energy: https://1prime.ru/energy/
    Fin_market: https://1prime.ru/Financial_market/
"""

from crawlers.abstract import Crawler, News


class Prime(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Prime Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('article')

        for news in news_container:

            title = news.find('h2')
            
            # Get info
            info = {
                'category': self.category,
                'title': title.get_text(),
                'url': 'https://1prime.ru' + title.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class Economy(Prime):
    """economy: https://1prime.ru/state_regulation/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/state_regulation/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime Economy'

class Finance(Prime):
    """economy: https://1prime.ru/finance/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/finance/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime Finance'

class IT(Prime):
    """economy: https://1prime.ru/telecommunications_and_technologies/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/telecommunications_and_technologies/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime IT'

class Business(Prime):
    """economy: https://1prime.ru/business/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/business/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime Business'

class Energy(Prime):
    """economy: https://1prime.ru/energy/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/energy/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime Energy'

class Fin_market(Prime):
    """economy: https://1prime.ru/Financial_market/"""
    
    category: str = 'economy'
    url: str = 'https://1prime.ru/Financial_market/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Prime Fin_market'