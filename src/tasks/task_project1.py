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

def get_top_director(df):
    try:
        director_counts = df['director'].value_counts()
        top_director = director_counts.idxmax()
        top_director_count = director_counts.max()
        return top_director, top_director_count
    except Exception:
        logging.exception("Lỗi get_top_director!")

def get_top_cast(df):
    try:
        cast_series = df['cast'].dropna()
        exploded_cast = cast_series.str.split('|').explode()
        actor_counts = exploded_cast.value_counts()
        top_actor = actor_counts.idxmax()
        top_actor_count = actor_counts.max()
        return top_actor, top_actor_count
    except Exception:
        logging.exception("Lỗi get_top_cast!")

def get_director_cast(df):
    try:
        director, top_director = get_top_director(df)
        cast, top_cast = get_top_cast(df)
        with open(f'{OUTPUT_DIR}/top_director_cast.txt', 'w', encoding='utf-8') as f:
            f.write("[director]\n")
            f.write(f'Đạo diễn: {director} có tổng {top_director} bộ phim,'
                    f' được vinh danh là đạo diễn có nhiều bộ phim nhất\n')
            f.write("[cast]\n")
            f.write(f'Diễn viên: {cast} đã đóng {top_cast} bộ phim,'
                    f' được vinh danh là diễn viên có nhiều bộ phim nhất\n')
    except Exception:
        logging.exception("Lỗi ghi đạo diễn và diễn viên!")

def get_genres(df):
    try:
        genre_series = df["genres"].dropna()
        exploded_genres = genre_series.str.split("|").explode()
        genre_counts = exploded_genres.value_counts()
        with open(f'{OUTPUT_DIR}/genres.txt', 'w', encoding='utf-8') as f:
            f.write("[genres]\n")
            for genre, count in genre_counts.items():
                f.write(f"{genre}: {count} phim\n")
    except Exception:
        logging.exception("Lỗi get_genres!")