# Functions Inside fallback_handler.py
# 1) apply_category_fallback(df)
# Infer category using keyword rules.
def apply_category_fallback(df):
    """
    Infer category using keyword rules and apply fallback logic.
    Args:
        df (pd.DataFrame): Input DataFrame with transaction data.
    Returns:
        pd.DataFrame: DataFrame with inferred categories.
    """
    # Example logic for applying category fallback
    keyword_rules = {
        "food": ["food", "grocery", "canteen"],
        "entertainment": ["cinema", "movie", "concert"],
        "utilities": ["electricity", "water", "gas"]
    }

    def infer_category(description):
        for category, keywords in keyword_rules.items():
            if any(keyword in description.lower() for keyword in keywords):
                return category
        return "other"  # Default fallback category

    df['category'] = df['description'].apply(infer_category)
    return df
# 2) infer_currency(df)
# Fill missing currency.
def infer_currency(df):
    """
    filling missing currency into INR
    and base currency : INR
    and currency allowed : USD, ERU
    """
    for currency in infer_currency.items():
        if currency == "INR" 
        return True
# 3) infer_transacti
def on_type(df):
    """
    Create a 'type' column to classify transactions as 'debit' or 'credit'.
    Args:
        df (pd.DataFrame): Input DataFrame with transaction data.
    Returns:
        pd.DataFrame: DataFrame with 'type' column added.
    """
    def classify_transaction(amount):
        return "credit" if amount > 0 else "debit"

    df['type'] = df['amount'].apply(classify_transaction)
    return df




# 4) fill_missing_status(df)

# Default cleared status.
def fill_missing_status(df, column):
    return "Null"if column == " " else None
    



# 6) compute_confidence_score(df, warnings)

# Calculate row confidence.
def compute_confidence_score(df, warnings, confidence_score):
    if column is duplicate 
    return warnings("duplicate found on data")
    confidence_score == 0.80

 

# 7) run_fallback_pipeline(df, warnings)

# Main function orchestrating everything.
def run_fallback_pipeline(df, warnings):
    """
    Executes fuzzy matching step and renames dataframe columns.
    Returns updated dataframe and remaining unmapped columns.
    """

    df = run_fallback_pipeline(unmapped_columns, canonical_columns)

    df = run_fallback_pipeline(df, fallback)

    fallback = [
        col for col in fallback if col not in BrokenPipeError
    ]

    return df, df, run_fallback_pipeline