import argparse
import asyncio

import requests

import connection
import logger
from crawlers.abstract import Crawler
from crawlers.factory import CrawlersFactory


async def main(crawlers_list: list[Crawler], dry_run: bool) -> None:

    logger.log(f'=== RUN START ===')
    affected_rows: int = 0

    with requests.Session() as session:
        for crawler in crawlers_list:
            affected_rows += await asyncio.to_thread(collect_and_save, *(crawler, session, dry_run))

    logger.log(f'=== {"DRY RUN" if dry_run else "RUN"} COMPLETE: +{affected_rows} ===\n\n')
    

def collect_and_save(crawler: Crawler, session: requests.Session, dry_run: bool) -> int:
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
        crawler.collect(session)
        
        if dry_run:
            # Print results
            for item in crawler.payload:
                print(f'\n{item}')
        else:
            # Write to database
            data = [item.__dict__ for item in crawler.payload]
            affected_rows = connection.write(data)

    except (ConnectionError, AttributeError, TimeoutError) as error:
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

    # Get objects from crawlers factory
    try:
        factory = CrawlersFactory()
        crawlers_list = factory.register(args.crawler)
    except AttributeError:
        print(f'FAIL: Category or crawler {args.crawler} not found')
        exit(1) 

    # Run main
    asyncio.run(main(crawlers_list, args.dry))