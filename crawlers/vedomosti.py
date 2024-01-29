"""
Crawlers:
    Economy:
"""

from crawlers.abstract import Crawler, News
from debug import debug


class Vedomosti(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Vedomosti Parent Class'

    def collect(self, session) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session)
        debug.dump_to_file(soup)

        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            url = news.parent.get('href')
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': url,
            }

            # Save result
            self.payload.append(News(**info))

class Economy(Vedomosti):
    """economy: """
    
    category: str = 'economy'
    url: str = ''
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Vedomosti '