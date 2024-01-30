"""Crawlers factory"""

import importlib

from crawlers import forbes, interfax, kommersant, prime1, rbc, tass
from crawlers.abstract import Crawler
from crawlers.corporate import mkb


class CrawlersFactory():
    """Factory for Crawler objects

    Methods:
        register: generate crawlers by name or category
    """

    def register(self, crawler: str) -> list[Crawler]:
        """Generate crawlers

        Args:
            crawler: crawler or category name

        Returns:
            List with Crawler objects

        Raises:
            AttributeError: category or crawler not found
            ModuleNotFoundError: category or crawler not found
        """

        if crawler == 'all':
            return [
                    forbes.Business(),
                    forbes.Corporate(),
                    forbes.Finance(),
                    forbes.Invest(),
                    interfax.Main(),
                    interfax.Economy(),
                    kommersant.Business(),
                    kommersant.Finance(),
                    kommersant.Market(),
                    kommersant.Economy(),
                    prime1.Business(),
                    prime1.Economy(),
                    prime1.Finance(),
                    prime1.Fin_market(),
                    prime1.IT(),
                    prime1.Energy(),
                    rbc.Business(),
                    rbc.Economics(),
                    rbc.Finances(),
                    tass.Economy(),
                    tass.National_projects(),
                    tass.Real_estate(),
                    tass.Small_business(),
                    tass.Politics(),
                    tass.World(),
                    tass.Society(),
                    tass.Country(),
                    ]

        elif crawler == 'test':
            return [
                    mkb.News(),
                    ]

        else:
            # Find crawler by name
            moduleName = crawler[:crawler.find('.')]
            className = crawler[crawler.find('.') + 1:]

            module = importlib.import_module('crawlers.' + moduleName)
            requested_crawler = getattr(module, className)

            return [requested_crawler()]