import csv
from pathlib import Path

import pandas as pd


class ExportService:

    def __init__(self, export_folder="exports"):
        self.export_folder = Path(export_folder)
        self.export_folder.mkdir(
            exist_ok=True
        )


    def export_csv(self, books):

        file_path = self.export_folder / "books.csv"

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

        return file_path


    def export_excel(self, books):

        file_path = self.export_folder / "books.xlsx"

        data = []

        for book in books:
            data.append(
                {
                    "Title": book.title,
                    "Price": book.price
                }
            )


        dataframe = pd.DataFrame(data)

        dataframe.to_excel(
            file_path,
            index=False
        )

        return file_path