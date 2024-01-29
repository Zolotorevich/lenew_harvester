"""
Crawlers:
    Business: https://www.forbes.ru/archive/biznes
    Finance: https://www.forbes.ru/archive/finansy
    Invest: https://www.forbes.ru/archive/investicii
    Corporate: https://www.forbes.ru/archive/novosti-kompaniy
"""

from crawlers.abstract import Crawler, News


class Forbes(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Forbes Parent Class'

    def collect(self, session) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session)

        # Find news
        news_container = soup.select('h3')

        for news in news_container:
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://www.forbes.ru' + news.parent.get('href'),
                'preview': news.parent.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))

class Business(Forbes):
    """economy: https://www.forbes.ru/archive/biznes"""
    
    category: str = 'economy'
    url: str = 'https://www.forbes.ru/archive/biznes'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Forbes Business'

class Finance(Forbes):
    """economy: https://www.forbes.ru/archive/finansy"""
    
    category: str = 'economy'
    url: str = 'https://www.forbes.ru/archive/finansy'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Forbes Finance'

class Invest(Forbes):
    """economy: https://www.forbes.ru/archive/investicii"""
    
    category: str = 'economy'
    url: str = 'https://www.forbes.ru/archive/investicii'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Forbes Invest'

class Corporate(Forbes):
    """economy: https://www.forbes.ru/archive/novosti-kompaniy"""
    
    category: str = 'economy'
    url: str = 'https://www.forbes.ru/archive/novosti-kompaniy'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Forbes Corporate'