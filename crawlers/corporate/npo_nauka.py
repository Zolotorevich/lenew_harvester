"""НПО Наука [NAUK]

Crawlers:
    News: https://npo-nauka.ru/press-centre/news/
"""

from crawlers.abstract import Crawler, News


class npo_nauka(Crawler):
    """Parent class"""

    category: str = 'npo_nauka'

    def __str__(self) -> str:
        return 'НПО Наука Parent Class'

class All_News(npo_nauka):
    """НПО Наука: Новости"""

    url: str = 'https://npo-nauka.ru/press-centre/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'НПО Наука Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('h3')

        for news in news_container:
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': 'https://npo-nauka.ru' + news.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))