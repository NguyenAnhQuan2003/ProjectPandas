import pandas as pd
import logging
from logs.logging_config import setup_logging

setup_logging()

def load_tmdb_movies(path=str, **kwargs) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(path, **kwargs)
        logging.info("Đọc file thành công")
        return df
    except Exception as e:
        logging.exception("Lỗi đọc file csv")
        return None



