import pandas as pd
from src.column_mapper import map_columns


# -------------------------------------------------
# Test 1 — Exact column mapping
# -------------------------------------------------

def test_exact_column_mapping():
    df = pd.DataFrame(columns=[
        "date",
        "description",
        "amount",
        "currency",
        "category"
    ])

    mapped_df, stats = map_columns(df, source_id="generic")

    assert "date" in mapped_df.columns
    assert stats["exact_matches"] >= 5


# -------------------------------------------------
# Test 2 — Case and spacing variations
# -------------------------------------------------

def test_column_normalization():
    df = pd.DataFrame(columns=[
        "Transaction Date",
        "Transaction Description",
        "Amount",
        "Currency Code",
        "Expense Category"
    ])

    mapped_df, stats = map_columns(df, source_id="generic")

    expected_columns = ["date", "description", "amount", "currency", "category"]

    for col in expected_columns:
        assert col in mapped_df.columns


# -------------------------------------------------
# Test 3 — Fuzzy column mapping
# -------------------------------------------------

def test_fuzzy_mapping():
    df = pd.DataFrame(columns=[
        "txn_dt",
        "narration",
        "amt",
        "curr",
        "cat"
    ])

    mapped_df, stats = map_columns(df, source_id="generic")

    assert stats["fuzzy_matches"] >= 1
    assert "date" in mapped_df.columns
    assert "amount" in mapped_df.columns


# -------------------------------------------------
# Test 4 — Unknown columns are flagged
# -------------------------------------------------

def test_unknown_columns_flagged():
    df = pd.DataFrame(columns=[
        "random_field_1",
        "random_field_2"
    ])

    mapped_df, stats = map_columns(df, source_id="generic")

    assert stats["unmapped_columns"] >= 1


# -------------------------------------------------
# Test 5 — Required columns must exist after mapping
# -------------------------------------------------

def test_required_columns_exist():
    df = pd.DataFrame(columns=[
        "date",
        "amount"
    ])

    mapped_df, stats = map_columns(df, source_id="generic")

    required_columns = ["date", "description", "amount", "currency", "category"]

    for col in required_columns:
        assert col in mapped_df.columns