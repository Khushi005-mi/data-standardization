# Validate that fallback rules:

# Fill missing values correctly
# Apply default values when needed
# Flag rows that cannot be safely fixed
# Never silently invent financial data
def test_fallback_rules():
    # Test that missing values are filled correctly
    assert fill_missing_values({"key": None}) == {"key": "default_value"}

    # Test that default values are applied when needed
    assert apply_default_values({"key": "value"}) == {"key": "value"}
    assert apply_default_values({"key": None}) == {"key": "default_value"}

    # Test that rows that cannot be safely fixed are flagged
    assert flag_unfixable_rows({"key": "invalid"}) == {"key": "invalid", "flagged": True}

    # Test that financial data is not silently invented
    assert not invent_financial_data({"key": None})

    # Test that results are deterministic
    result1 = deterministic_function({"key": "value"})
    result2 = deterministic_function({"key": "value"})
    assert result1 == result2
    
