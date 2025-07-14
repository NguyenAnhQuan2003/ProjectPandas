import logging
from config.paths import OUTPUT_LOGS

def setup_logging(
    log_file=OUTPUT_LOGS,
    level=logging.INFO,
    log_format='%(asctime)s - %(levelname)s - %(message)s'
):
    logging.basicConfig(
        filename=log_file,
        level=level,
        format=log_format,
        encoding='utf-8'
    )