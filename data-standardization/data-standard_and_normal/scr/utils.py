"""
utils.py

Shared utility helpers used across the Financial Data Standardization Engine.

Responsibilities:
1) File reading (CSV / Excel / JSON)
2) Column normalization
3) String normalization (important for matching)
4) Date parsing
5) Currency cleanup helpers
6) Logging helper
"""

import pandas as pd
import re
from pathlib import Path
from datetime import datetime
from unidecode import unidecode


# =========================================================
# 1) FILE READING HELPERS
# =========================================================

SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".xls", ".json"]


def read_input_file(file_path: str) -> pd.DataFrame:
    """
    Universal reader for financial files.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = path.suffix.lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")

    if ext == ".csv":
        return _read_csv(path)

    if ext in [".xlsx", ".xls"]:
        return _read_excel(path)

    if ext == ".json":
        return _read_json(path)


def _read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")


def _read_excel(path: Path) -> pd.DataFrame:
    return pd.read_excel(path, engine="openpyxl")


def _read_json(path: Path) -> pd.DataFrame:
    return pd.read_json(path)


# =========================================================
# 2) COLUMN NORMALIZATION
# =========================================================

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standard column cleanup applied immediately after reading.
    """

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )

    return df


# =========================================================
# 3) STRING NORMALIZATION (VERY IMPORTANT)
# =========================================================

def normalize_text(text: str) -> str:
    """
    Used before fuzzy matching and mapping.
    """
    if pd.isna(text):
        return ""

    text = str(text)
    text = unidecode(text)        # remove accents
    text = text.lower().strip()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text


# =========================================================
# 4) DATE PARSING
# =========================================================

COMMON_DATE_FORMATS = [
    "%d-%m-%Y",
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m/%d/%Y",
    "%d %b %Y",
    "%d %B %Y",
]


def parse_date(value):
    """
    Attempts multiple date formats.
    Returns ISO format YYYY-MM-DD.
    """
    if pd.isna(value):
        return None

    value = str(value).strip()

    for fmt in COMMON_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue

    return None  # let fallback handler deal with it


# =========================================================
# 5) CURRENCY CLEANING
# =========================================================

def extract_numeric_amount(value):
    """
    Converts values like:
    ₹1,20,000.50  → 120000.50
    $1,000 → 1000
    """
    if pd.isna(value):
        return None

    value = str(value)
    value = re.sub(r"[^\d\.-]", "", value)

    try:
        return float(value)
    except ValueError:
        return None


# =========================================================
# 6) LOGGING HELPER
# =========================================================

def log_step(message: str):
    """
    Simple pipeline logger.
    Replace later with proper logging if needed.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}")