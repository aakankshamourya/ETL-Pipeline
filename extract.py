import pandas as pd


FILE_PATH = r"C:\Users\aakan\Downloads\ETL Pipeline\Data\dirty_books_2026.csv"


def extract_books():
    """Read raw book data from CSV."""
    df = pd.read_csv(FILE_PATH)
    return df


if __name__ == "__main__":
    df = extract_books()

    print("========== EXTRACTED DATA ==========")
    print(df.head())

    print("\nNumber of rows:", len(df))
    print("Number of columns:", len(df.columns))
    print("Shape:", df.shape)