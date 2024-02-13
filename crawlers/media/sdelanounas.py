"""
Crawlers:
    Economy: https://sdelanounas.ru/blogs/
"""

from crawlers.abstract import Crawler, News


class sdelanounas(Crawler):
    """Parent class"""

    def __str__(self) -> str:
        return 'Сделано у нас Parent Class'

    def collect(self) -> None:
        # Get HTML
        soup = self.request_and_parse_HTML(self.url)

        # Find news
        news_container = soup.select('.title')

        for news in news_container:
            
            title = news.find('h2')

            info = {
                'category': self.category,
                'title': title.get_text(),
                'url': 'https://sdelanounas.ru' + title.find('a').get('href'),
            }

            # Save result
            self.payload.append(News(**info))

class All_News(sdelanounas):
    """economy: https://sdelanounas.ru/blogs/"""
    
    category: str = 'economy'
    url: str = 'https://sdelanounas.ru/blogs/'
    payload: list[News] = []

    def __str__(self) -> str:
        return 'Сделано у нас All News'