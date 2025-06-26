import csv
import logging

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        records = []
        try:
            with open(self.file_path, 'r',  encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        records.append({
                            "Company": row["Company"].strip(),
                            "Investor": row["Investor"].strip(),
                            "Quantity": int(row["Quantity"]),
                            "Price": float(row["Price"])
                        })
                    except Exception as e:
                        logging.warning(f"Skipping bad row: {row} | {e}")
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            raise
        return records
