"""
Crawlers:
    Economy: https://www.interfax.ru/business/
"""

from crawlers.abstract import Crawler, News
from debug import debug


class TASS(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'TASS Parent Class'

    def collect(self, session) -> None:
        
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session)

        # Find news
        news_container = soup.select('#infinite_listing a')

        for news in news_container:
            
            # Find url
            url = news.get('href')
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://www.tass.ru' + url,
            }

            # Save result
            self.payload.append(News(**info))

class Economy(TASS):
    category: str = 'economy'
    url: str = 'https://tass.ru/ekonomika'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Economy'

class National_projects(TASS):
    category: str = 'economy'
    url: str = 'https://tass.ru/nacionalnye-proekty'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS National projects'

class Real_estate(TASS):
    category: str = 'economy'
    url: str = 'https://tass.ru/nedvizhimost'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Real estate'

class Small_business(TASS):
    category: str = 'economy'
    url: str = 'https://tass.ru/msp'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Small business'
    
class Politics(TASS):
    category: str = 'politics'
    url: str = 'https://tass.ru/politika'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Politics'

class World(TASS):
    category: str = 'politics'
    url: str = 'https://tass.ru/mezhdunarodnaya-panorama'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS World'

class Society(TASS):
    category: str = 'politics'
    url: str = 'https://tass.ru/obschestvo'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Society'

class Country(TASS):
    category: str = 'politics'
    url: str = 'https://tass.ru/v-strane'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Country'