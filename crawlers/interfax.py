"""
Crawlers:
    Economy: https://www.interfax.ru/digital/
"""

from crawlers.abstract import Crawler, News


class Economy(Crawler):
    category: str = 'economy'
    url: str = 'https://www.interfax.ru/digital/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Interfax Economy'

    def collect(self, session) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url, session, 'windows-1251')

        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            # Find url
            url = news.parent.get('href')
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://www.interfax.ru' + url,
            }

            # Save result
            self.payload.append(News(**info))

# TODO Class for search results