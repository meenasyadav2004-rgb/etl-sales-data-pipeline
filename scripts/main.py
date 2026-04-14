from extract import extract
from transform import transform
from load import load
from logger import setup_logger

def run_pipeline():
    setup_logger()

    print("Starting ETL Pipeline...")

    df = extract()
    if df is not None:
        df = transform(df)
        if df is not None:
            load(df)

    print("ETL Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()