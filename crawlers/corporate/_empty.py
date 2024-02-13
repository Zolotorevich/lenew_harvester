"""Henderson [HNFG]

Crawlers:
    News: 
"""

from crawlers.abstract import Crawler, News
from debug import debug


class utair(Crawler):
    """Parent class"""

    category: str = 'henderson'

    def __str__(self) -> str:
        return 'Henderson Parent Class'

class All_News(utair):
    """Henderson: Новости"""

    url: str = ''
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Henderson Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)
        # soup = self.selenium_and_parse_HTML(self.url)
        
        debug.dump_to_file(soup)

        # Find news
        news_container = soup.select('.hotnews-body')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://www.utair.ru' + news.find('a').get('href'),
                'preview': news.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))