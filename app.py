import argparse
import asyncio

import requests

import connection
import logger
from crawlers.abstract import Crawler
from crawlers.factory import CrawlersFactory


async def main(crawlers_list: list[Crawler], dry_run: bool) -> None:

    with requests.Session() as session:
        affected_rows = await asyncio.gather(
            *[collect_and_save(crawler, session, dry_run) for crawler in crawlers_list]
            )
            
    logger.log(f'=== {"Dry run" if dry_run else "Run"} complete, +{sum(affected_rows)} ===\n\n')


async def collect_and_save(crawler: Crawler, session: requests.Session, dry_run: bool) -> int:
    """Launch crawlers and save data

    Args:
        crawler: Crawler object
        dry_run: print results and don't write to DB

    Returns:
        Number of affected rows
    """

    affected_rows: int = 0

    try:
        # Run crawler
        await asyncio.to_thread(crawler.collect, session)
        
        if dry_run:
            # Print results
            for item in crawler.payload:
                print(f'\n{item}')
        else:
            # Write to database
            data = [item.__dict__ for item in crawler.payload]
            affected_rows = connection.write(data)

    except (ConnectionError, AttributeError, TimeoutError,
            requests.ReadTimeout, requests.ConnectionError) as error:
            logger.log(f'[ERROR] {crawler}: {error}')

    logger.log(f'{crawler} +{affected_rows}')
    return affected_rows

if __name__ == "__main__":

    # Get CLI flags
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--crawler", dest="crawler", required=True,
                        help="Category or crawler name")

    parser.add_argument("-d", "--dry", dest="dry", action='store_true',
                        help="Don't write to database")
    
    args = parser.parse_args()

    # Get crawlers from factory
    try:
        factory = CrawlersFactory()
        crawlers_list = factory.register(args.crawler)
    except (AttributeError, ModuleNotFoundError):
        print(f'FAIL: Category or crawler {args.crawler} not found')
        exit(1)

    # Run main
    logger.log(f'=== {args.crawler} ===')
    asyncio.run(main(crawlers_list, args.dry))