from src.load_csv import load_high_vote_csv
import logging
from logs.logging_config import setup_logging

setup_logging()
df = load_high_vote_csv()
def test_data_high_vote():
    try:
        df_high_vote_head = df['vote_average'].head(10)
        df_high_vote_tail = df['vote_average'].tail(10)
        logging.info(f"Head data: {df_high_vote_head}")
        logging.info(f'Tail data: {df_high_vote_tail}')
    except Exception:
        logging.exception("Lỗi phần test!")

if __name__ == '__main__':
    # test_data_high_vote()
    print(df.columns.tolist())
    # print(df['director'])
    print(df['genres'].head(10))
