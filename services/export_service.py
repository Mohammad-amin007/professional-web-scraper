import csv
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


                writer = csv.writer(file)


                writer.writerow(
                    [
                        "Title",
                        "Price"
                    ]
                )


                for book in books:

                    writer.writerow(
                        [
                            book.title,
                            book.price
                        ]
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

            data = []


            for book in books:

                data.append(
                    {
                        "Title": book.title,
                        "Price": book.price
                    }
                )


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