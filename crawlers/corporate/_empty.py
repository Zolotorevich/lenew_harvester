"""ORGANIZASTION

Crawlers:
    News: 
    Invest: 
"""

from crawlers.abstract import Crawler, News
from debug import debug


class News(Crawler):
    """News: """

    category: str = ''
    url: str = ''
    payload: list[News] = []

    def __str__(self) -> str:
        return ''

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)
        debug.dump_to_file(soup)
        
        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            # Find url
            url = news.parent.get('href')
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': url,
            }

            # Save result
            self.payload.append(News(**info))