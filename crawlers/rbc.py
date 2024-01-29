"""
Crawlers:
    Economics: https://www.rbc.ru/economics/
    Business: https://www.rbc.ru/business/
    Finances: https://www.rbc.ru/finances/
"""

from crawlers.abstract import Crawler, News


class RBC(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'RBC parent class'

    def collect(self, session) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session)

        # Find news
        news_container = soup.find_all('div', class_='item__wrap')

        for news in news_container:

            try:
                # Get URL
                url = news.find('a', class_='item__link').get('href')
            except AttributeError:
                # It's currencies rates, ignore
                continue

            title = news.find('span', class_='item__title').get_text()

            # Get info
            info = {
                'category': self.category,
                'url': url,
                'title': title,
            }

            # Save result
            self.payload.append(News(**info))

class Economics(RBC):
    """economy: https://www.rbc.ru/economics/"""
    
    category: str = 'economy'
    url: str = 'https://www.rbc.ru/economics/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'RBC Economics'

class Business(RBC):
    """economy: https://www.rbc.ru/business/"""
    
    category: str = 'economy'
    url: str = 'https://www.rbc.ru/business/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'RBC Business'

class Finances(RBC):
    """economy: https://www.rbc.ru/finances/"""
    
    category: str = 'economy'
    url: str = 'https://www.rbc.ru/finances/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'RBC Finances'