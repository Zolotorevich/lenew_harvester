"""Sollers [SVAV]

Crawlers:
    News: https://sollers-auto.com/press-center/news/
"""

from crawlers.abstract import Crawler, News


class sollers(Crawler):
    """Parent class"""

    category: str = 'sollers'

    def __str__(self) -> str:
        return 'Sollers Parent Class'

class All_News(sollers):
    """Sollers: Новости"""

    url: str = 'https://sollers-auto.com/press-center/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Sollers Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.news-item__content')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.find('a').get_text(),
                'url': 'https://sollers-auto.com' + news.find('a').get('href'),
                'preview': news.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))