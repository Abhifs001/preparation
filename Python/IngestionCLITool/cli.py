import argparse

def get_args():
    parser = argparse.ArgumentParser(description="IPO Ingestion Tool")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("--csv", help="Output CSV file", default="summary.csv")
    parser.add_argument("--json", help="Output JSON file", default=None)
    return parser.parse_args()
