import csv
import json
import logging

class Writer:
    @staticmethod
    def to_csv(summary, path):
        with open(path, 'w', newline='', encoding= 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Total Investment (₹)"])
            for company, total in summary.items():
                writer.writerow([company, round(total, 2)])
        logging.info(f"CSV written: {path}")

    @staticmethod
    def to_json(summary, path):
        with open(path, 'w' , encoding='utf-8') as file:
            json.dump(summary, file, indent=4)
        logging.info(f"JSON written: {path}")
