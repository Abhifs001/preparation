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
   


# # ------------------------------------------------------------------------------------------------------------------------
# # 📄 IPO Ingestion Script – Interview Q&A (Markdown Format)

# ## 🔧 Python & File Handling

# ### 1. What is `csv.DictReader` and why did you use it instead of `csv.reader`?
# ```python
# # csv.DictReader returns each row as a dictionary with headers as keys.
# row['Company']  # More readable and safer than row[0]
# ```

# ### 2. How does your script handle bad/malformed rows in the CSV file?
# ```python
# try:
#     quantity = int(row["Quantity"])
#     ...
# except Exception as e:
#     logging.warning(f"Invalid row skipped: {row} | Error: {e}")
# ```
# This prevents crashing and logs the issue.

# ### 3. Why did you wrap file operations in `try-except` blocks?
# ```python
# try:
#     with open(file_path, 'r') as f:
#         ...
# except FileNotFoundError:
#     logging.error(f"File not found: {file_path}")
# ```
# To gracefully handle file errors and log them.

# ### 4. What is the purpose of `newline=''` when opening a file for writing CSV?
# ```python
# with open('output.csv', 'w', newline='') as f:
#     ...
# ```
# Prevents extra blank lines on Windows.

# ### 5. How would your script behave if the input CSV file is empty or missing headers?
# ```python
# # If headers are missing, DictReader will return wrong keys or None.
# # Accessing row['Company'] will raise a KeyError.
# ```

# ### 6. What's the difference between `logging.info()` and `print()`?
# - `print()` outputs to the console.
# - `logging.info()` logs to a file with timestamps and severity levels.

# ### 7. Why is `with open(...) as f:` preferred?
# ```python
# with open("data.csv") as f:
#     ...
# # Ensures file is auto-closed even if an exception occurs.
# ```

# ---

# ## 🧠 Python Concepts & Best Practices

# ### 8. What happens if a required argument is not passed to the script?
# ```bash
# python script.py  # argparse raises error and prints usage
# ```

# ### 9. Why did you use `defaultdict(float)`?
# ```python
# from collections import defaultdict
# summary = defaultdict(float)
# summary["TCS"] += 1000.0  # No need to check if key exists
# ```

# ### 10. Difference between `writerow()` and `writerows()`?
# ```python
# writer.writerow([company, price])  # Single row
# writer.writerows(list_of_rows)    # Multiple rows
# ```

# ### 11. How to extend the script for multiple files?
# ```python
# import os
# for file in os.listdir("Data"):
#     if file.endswith(".csv"):
#         read_file(os.path.join("Data", file))
# ```

# ---

# ## ⚙️ CLI and Automation

# ### 12. Why positional arguments over optional flags?
# ```python
# parser.add_argument("inputfile")  # Required
# parser.add_argument("--csv")      # Optional with default
# ```

# ### 13. How to add a timestamp to filenames?
# ```python
# from datetime import datetime
# filename = f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
# ```

# ### 14. How to make the script a reusable module?
# ```python
# # Wrap logic in functions
# if __name__ == "__main__":
#     main()  # Only runs CLI when script is executed directly
# ```

# ---

# ## 🛡️ Error Handling and Logging

# ### 15. What errors are logged?
# ```python
# logging.error("File not found")
# logging.warning("Invalid row skipped")
# logging.info("Ingestion completed")
# ```

# ### 16. How to handle duplicate rows or missing values?
# ```python
# seen = set()
# if (row["Company"], row["Investor"]) not in seen:
#     seen.add((row["Company"], row["Investor"]))
#     ...
# ```

# ### 17. Purpose of `logging.basicConfig()`?
# ```python
# logging.basicConfig(
#     filename="logfile.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# ```
# Ensures consistent and persistent logging.

# ---

# ## 🔁 Data Engineering / Business Logic

# ### 18. How does the summary logic work?
# ```python
# summary[row["Company"]] += row["Price"]
# # Alternatively: row["Quantity"] * row["Price"]
# ```

# ### 19. How to group by Investor instead of Company?
# ```python
# summary[row["Investor"]] += row["Price"]
# ```

# ### 20. How to optimize for large files (millions of rows)?
# ```python
# # Stream data instead of storing all rows
# with open(file) as f:
#     for row in csv.DictReader(f):
#         process(row)
# ```
# Or use pandas with `chunksize`:
# ```python
# pd.read_csv("file.csv", chunksize=10000)
# ```

# ---
