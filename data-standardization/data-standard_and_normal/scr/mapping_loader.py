# 1) Locate Config Folder
# Find path regardless of where code runs (API / script / tests).
from config/category_mappings.yaml import category
from config/column_mappings.yaml import column
from config/currency_mappings.yaml import currency
from config/fallback_mappings.yaml import fallback
from config.settings_mappings.yaml import system
from config.source_mappings.yaml import source

# 2) Load YAML Safely
with open(config, "r") as f:
    with yaml.safe_load()

# Use safe YAML parsing.
from pathlib import Path
import yaml

CONFIG_CACHE = {}

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


def load_yaml_config(file_name: str) -> dict:
    """
    Load YAML config file with in-memory caching.
    """

    # Return cached version if already loaded
    if file_name in CONFIG_CACHE:
        return CONFIG_CACHE[file_name]

    # Build full path
    file_path = CONFIG_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    # Read YAML safely
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    # Store in cache
    CONFIG_CACHE[file_name] = data

    return data
# 4) Provide Getter Functions
from mapping_loader import get_exact_mapping

mapping = get_exact_mapping()
def get_column_mapping(COLUMN_MAPPING,load_configs):
    if COLUMN_MAPPING is None:
        load_configs()
    return COLUMN_MAPPING

def get_exact_mapping(EXACT_MAPPING,load_configs):
    if EXACT_MAPPING is None:
        load_configs()
    return EXACT_MAPPING

def get_fuzzy_wording(FUZZY_WORDING,load_configs):
    if FUZZY_WORDING is None:
        load_configs()
    return FUZZY_WORDING
    
    

        