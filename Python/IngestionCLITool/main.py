# main.py

from core.logger_config import setup_logger
from cli import get_args
from core.file_reader import FileReader
from core.summarizer import Summarizer
from core.writer import Writer

logger = setup_logger()  # Initialize log file before anything else

def main():
    args = get_args()
    logger.info("IPO Ingestion Started")

    try:
        logger.info(f"Reading input file: {args.input}")
        reader = FileReader(args.input)
        logger.info("Reading records from file" )
        records = reader.read()
        logger.info(f"Total records read: {len(records)}")

        summary = Summarizer.summarize(records)
  
        logger.info("Summarization completed")

        logger.info(f"Writing summary to CSV: {args.csv}")
        Writer.to_csv(summary, args.csv)

        logger.info("CSV writing completed")


        logger.info("Writing summary to JSON")
        if args.json:
            Writer.to_json(summary, args.json)

        logger.info("IPO Ingestion Completed Successfully")
        print(f"CSV written to: {args.csv}")
        if args.json:
            print(f"JSON written to: {args.json}")
    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        print("Ingestion failed. Check logs.")

if __name__ == "__main__":
    main()
