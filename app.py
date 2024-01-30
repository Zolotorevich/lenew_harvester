import argparse
import asyncio
from time import perf_counter

import requests

import connection
import logger
from crawlers.abstract import Crawler
from crawlers.factory import CrawlersFactory


async def main(crawlers_list: list[Crawler], dry_run: bool) -> None:

    time_start = perf_counter()

    # Launch crawlers
    affected_rows = await asyncio.gather(
        *(collect_and_save(crawler, dry_run) for crawler in crawlers_list)
        )

    # Log results
    elapsed_time = perf_counter() - time_start
    logger.log(f'=== {"Dry run" if dry_run else "Run"} complete, '
               f'+{sum(affected_rows)} in {round(elapsed_time, 2)} sec ===\n\n')


async def collect_and_save(crawler: Crawler, dry_run: bool) -> int:
    """Launch crawlers and save data

    Args:
        crawler: Crawler object
        dry_run: print results and don't write them to DB

    Returns:
        Number of affected rows or would have been affected if not dry_run
    """

    affected_rows: int = 0

    try:
        # Run crawler
        await asyncio.to_thread(crawler.collect)
        
        if dry_run:
            # Print results
            print(*crawler.payload, sep='\n\n')
            affected_rows = len(crawler.payload)
        else:
            # Write to database
            data = [item.__dict__ for item in crawler.payload]
            affected_rows = connection.write(data)

        # Log results
        logger.log(f'{crawler} +{affected_rows}')

    except (AttributeError, TimeoutError, ConnectionError,
            requests.ReadTimeout, requests.ConnectionError) as error:
            logger.log(f'[ERROR] {crawler}: {error}')

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