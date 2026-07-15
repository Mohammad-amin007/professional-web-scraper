import asyncio

from apscheduler.schedulers.background import BackgroundScheduler

from app import run_pipeline

from utils.logger import logger


class ScraperScheduler:

    def __init__(self):

        self.scheduler = BackgroundScheduler()



    def run_job(self):

        logger.info(
            "Scheduled scraper execution started."
        )


        try:

            asyncio.run(
                run_pipeline()
            )


            logger.info(
                "Scheduled scraper execution completed."
            )


        except Exception:

            logger.exception(
                "Scheduled scraper execution failed."
            )



    def start(
        self,
        interval_minutes=60
    ):

        logger.info(
            f"Starting scheduler. Interval: {interval_minutes} minutes"
        )


        self.scheduler.add_job(
            self.run_job,
            "interval",
            minutes=interval_minutes,
            id="scraper_pipeline",
            replace_existing=True
        )


        self.scheduler.start()



    def shutdown(self):

        logger.info(
            "Scheduler shutting down."
        )


        self.scheduler.shutdown()