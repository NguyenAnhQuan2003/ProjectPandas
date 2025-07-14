import logging

from logs.logging_config import setup_logging
from input.reading_data import load_tmdb_movies
from config.paths import OUTPUT_DIR, INPUT_DIR
setup_logging()

def load_csv():
    try:
        df = load_tmdb_movies(
            INPUT_DIR,
            quotechar='"',
            encoding="utf-8",
            on_bad_lines="warn",
            low_memory=False)
        return df
    except Exception as e:
        logging.exception("Error loading csv by Sort_by_Release_date!")