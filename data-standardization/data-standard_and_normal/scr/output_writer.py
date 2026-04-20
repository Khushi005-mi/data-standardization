# imports
import pandas as pd 
import matplotlib.pyplot as plt

# Output file configuration
# Utility: ensure output folders exist

# 1) Write Clean Standardized Dataset
def clean_standardized_dataset(df, output_path):
    """
    Writes the clean standardized dataset to the specified output path.

    Args:
        df (pd.DataFrame): The clean standardized DataFrame.
        output_path (str): The file path to write the dataset to.
    """
    df.to_csv(output_path, index=False)
    print(f"Clean standardized dataset written to {output_path}")

# 2) Write Flagged Rows (for manual review)
def flagged_rows(df, output_path):
    """
    Writes the flagged rows for manual review to the specified output path.

    Args:
        df (pd.DataFrame): The DataFrame containing flagged rows.
        output_path (str): The file path to write the flagged rows to.
    """
    flagged_rows = df[df["flag"] == True]  # Assuming 'flag' column indicates flagged rows
    flagged_rows.to_csv(output_path, index=False)
    print(f"Flagged rows written to {output_path}")
# 3) Generate Pipeline Summary Report
def pipeline_Summary_report(df:str):
    Summary = (
        "clean_standardized_dataset" = clean_standardized_dataset,
        "flagged_dataset" = flagged_rows,
        "status"= "success"

    )
# 4) Master Writer (Single Entry Point)
def master_writer(df, output_paths):
    """
    Master writer function to handle all output writing tasks.

    Args:
        df (pd.DataFrame): The DataFrame to process.
        output_paths (dict): A dictionary containing output paths for different outputs.
            Expected keys: 'clean', 'flagged'
    """
    # Write clean standardized dataset
    clean_standardized_dataset(df,output_paths,["clean"])

    # Write flagged rows
    flagged_rows(df,output_paths)

    print("All outputs have been written successfully.")
