from input.reading_data import load_tmdb_movies
import pandas as pd
import logging
from logs.logging_config import setup_logging

setup_logging()

def is_datetime(df):
    try:
        df['release_date'] = pd.to_datetime(
            df['release_date'],
            format='%m/%d/%y',
            errors='coerce'
        )
        logging.info("Success format datetime")
        return df
    except Exception:
        logging.exception("Error clean format datetime!")

def is_numeric(df):
    try:
        df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
        logging.info("Success format numeric")
        return df
    except Exception:
        logging.exception("Error clean format numeric!")