from fastapi import FastAPI, UploadFile, File
import pandas as pd
from src.run_standardization import run_pipeline

app = FastAPI(title="Financial Data Standardization API")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/standardize")
async def standardize(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result = run_pipeline(df)
    return result.to_dict(orient="records")