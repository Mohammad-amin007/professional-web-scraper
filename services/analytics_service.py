from statistics import mean

from utils.logger import logger


class AnalyticsService:


    def get_total_books(self, books):

        logger.info(
            "Calculating total books."
        )

        try:

            total = len(books)

            logger.info(
                f"Total books: {total}"
            )

            return total


        except Exception:

            logger.exception(
                "Failed calculating total books."
            )

            raise



    def get_average_price(self, books):

        logger.info(
            "Calculating average price."
        )

        try:

            if not books:
                logger.warning(
                    "No books available for average calculation."
                )

                return 0


            prices = [
                book.price
                for book in books
            ]


            average = round(
                mean(prices),
                2
            )


            logger.info(
                f"Average price calculated: {average}"
            )


            return average


        except Exception:

            logger.exception(
                "Failed calculating average price."
            )

            raise



    def get_most_expensive_book(self, books):

        logger.info(
            "Finding most expensive book."
        )

        try:

            if not books:

                logger.warning(
                    "No books available."
                )

                return None


            book = max(
                books,
                key=lambda book: book.price
            )


            logger.info(
                f"Most expensive book: {book.title}"
            )


            return book


        except Exception:

            logger.exception(
                "Failed finding most expensive book."
            )

            raise



    def get_cheapest_book(self, books):

        logger.info(
            "Finding cheapest book."
        )

        try:

            if not books:

                logger.warning(
                    "No books available."
                )

                return None


            book = min(
                books,
                key=lambda book: book.price
            )


            logger.info(
                f"Cheapest book: {book.title}"
            )


            return book


        except Exception:

            logger.exception(
                "Failed finding cheapest book."
            )

            raise



    def get_top_expensive_books(
        self,
        books,
        limit=5
    ):

        logger.info(
            f"Getting top {limit} expensive books."
        )

        try:

            result = sorted(
                books,
                key=lambda book: book.price,
                reverse=True
            )[:limit]


            logger.info(
                f"Top expensive books generated: {len(result)}"
            )


            return result


        except Exception:

            logger.exception(
                "Failed generating top expensive books."
            )

            raise