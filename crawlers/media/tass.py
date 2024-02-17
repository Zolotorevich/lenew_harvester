"""
Crawlers:
    Economy: https://tass.ru/ekonomika
    National_projects: https://tass.ru/nacionalnye-proekty
    Real_estate: https://tass.ru/nedvizhimost
    Small_business: https://tass.ru/msp
    Politics: https://tass.ru/politika
    World: https://tass.ru/mezhdunarodnaya-panorama
    Society: https://tass.ru/obschestvo
    Country: https://tass.ru/v-strane
"""

from crawlers.abstract import Crawler, News


class TASS(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'TASS Parent Class'

    def collect(self) -> None:
        
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('#infinite_listing a')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.select('span[class*="tass_pkg_title-"]')[0].get_text(),
                'url': 'https://www.tass.ru' + news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class Economy(TASS):
    """economy: https://tass.ru/ekonomika"""
    category: str = 'economy'
    url: str = 'https://tass.ru/ekonomika'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Economy'

class National_projects(TASS):
    """economy: https://tass.ru/nacionalnye-proekty"""
    category: str = 'economy'
    url: str = 'https://tass.ru/nacionalnye-proekty'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS National projects'

class Real_estate(TASS):
    """economy: https://tass.ru/nedvizhimost"""
    category: str = 'economy'
    url: str = 'https://tass.ru/nedvizhimost'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Real estate'

class Small_business(TASS):
    """economy: https://tass.ru/msp"""
    category: str = 'economy'
    url: str = 'https://tass.ru/msp'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Small business'
    
class Politics(TASS):
    """politics: https://tass.ru/politika"""
    category: str = 'politics'
    url: str = 'https://tass.ru/politika'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Politics'

class World(TASS):
    """politics: https://tass.ru/mezhdunarodnaya-panorama"""
    category: str = 'politics'
    url: str = 'https://tass.ru/mezhdunarodnaya-panorama'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS World'

class Society(TASS):
    """politics: https://tass.ru/obschestvo"""
    category: str = 'politics'
    url: str = 'https://tass.ru/obschestvo'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Society'

class Country(TASS):
    """politics: https://tass.ru/v-strane"""
    category: str = 'politics'
    url: str = 'https://tass.ru/v-strane'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'TASS Country'