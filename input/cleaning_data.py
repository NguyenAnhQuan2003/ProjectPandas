from input.reading_data import load_tmdb_movies
import pandas as pd
import logging
from logs.logging_config import setup_logging

setup_logging()

def is_datetime(df, column: str):
    try:
        df[column] = pd.to_datetime(
            df[column],
            format='%m/%d/%y',
            errors='coerce'
        )
        logging.info("Success format datetime")
        return df
    except Exception:
        logging.exception("Error clean format datetime!")

def is_numeric(df, column: str):
    try:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        logging.info("Success format numeric")
        return df
    except Exception:
        logging.exception("Error clean format numeric!")