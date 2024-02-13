"""
Crawlers:
    Economy: https://infobrics.org/news/
"""

from crawlers.abstract import Crawler, News


class BRICS(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'BRICS Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

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

class All_News(BRICS):
    """economy: https://infobrics.org/news/"""
    
    category: str = 'economy'
    url: str = 'https://infobrics.org/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'BRICS All News'