from src.load_csv import load_csv
from input.cleaning_data import is_datetime, is_numeric
from config.paths import OUTPUT_DIR
from logs.logging_config import setup_logging
import logging


setup_logging()
df = load_csv()
is_datetime(df)
is_numeric(df)

def sort_by_release_date(df):
    try:
        df_sorted = df.sort_values(by='release_date', ascending=False)
        df_sorted.to_csv(f'{OUTPUT_DIR}/sort_by_release_date.csv', index=False)
        logging.info("Sorting by release date successful!")
        return df_sorted
    except Exception:
        logging.exception("Lỗi sắp xếp ngày!")

def high_vote(df):
    try:
        df_votes = df[df['vote_average'] >= 7.5]
        df_votes.to_csv(f'{OUTPUT_DIR}/high_vote.csv', index=False)
        logging.info("High vote successful!")
        return None
    except Exception:
        logging.exception("Lỗi vote_avg không phải số!")
