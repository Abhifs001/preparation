import csv 
import argparse
import logging
import json 
from collections import defaultdict
from datetime import datetime

#-------------variable declaration-----------------
#file_name = './Data/ipo.csv'

#--------------------------Logging Configuration--------------------------
logging.basicConfig(
    filename  = 'file_handling.log',
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
) 
#---------------------------READING FILE --------------------------
def read_file(file_path):
    records=[] 

    try: 
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    company = row['Company']
                    investor = row['Investor']
                    quantity = row['Quantity']
                    price  =  float(row['Price'])
                    records.append({
                        'Company': company,
                        'Investor': investor,
                        'Quantity': quantity,
                        'Price': price
                    })
                except Exception as e:
                    logging.warning(f"Invalid row skipped: {row} | Error: {e}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise

    return records

#-------------------------------------summarize function--------------------------

def summarize_ipo_data(records):
    summary = defaultdict(float)
    for row in records:
        summary[row['Company']] += row['Price']
    return summary

#------------------------------------CSV summary 

def write_summary_to_csv(summary, output_path):
    with open(output_path, 'w', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(['Company', 'Total Price'])
        for company, total_price in summary.items():
            writer.writerow([company, round(total_price, 2)])
        logging.info(f"Summary written to {output_path}")

#------------------------------------JSON summary--------------------------
def write_summary_to_json(summary, output_path):
    with open(output_path, 'w') as jsonfile:
        json.dump(summary, jsonfile, indent=4)
        logging.info(f"Summary written to {output_path}")

#------------------------------------Main function--------------------------
def main():
    try:
        parser = argparse.ArgumentParser(description="Process IPO data from a CSV file.")
        parser.add_argument("inputfile", help="Path to the input CSV file")
        parser.add_argument("csv", help="Path to the output CSV file")
        parser.add_argument("json", help="path to output json file ")


        args = parser.parse_args()

        logging.info(f"------------------------Ingesting file {args.inputfile}------------------------")

        records  = read_file(args.inputfile)
        summary = summarize_ipo_data(records)
        write_summary_to_csv(summary, args.csv)

        if args.json:
            write_summary_to_json(summary, args.json)
        
        
        logging.info("--- IPO Ingestion Completed ---")
        print(f"Summary written to {args.csv}")
    except FileNotFoundError as e:
        logging.error(f"File not found: {args.inputfile}")
        return

if __name__ == "__main__":
    main()
   
