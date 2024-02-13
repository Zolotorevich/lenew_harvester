"""Crawlers factory"""

import importlib

from crawlers.abstract import Crawler


class CrawlersFactory():
    """Factory for Crawler objects

    Methods:
        get_crawler: generate one crawler by category and name
        register: generate list of crawlers by category or search by name
    """

    media = [
            'cbr.All_News',
            'forbes.Business',
            'forbes.Corporate',
            'forbes.Finance',
            'forbes.Invest',
            'interfax.Main',
            'interfax.Economy',
            'kommersant.Business',
            'kommersant.Finance',
            'kommersant.Market',
            'kommersant.Economy',
            'minfin.All_News',
            'prime1.Business',
            'prime1.Economy',
            'prime1.Finance',
            'prime1.Fin_market',
            'prime1.IT',
            'prime1.Energy',
            'rbc.Business',
            'rbc.Economics',
            'rbc.Finances',
            'tass.Economy',
            'tass.National_projects',
            'tass.Real_estate',
            'tass.Small_business',
            'tass.Politics',
            'tass.World',
            'tass.Society',
            'tass.Country',
        ]

    corporate = [
            'mkb.All_News',
            'utair.All_News',
            'henderson.All_News',
            'viborgsky_sudzavod.All_News',
            'viborgsky_sudzavod.Korabel',
            'mechel.All_News',
            'fesco.All_News',
        ]
    

    def get_crawler(self, category: str, name: str) -> Crawler:
        """Generate one crawler

        Args:
            category: aka module directory
            name: filename.Class

        Returns:
            One crawler object
        """

        # Get module and class names
        moduleName = name[:name.find('.')]
        className = name[name.find('.') + 1:]

        # Find crawler
        module = importlib.import_module(f'crawlers.{category}.{moduleName}')
        requested_crawler = getattr(module, className)

        return requested_crawler()

    def register(self, category: str) -> list[Crawler]:
        """Generate crawlers by category

        Args:
            crawler: category or crawler full name, e.g. directory.file.Class

        Returns:
            List with Crawler objects

        Raises:
            AttributeError: category or crawler not found
            ModuleNotFoundError: category or crawler not found
        """

        if category == 'all':
            media = [self.get_crawler('media', crawler) for crawler in self.media]
            corporate = [self.get_crawler('corporate', crawler) for crawler in self.corporate]
            return media + corporate
            
        elif category == 'media':
            return [self.get_crawler('media', crawler) for crawler in self.media]

        elif category == 'corporate':
            return [self.get_crawler('corporate', crawler) for crawler in self.corporate]

        else:
            # Find crawler by name
            crawler_category = category[:category.find('.')]
            crawler_name = category[category.find('.') + 1:]
            return [self.get_crawler(crawler_category, crawler_name)]