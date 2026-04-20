#Convert to string and lowercase
# Remove accents
import re
from unidecode import unidecode
def normalize_column_name(column: str) -> str:
    """
    Convert raw column names into normalized snake_case format.
    """

column = str(column).lower()
column = unidecode(column)
column = re.sub(r"[^\w\s]", "", column)
column = re.sub(r"\s+", "", column)
column = column.replace[" ","_"]
column = re.sub(r"_+", "_", column)
 
# 2. Apply exact mappings
def apply_exact_mapping(column: str) -> str:
    exact_mappings = {
        "id": "identifier",
        "dob": "date_of_birth",
        "fname": "first_name",
        "lname": "last_name",
    }
    return exact_mappings.get(column, column)


# 3. Apply fuzzy matching
# Import Library
from rapidfuzz import process, fuzz
# Step 2 — Define Matching Threshold
def fuzzy_match_columns(unmapped_columns, canonical_columns, threshold=80):
    """
    Attempts to map unmapped columns using fuzzy string matching.
    Returns dictionary: {raw_column: canonical_column}
    """

    fuzzy_matches = {}
    for col in unmapped_columns:
        match,score,_ = process.extractOne(
            col,
            canonical_columns,
            scorer=fuzz.token_sort_ratio
)      
        if score >= threshold:
         fuzzy_matches[col] = match
         return fuzzy_matches
# 4. Flag unmapped columns
def flag_unmapped_columns(unmapped_columns,warnings):
    for col in unmapped_columns:
            warnings.append({
            "type": "UNMAPPED_COLUMN",
            "column": col,
            "message": f"Column '{col}' could not be mapped to canonical schema"
        })
