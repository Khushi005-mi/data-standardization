# 1) Read source profiles from config
with open(config/source_profiles.yaml , "r") as f:
  data = f.read

# It loads config/source_profiles.yaml
# 2) Inspect the incoming dataframe
if not path.exists():
  raise FileNotFoundError(f"file is not present in{file_path}")
extension = path.suffix.lower()

if extension not in SUPPORTED_EXTENTION:
   raise ValueError("not supported extention")
if extension == ".csv":
    return _read_csv(path)

if extension == [".xls",".xlsx"]:
    return _read_csv(path)

if extension == ".json":
    return _read_csv(path)

# 3) Match signals against known profiles
def match_signals(df):
    signals = df.columns
    matched_signals = {}
    for signal in signals:
        if signal in KNOWN_PROFILES:
            matched_signals[signal] = KNOWN_PROFILES[signal]
    return matched_signals


# 4) Return a canonical source_id
def get_canonical_source_id(signals):
    for signal in signals:
        if signal in KNOWN_PROFILES:
            return KNOWN_PROFILES[signal]
    return "unknown"
