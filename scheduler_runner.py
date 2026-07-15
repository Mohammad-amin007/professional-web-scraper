from scheduler.scraper_scheduler import ScraperScheduler

from config import SchedulerConfig

from utils.logger import logger

import time



def main():

    scheduler = ScraperScheduler()


    scheduler.start(
        interval_minutes=(
            SchedulerConfig.INTERVAL_MINUTES
        )
    )


    logger.info(
        "Scheduler is running..."
    )


    try:

        while True:

            time.sleep(10)


    except KeyboardInterrupt:

        scheduler.shutdown()



if __name__ == "__main__":

    main()