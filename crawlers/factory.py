"""Crawlers factory"""

import importlib

from crawlers import interfax, tass
from crawlers.abstract import Crawler


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
                    interfax.Main(),
                    interfax.Economy(),
                    tass.Economy(),
                    tass.National_projects(),
                    tass.Real_estate(),
                    tass.Small_business(),
                    tass.Politics(),
                    tass.World(),
                    tass.Society(),
                    tass.Country(),
                    ]

        else:
            # Find crawler by name
            moduleName = crawler[:crawler.find('.')]
            className = crawler[crawler.find('.') + 1:]

            module = importlib.import_module('crawlers.' + moduleName)
            requested_crawler = getattr(module, className)

            return [requested_crawler()]