def transform(df):
    try:
        df = df.dropna()

        # Total before discount
        df["total_price"] = df["quantity"] * df["price"]

        # Discount amount
        df["discount_amount"] = df["total_price"] * df["discount"]

        # Final revenue
        df["final_price"] = df["total_price"] - df["discount_amount"]

        print("Transform successful")
        return df

    except Exception as e:
        print("Error in transform:", e)
        return None