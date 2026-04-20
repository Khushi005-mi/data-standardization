import pandas as pd
from pathlib import Path

from src.transformation_pipeline import run_pipeline


# -------------------------------------------------
# Test 1 — Full pipeline execution
# -------------------------------------------------

def test_pipeline_runs_successfully(tmp_path):
    """
    Runs entire pipeline on a small raw dataset.
    """

    # Create fake raw dataset
    raw_df = pd.DataFrame({
        "Txn Date": ["01/01/2024", "02/01/2024"],
        "Narration": ["Swiggy", "Uber"],
        "Amt (₹)": ["₹500", "₹300"],
        "Curr": ["INR", "INR"]
    })

    # Save to temp file
    input_file = tmp_path / "raw_bank.csv"
    raw_df.to_csv(input_file, index=False)

    # Run pipeline
    results = run_pipeline(str(input_file))

    # Verify outputs exist
    assert results["rows_processed"] == 2
    assert results["standardized_file"] is not None


# -------------------------------------------------
# Test 2 — Output schema validation
# -------------------------------------------------

def test_output_has_canonical_columns(tmp_path):
    raw_df = pd.DataFrame({
        "Txn Date": ["01/01/2024"],
        "Narration": ["Amazon"],
        "Amt (₹)": ["₹1000"],
        "Curr": ["INR"]
    })

    input_file = tmp_path / "raw.csv"
    raw_df.to_csv(input_file, index=False)

    results = run_pipeline(str(input_file))

    standardized_df = pd.read_csv(results["standardized_file"])

    expected_columns = [
        "date",
        "description",
        "amount",
        "currency",
        "category",
        "source",
        "flag_for_review"
    ]

    for col in expected_columns:
        assert col in standardized_df.columns


# -------------------------------------------------
# Test 3 — No crash on unknown columns
# -------------------------------------------------

def test_pipeline_handles_unknown_columns(tmp_path):
    raw_df = pd.DataFrame({
        "Some Random Column": ["A"],
        "Another Weird Column": ["B"]
    })

    input_file = tmp_path / "unknown.csv"
    raw_df.to_csv(input_file, index=False)

    results = run_pipeline(str(input_file))

    assert results["rows_processed"] == 1
    assert results["flagged_rows"] >= 1