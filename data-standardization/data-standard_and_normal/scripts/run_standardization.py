# 1) Accept input file from terminal
import pandas as pd
import sys
def accept_input(df:pd.DataFrame):
    if len(sys.argv) != 2:
        raise ValueError("Please provide exactly one input file path as an argument.")

    input_file = sys.argv[1]
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        raise ValueError(f"Error reading the input file: {e}")

    return df
# 2) Validate input
if col  in input_file not in input(input_file,"r"):
  raise ValueError("input is not valid")

# 3) Load raw dataframe
def Load_raw_dataframe(df:pd.DataFrame):
    raw_data = pd.read_csv("data-standard_and_normal/data/reports")

# 4) Run transformation pipeline
def run_transformation_pipeline(df: pd.DataFrame):
    # Example transformation: Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Example transformation: Fill missing values with mean for numeric columns
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Example transformation: Normalize numeric columns
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    return df
# 5) Print summary to terminal
summary = {
    "raw_dataframe ": Load_raw_dataframe,
    "transformation":run_transformation_pipeline
}
# User runs script →
#     Validate CLI args →
#     Read raw file →
#     Run pipeline →
#     Write outputs →
#     Print summary →
# Done