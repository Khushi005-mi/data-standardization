"""
Financial Data Standardization API
Exposes the transformation pipeline as a serverless FastAPI endpoint.
"""

# =============================
# Imports
# =============================
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import tempfile
import shutil
import time

from loguru import logger

# Import core pipeline
from src.transformation_pipeline import run_transformation_pipeline

# =============================
# App Initialization
# =============================
app = FastAPI(title="Financial Standardization Engine")


# =============================
# Health Check Endpoint
# =============================
@app.get("/")
def health_check():
    """
    Used by deployment platforms to verify the API is running.
    """
    return {"status": "API is running"}


# =============================
# Main Standardization Endpoint
# =============================
@app.post("/api/standardize")
async def standardize_file(file: UploadFile = File(...)):
    """
    Accepts a CSV file and returns standardized financial data.
    """

    start_time = time.time()

    # -------------------------
    # Validate file
    # -------------------------
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    logger.info(f"Received file: {file.filename}")

    try:
        # -------------------------
        # Create temp directory
        # -------------------------
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir) / file.filename

            # Save uploaded file to temp storage
            with open(temp_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            logger.info("File saved to temporary storage")

            # -------------------------
            # Run transformation pipeline
            # -------------------------
            results = run_transformation_pipeline(temp_path)

            duration = round(time.time() - start_time, 2)

            logger.success(f"Processing completed in {duration} seconds")

            # -------------------------
            # Build API response
            # -------------------------
            response = {
                "status": "success",
                "processing_time_seconds": duration,
                "source_detected": results["source"],
                "records_processed": results["records_processed"],
                "records_standardized": results["records_standardized"],
                "data_quality_warnings": results["warnings"],
                "standardized_preview": results["preview"]
            }

            return JSONResponse(content=response)

    except Exception as e:
        logger.exception("Pipeline failed")

        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )