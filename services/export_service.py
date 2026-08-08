import csv
import json
from pathlib import Path

import pandas as pd

from config import StorageConfig
from utils.logger import logger


class ExportService:

    def __init__(self):

        self.export_folder = Path(
            StorageConfig.EXPORT_FOLDER
        )

        self.export_folder.mkdir(
            parents=True,
            exist_ok=True
        )


    def _book_to_dict(
        self,
        book
    ):

        return {
            "title": book.title,
            "price": book.price,
            "availability": book.availability,
            "rating": book.rating,
            "product_url": book.product_url,
        }


    def export_csv(
        self,
        books
    ):

        file_path = (
            self.export_folder /
            "books.csv"
        )


        logger.info(
            f"Starting CSV export. Records: {len(books)}"
        )


        try:

            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:


                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "title",
                        "price",
                        "availability",
                        "rating",
                        "product_url",
                    ]
                )


                writer.writeheader()


                for book in books:

                    writer.writerow(
                        self._book_to_dict(book)
                    )


            logger.info(
                f"CSV exported successfully: {file_path}"
            )


            return file_path


        except Exception:

            logger.exception(
                "CSV export failed."
            )

            raise



    def export_excel(
        self,
        books
    ):


        file_path = (
            self.export_folder /
            "books.xlsx"
        )


        logger.info(
            f"Starting Excel export. Records: {len(books)}"
        )


        try:

            data = [
                self._book_to_dict(book)
                for book in books
            ]


            dataframe = pd.DataFrame(
                data
            )


            dataframe.to_excel(
                file_path,
                index=False
            )


            logger.info(
                f"Excel exported successfully: {file_path}"
            )


            return file_path


        except Exception:

            logger.exception(
                "Excel export failed."
            )

            raise



    def export_json(
        self,
        books
    ):

        file_path = (
            self.export_folder /
            "books.json"
        )


        logger.info(
            f"Starting JSON export. Records: {len(books)}"
        )


        try:

            data = [
                self._book_to_dict(book)
                for book in books
            ]


            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )


            logger.info(
                f"JSON exported successfully: {file_path}"
            )


            return file_path


        except Exception:

            logger.exception(
                "JSON export failed."
            )

            raise