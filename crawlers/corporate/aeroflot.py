"""Аэрофлот [AFLT]

Crawlers:
    News: https://www.aeroflot.ru/ru-ru/news
"""

from crawlers.abstract import Crawler, News
from crawlers.search.interfax import Search_Interfax
from debug import debug


class aeroflot(Crawler):
    """Parent class"""

    category: str = 'aeroflot'

    def __str__(self) -> str:
        return 'Аэрофлот Parent Class'

class All_News(aeroflot):
    """Аэрофлот: Новости"""

    url: str = 'https://www.aeroflot.ru/ru-ru/news'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Аэрофлот Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.selenium_and_parse_HTML(self.url)
        # soup = self.request_and_parse_HTML(self.url)

        debug.dump_to_file(soup)

        # Find news
        news_container = soup.select('h3')

        for news in news_container:

            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://mkb.ru' + news.parent.get('href'),
            }

            # Save result
            self.payload.append(News(**info))
            