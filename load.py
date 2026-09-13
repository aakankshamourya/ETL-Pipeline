import psycopg2
import pandas as pd


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="BOOK_ETL_DB",
        user="postgres",
        password="mourya++11@@AA"
    )

    return connection


def load_books(df):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO books (
            book_title,
            author,
            genre,
            page_count,
            read_date,
            my_rating,
            format
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:

        for _, row in df.iterrows():

            # Convert pandas missing values to Python None
            values = (
                row["book_title"],
                row["author"],
                row["genre"],
                None if pd.isna(row["page_count"])
                    else int(row["page_count"]),

                None if pd.isna(row["read_date"])
                    else row["read_date"].date(),

                None if pd.isna(row["my_rating"])
                    else float(row["my_rating"]),

                row["format"]
            )

            cursor.execute(query, values)

        connection.commit()

        print(f"✅ {len(df)} records loaded into PostgreSQL")

    except Exception as e:

        connection.rollback()

        print("❌ Error while loading data")
        print("Error:", e)

        raise

    finally:

        cursor.close()
        connection.close()


if __name__ == "__main__":

    try:

        connection = get_connection()

        print("✅ Successfully connected to PostgreSQL")

        connection.close()

    except Exception as e:

        print("❌ PostgreSQL connection failed")
        print("Error:", e)