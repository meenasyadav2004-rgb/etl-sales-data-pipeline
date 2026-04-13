ETL Sales Data Pipeline (Python Project)

Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and Pandas. It processes raw sales data, performs data transformations, and generates a cleaned dataset for analysis.


 Tech Stack
- Python
- Pandas
- File Handling (CSV)


  ETL Process
 1. Extract
- Reads raw sales data from CSV file
- Handles file path errors

 2. Transform
  - Cleans missing values
  - Calculates:
  - Total Price
  - Discount Amount
  - Final Revenue

 3. Load
- Saves processed data into output folder

 Features
- Modular code structure
- Error handling
- Real-world business logic (discount & revenue calculation)
  
 How to Run
bash
python scripts/main.py
