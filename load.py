import os

def load(df):
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        output_path = os.path.join(BASE_DIR, "output", "cleaned_data.csv")

        df.to_csv(output_path, index=False)

        print("Load successful")
        print("File saved at:", output_path)

    except Exception as e:
        print("Error in load:", e)