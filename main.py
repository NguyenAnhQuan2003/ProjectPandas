import logging
from logs.logging_config import setup_logging
from src.tasks.task_project1 import sort_by_release_date, high_vote
from src.load_csv import load_csv
setup_logging()
def main():
    try:
        df = load_csv()
        sort_by_release_date(df)
        high_vote(df)
    except Exception:
        logging.exception("Lỗi chạy main!")

if __name__ == "__main__":
    main()