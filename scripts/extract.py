import os
import pandas as pd

def extract():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(BASE_DIR, "data", "sales_data.csv")

        print("Reading file from:", file_path)

        df = pd.read_csv(file_path)
        print("Extract successful")
        return df

    except Exception as e:
        print("Error in extract:", e)
        return None

 
if __name__ == "__main__":
    df = extract()
    
    if df is not None:
        print(df.head())
    else:
        print("No data to display")
