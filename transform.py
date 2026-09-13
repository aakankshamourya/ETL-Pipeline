import pandas as pd


def transform_books(df):

    # Make a copy so the original raw data is not modified
    df = df.copy()

    # --------------------------------------------------
    # 1. Clean column names
    # --------------------------------------------------

    df.columns = df.columns.str.strip().str.lower()

    # --------------------------------------------------
    # 2. Clean book titles
    # --------------------------------------------------

    df["book_title"] = (
        df["book_title"]
        .astype("string")
        .str.strip()
    )

    # --------------------------------------------------
    # 3. Clean author names
    # --------------------------------------------------

    df["author"] = (
        df["author"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # --------------------------------------------------
    # 4. Standardize genre
    # --------------------------------------------------

    df["genre"] = (
        df["genre"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    genre_mapping = {
        "fantasy": "Fantasy",
        "horror & thriller": "Horror & Thriller",
        "horror-thriller": "Horror & Thriller",
        "sci-fi": "Sci-Fi",
        "scifi": "Sci-Fi",
        "historical fiction": "Historical Fiction",
        "romance": "Romance"
    }

    df["genre"] = df["genre"].replace(genre_mapping)

    # --------------------------------------------------
    # 5. Clean page count
    # --------------------------------------------------

    df["page_count"] = pd.to_numeric(
        df["page_count"],
        errors="coerce"
    )

    # Use nullable integer type
    df["page_count"] = df["page_count"].astype("Int64")

    # --------------------------------------------------
    # 6. Clean rating
    # --------------------------------------------------

    df["my_rating"] = pd.to_numeric(
        df["my_rating"],
        errors="coerce"
    )

    # Ratings must be between 0 and 5
    df.loc[
        ~df["my_rating"].between(0, 5),
        "my_rating"
    ] = pd.NA

    # --------------------------------------------------
    # 7. Clean read date
    # --------------------------------------------------

    df["read_date"] = (
        df["read_date"]
        .astype("string")
        .str.strip()
        .str.replace(".", "-", regex=False)
        .str.replace("/", "-", regex=False)
    )

    # Convert to datetime
    df["read_date"] = pd.to_datetime(
        df["read_date"],
        format="%Y-%m",
        errors="coerce"
    )

    # --------------------------------------------------
    # 8. Standardize format
    # --------------------------------------------------

    df["format"] = (
        df["format"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    format_mapping = {
        "physical": "Physical",
        "kindle": "Kindle",
        "digital": "Digital",
        "e-book": "Digital"
    }

    df["format"] = df["format"].replace(format_mapping)

    # --------------------------------------------------
    # 9. Remove duplicate books
    # --------------------------------------------------

    df = df.drop_duplicates(
        subset=["book_title", "author"],
        keep="first"
    )

    return df


if __name__ == "__main__":

    file_path = (
        r"C:\Users\aakan\Downloads\ETL Pipeline"
        r"\Data\dirty_books_2026.csv"
    )

    # EXTRACT
    df = pd.read_csv(file_path)

    print("========== RAW DATA ==========")
    print(df)

    print("\nRaw shape:", df.shape)

    # TRANSFORM
    cleaned_df = transform_books(df)

    print("\n========== CLEANED DATA ==========")
    print(cleaned_df)

    print("\nCleaned shape:", cleaned_df.shape)

    print("\n========== MISSING VALUES ==========")
    print(cleaned_df.isnull().sum())