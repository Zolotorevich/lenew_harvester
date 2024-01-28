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

        debug.dump_to_file(soup, terminate=True)

        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            # Find url
            url = news.parent.get('href')
            
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