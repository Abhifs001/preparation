# core/logger_config.py

import logging

def setup_logger(log_file="ipo_tool.log"):
    logging.basicConfig(
        filename=log_file,
        filemode='a',  # Append mode (or 'w' for overwrite)
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()
