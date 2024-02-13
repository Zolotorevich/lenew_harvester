"""ЮТэйр [UTAR]

Crawlers:
    News: https://www.utair.ru/about/news/
"""

from crawlers.abstract import Crawler, News


class utair(Crawler):
    """Parent class"""

    category: str = 'utair'

    def __str__(self) -> str:
        return 'ЮТэйр Parent Class'

class All_News(utair):
    """ЮТэйр: Новости"""

    url: str = 'https://www.utair.ru/about/news/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'ЮТэйр Новости'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.hotnews-body')

        for news in news_container:


            title = news.find('div', class_='hotnews-head')
            preview = news.find('div', class_='hotnews-text')

            # Get info
            info = {
                'category': self.category,
                'title': title.get_text().strip(),
                'url': 'https://www.utair.ru' + title.find('a').get('href'),
                'preview': preview.find('p').get_text(),
            }

            # Save result
            self.payload.append(News(**info))