import argparse
import asyncio

import connection
import logger
from crawlers.abstract import Crawler
from crawlers.factory import CrawlersFactory


async def main(crawlers_list: list[Crawler], dry_run: bool) -> None:

    affected_rows: int = 0

    for crawler in crawlers_list:
        affected_rows += await asyncio.to_thread(collect_and_save, *(crawler, dry_run))

    if dry_run:
        logger.log(f'Dry run: +{affected_rows}')
    else:
        logger.log(f'Run: +{affected_rows}')

def collect_and_save(crawler: Crawler, dry_run: bool) -> int:
    """Launch crawlers and save data

    Args:
        crawler: Crawler object
        dry_run: don't write to DB

    Returns:
        Number of affected rows
    """

    affected_rows: int = 0
    
    try:
        # Run crawler
        crawler.collect()

        if dry_run:
            # Print results
            for item in crawler.payload:
                print(f'\n{item}')
        else:
            # Write to database
            data = [item.__dict__ for item in crawler.payload]
            affected_rows = connection.write(data)
            logger.log(f'{crawler} +{affected_rows}')

    except (ConnectionError, AttributeError, TimeoutError) as error:
            logger.log(f'[ERROR] {crawler}: {error}')

    return affected_rows

if __name__ == "__main__":

    # Check CLI flags
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--crawler", dest="crawler", required=True,
                        help="Category or crawler name")

    parser.add_argument("-d", "--dry", dest="dry", action='store_true',
                        help="Don't write to database")
    
    args = parser.parse_args()

    # Get objects from crawlers factory
    factory = CrawlersFactory()
    crawlers_list = factory.register(args.crawler)

    asyncio.run(main(crawlers_list, args.dry))