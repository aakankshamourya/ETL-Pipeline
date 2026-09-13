import pandas as pd


def validate_books(df):

    errors = []

    # 1. Check required columns
    required_columns = [
        "book_title",
        "author",
        "genre",
        "page_count",
        "read_date",
        "my_rating",
        "format"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing columns: {missing_columns}"
        )

    # Stop validation if required columns are missing
    if missing_columns:
        print("❌ VALIDATION FAILED")

        for error in errors:
            print("-", error)

        return False

    # 2. Check book title
    if df["book_title"].isnull().any():
        errors.append("Some book titles are missing")

    # 3. Check author
    if df["author"].isnull().any():
        errors.append("Some authors are missing")

    # 4. Validate rating
    invalid_ratings = df[
        ~df["my_rating"].between(0, 5)
        & df["my_rating"].notnull()
    ]

    if not invalid_ratings.empty:
        errors.append(
            f"Invalid ratings found: {len(invalid_ratings)}"
        )

    # 5. Validate page count
    invalid_pages = df[
        (df["page_count"] <= 0)
        & df["page_count"].notnull()
    ]

    if not invalid_pages.empty:
        errors.append(
            f"Invalid page counts found: {len(invalid_pages)}"
        )

    # 6. Validate format
    allowed_formats = {
        "Physical",
        "Kindle",
        "Digital"
    }

    invalid_formats = df[
        ~df["format"].isin(allowed_formats)
        & df["format"].notnull()
    ]

    if not invalid_formats.empty:
        errors.append(
            f"Invalid formats found: {len(invalid_formats)}"
        )

    # 7. Check duplicate books
    duplicates = df.duplicated(
        subset=["book_title", "author"]
    )

    if duplicates.any():
        errors.append(
            f"Duplicate books found: {duplicates.sum()}"
        )

    # Final result
    if errors:

        print("❌ VALIDATION FAILED")

        for error in errors:
            print("-", error)

        return False

    print("✅ VALIDATION PASSED")

    return True


# Test the complete validation flow
from extract import extract_books
from transform import transform_books


if __name__ == "__main__":

    print("Running ETL validation...\n")

    # Extract
    df = extract_books()

    # Transform
    cleaned_df = transform_books(df)

    # Validate
    result = validate_books(cleaned_df)

    print("\nValidation result:", result)

    if result:
        print("✅ Data is ready for PostgreSQL!")
    else:
        print("❌ Data should NOT be loaded.")