import pandas as pd
from sqlalchemy import create_engine

def load_to_mysql(df: pd.DataFrame) -> None:
    """Loads data into a MySQL database"""
    try:
        # Replace with your actual credentials and DB name
        user = 'root'
        password = '5445'
        host = 'localhost'
        port = '3306'
        database = 'my_database'

        # MySQL connection string
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

        # Load data to MySQL
        df.to_sql('test_mysql', con=engine, if_exists='replace', index=False)

        print(f"✅ Loaded {len(df)} rows into MySQL table 'cal_uni'.")
    except Exception as e:
        print(f"❌ Failed to load data: {e}")

# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Score': [90, 85]
    })
    load_to_mysql(df)
