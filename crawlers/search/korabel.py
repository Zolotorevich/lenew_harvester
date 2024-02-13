"""
Search crawler Korabel

NOTE: query = /company/{%query%}.html 
"""

from crawlers.abstract import Crawler, News
from debug import debug


class Search_Korabel(Crawler):
    """Parent class"""

    url: str = 'https://www.korabel.ru/catalogue/company/'

    def __str__(self) -> str:
        return 'Search Korabel Parent Class'

    def collect(self) -> None:
        # Generate SERP url
        serp_url = f'{self.url}{self.search_query}.html'
        
        # Get HTML
        soup = self.request_and_parse_HTML(serp_url)
    
        # Find news
        news_container = soup.select('.title_h2')

        for news in news_container:
            
            # Get info
            info = {
                'category': self.category,
                'title': news.get_text(),
                'url': news.get('href'),
            }

            # Save result
            self.payload.append(News(**info))