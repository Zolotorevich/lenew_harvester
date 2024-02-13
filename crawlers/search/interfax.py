# NOTE NOT WORKING!
"""
Search crawler Interfax
"""

from crawlers.abstract import Crawler, News


class Search_Interfax(Crawler):
    """Parent class"""

    url: str = 'https://www.interfax.ru/search/?df=08.02.2023&dt=13.02.2024&sec=0&phrase='

    def __str__(self) -> str:
        return 'Search Interfax Parent Class'

    def collect(self) -> None:
        # TODO Generate query

        
        # Get HTML
        soup = self.request_and_parse_HTML(self.url + self.search_query, 'windows-1251')
    
        # Find news
        news_container = soup.select('.timeline h3')

        for news in news_container:
            
            # Find url and check if it's relative
            url = news.parent.get('href')
            if url[:1] == '/':
                url = 'https://www.interfax.ru' + url
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': url,
            }

            # Save result
            self.payload.append(News(**info))