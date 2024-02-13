"""
Crawlers:
    Economy: https://e-cis.info/news/
"""

from crawlers.abstract import Crawler, News
from debug import debug


class CIS(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'СНГ Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        debug.dump_to_file(soup)

        # Find news
        news_container = soup.select('.news-short')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('span', class_='news-text').get_text(),
                'url': 'https://infobrics.org' + news.get('href'),
                'preview': news.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))

class All_News(CIS):
    """economy: https://e-cis.info/news/"""
    
    category: str = 'economy'
    url: str = 'https://e-cis.info/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'СНГ All News'