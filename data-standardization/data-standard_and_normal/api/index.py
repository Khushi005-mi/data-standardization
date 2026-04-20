from fastapi import FastAPI, UploadFile, File
import pandas as pd
from mangum import Mangum
from src.run_standardization import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is live"}

@app.post("/standardize")
async def standardize(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result = run_pipeline(df)
    return result.to_dict(orient="records")

handler = Mangum(app)