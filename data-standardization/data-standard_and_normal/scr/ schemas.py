"""
Canonical Data Schemas

Defines the standard structure of financial records after transformation.
All pipeline modules must output data that conforms to this schema.

This ensures:
- Consistent column names
- Predictable data types
- Compatibility with analytics and reporting tools
"""
import pandas as pd
# "1. Canonical column list
def canonical_column_list(df:pd.DataFrame) -> pd.DataFrame:
    canonical_column = ["Id ", "Date, Name "," Description" , "Amount" , "Status", "Salary", "Department",  "Currency", "Balance"]

# 2. Required column set
required_column_set = ["date",
"description",
"category",
"amount",
"currency",
"base_currency",
"amount_base",
"source",
"account",
"transaction_type",
"status",
"confidence_score"
]
# 3. Data type expectations
data_type_expectations = {
    "date": "datetime64[ns]",
    "description": "string",
    "category": "string",
    "Amount": "int",
    "currency" : "INR"}
# 4. Validation helper functions
def validate_columns(df: pd.DataFrame, required_columns: list) -> bool:
    """
    Validates if the DataFrame contains all required columns.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        required_columns (list): List of required column names.

    Returns:
        bool: True if all required columns are present, False otherwise.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return False
    return True

def validate_data_types(df: pd.DataFrame, data_type_expectations: dict) -> bool:
    """
    Validates if the DataFrame columns match the expected data types.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        data_type_expectations (dict): Dictionary of column names and expected data types.

    Returns:
        bool: True if all columns match the expected data types, False otherwise.
    """
    for column, expected_type in data_type_expectations.items():
        if column in df.columns:
            if df[column].dtype != expected_type:
                print(f"Column '{column}' has incorrect type. Expected: {expected_type}, Found: {df[column].dtype}")
                return False
    return True
