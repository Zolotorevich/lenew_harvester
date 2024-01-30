"""
Crawlers:
    Economy: https://www.kommersant.ru/rubric/3
    Finance: https://www.kommersant.ru/finance
    Market: https://www.kommersant.ru/rubric/41
    Business: https://www.kommersant.ru/rubric/4
"""

import json

from crawlers.abstract import Crawler, News


class Kommersant(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Kommersant parent class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Parse JSON
        script = soup.find_all('script', type='application/ld+json')[1].string
        data = json.loads(script)

        # Find news
        for news in data['itemListElement']:
            
            # Get info
            info = {
                'category': self.category,
                'url': news['url'],
                'title': news['name'],
            }

            # Save result
            self.payload.append(News(**info))


class Economy(Kommersant):
    """economy: https://www.kommersant.ru/rubric/3"""
    
    category: str = 'economy'
    url: str = 'https://www.kommersant.ru/rubric/3'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Kommersant Economy'

class Finance(Kommersant):
    """economy: https://www.kommersant.ru/finance"""
    
    category: str = 'economy'
    url: str = 'https://www.kommersant.ru/finance'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Kommersant Finance'

class Market(Kommersant):
    """economy: https://www.kommersant.ru/rubric/41"""
    
    category: str = 'economy'
    url: str = 'https://www.kommersant.ru/rubric/41'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Kommersant Market'

class Business(Kommersant):
    """economy: https://www.kommersant.ru/rubric/4"""
    
    category: str = 'economy'
    url: str = 'https://www.kommersant.ru/rubric/4'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Kommersant Business'