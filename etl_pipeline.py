print("🔥 etl_pipeline.py file is running")
from extract import extract_books
from transform import transform_books
from validation import validate_books
from load import load_books

def run_pipeline():

    print("\n========== ETL PIPELINE STARTED ==========")

    # -------------------------
    # 1. EXTRACT
    # -------------------------

    print("\n[1] Extracting data...")

    df = extract_books()

    print(f"Extracted records: {len(df)}")


    # -------------------------
    # 2. TRANSFORM
    # -------------------------

    print("\n[2] Transforming data...")

    cleaned_df = transform_books(df)

    print(f"Transformed records: {len(cleaned_df)}")


    # -------------------------
    # 3. VALIDATE
    # -------------------------

    print("\n[3] Validating data...")
    print("\nColumns after transformation:")
    print(cleaned_df.columns.tolist())
    is_valid = validate_books(cleaned_df)

    if not is_valid:

        print("\n❌ Validation failed.")
        print("Pipeline stopped.")

        return


    # -------------------------
    # 4. LOAD
    # -------------------------

    print("\n[4] Loading data into PostgreSQL...")

    load_books(cleaned_df)


    print("\n========== ETL PIPELINE COMPLETED ==========")


if __name__ == "__main__":

    run_pipeline()
    print("\n✅ ETL pipeline executed successfully")