from src.load_csv import load_csv
from input.cleaning_data import is_datetime, is_numeric
from config.paths import OUTPUT_DIR
from logs.logging_config import setup_logging
import logging


setup_logging()
df = load_csv()

def sort_by_release_date(df):
    try:
        is_datetime(df, 'release_date')
        df_sorted = df.sort_values(by='release_date', ascending=False)
        df_sorted.to_csv(f'{OUTPUT_DIR}/sort_by_release_date.csv', index=False)
        logging.info("Sorting by release date successful!")
        return df_sorted
    except Exception:
        logging.exception("Lỗi sắp xếp ngày!")

def high_vote(df):
    try:
        is_numeric(df, 'vote_average')
        df_votes = df[df['vote_average'] >= 7.5]
        df_votes.to_csv(f'{OUTPUT_DIR}/high_vote.csv', index=False)
        logging.info("High vote successful!")
        return None
    except Exception:
        logging.exception("Lỗi vote_avg không phải số!")

def revenue_max_min(df):
    try:
        is_numeric(df, 'revenue')
        revenue_min = df['revenue'].min()
        revenue_max = df['revenue'].max()
        with open(f'{OUTPUT_DIR}/revenue_max_min.txt', 'w' ,encoding='utf-8') as f:
            f.write("[revenue]\n")
            f.write(f"Doanh thu bộ phim thấp nhất là: {revenue_min}\n")
            f.write(f"Doanh thu bộ phim cao nhất là: {revenue_max}\n")
    except Exception:
        logging.exception("Lỗi revenue_max_min!")

def sum_revenue(df):
    try:
        is_numeric(df, 'revenue')
        revenue_sum = df['revenue'].sum()
        with open(f'{OUTPUT_DIR}/revenue_sum.txt', 'w', encoding='utf-8') as f:
            f.write("[sum revenue]\n")
            f.write(f"Tổng doanh thu của các bộ phim là: {revenue_sum}\n")
    except Exception:
        logging.exception("Lỗi sum_revenue!")

def revenue_top(df):
    try:
        is_numeric(df, 'revenue')
        revenue_top = df.nlargest(10,'revenue')[['original_title', 'revenue']]
        with open(f'{OUTPUT_DIR}/revenue_top.txt', 'w', encoding='utf-8') as f:
            f.write("[top 10 revenue]\n")
            f.write(f'Top 10 bộ phim có doanh thu cao nhất: {revenue_top}\n')
    except Exception:
        logging.exception("Lỗi revenue_top!")