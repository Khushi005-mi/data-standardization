import pandas as pd
from src.value_normalizer import normalize_values


# -------------------------------------------------
# Test 1 — Amount cleaning
# -------------------------------------------------

def test_amount_cleaning():
    df = pd.DataFrame({
        "amount": ["₹1,200.50", "$500", "1,000"]
    })

    result_df = normalize_values(df)

    assert result_df.loc[0, "amount"] == 1200.50
    assert result_df.loc[1, "amount"] == 500.0
    assert result_df.loc[2, "amount"] == 1000.0


# -------------------------------------------------
# Test 2 — Date normalization
# -------------------------------------------------

def test_date_parsing():
    df = pd.DataFrame({
        "date": ["01/01/2024", "2024-01-02", "03-01-2024"]
    })

    result_df = normalize_values(df)

    assert result_df.loc[0, "date"] == "2024-01-01"
    assert result_df.loc[1, "date"] == "2024-01-02"
    assert result_df.loc[2, "date"] == "2024-01-03"


# -------------------------------------------------
# Test 3 — Currency normalization
# -------------------------------------------------

def test_currency_normalization():
    df = pd.DataFrame({
        "currency": ["rs", "INR ", "usd", "$"]
    })

    result_df = normalize_values(df)

    assert all(result_df["currency"].isin(["INR", "USD"]))


# -------------------------------------------------
# Test 4 — Text normalization
# -------------------------------------------------

def test_description_cleaning():
    df = pd.DataFrame({
        "description": [" Café Expense ", "UBER!!", "Swiggy  "]
    })

    result_df = normalize_values(df)

    assert result_df.loc[0, "description"] == "cafe expense"
    assert result_df.loc[1, "description"] == "uber"
    assert result_df.loc[2, "description"] == "swiggy"


# -------------------------------------------------
# Test 5 — Invalid values handled safely
# -------------------------------------------------

def test_invalid_amount_returns_nan():
    df = pd.DataFrame({
        "amount": ["invalid"]
    })

    result_df = normalize_values(df)

    assert pd.isna(result_df.loc[0, "amount"])