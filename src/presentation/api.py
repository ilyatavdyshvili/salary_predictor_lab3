from fastapi import FastAPI, Depends
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from functools import lru_cache

from src.infrastructure.storage import S3Storage
from src.infrastructure.onnx_model import ONNXSalaryPredictor
from src.application.services import DataSyncService
from src.application.salary_service import SalaryPredictionService


app = FastAPI()


# === REQUEST MODEL ===
class SalaryRequest(BaseModel):
    experience: float
    city: str
    position: str


class SalaryResponse(BaseModel):
    predicted_salary: float


# === DEPENDENCY ===
@lru_cache()
def get_service():
    load_dotenv()

    storage = S3Storage(
        endpoint_url=os.getenv("S3_ENDPOINT"),
        access_key=os.getenv("S3_ACCESS_KEY"),
        secret_key=os.getenv("S3_SECRET_KEY"),
        bucket=os.getenv("S3_BUCKET"),
    )

    sync_service = DataSyncService(storage)

    # синхронизация модели
    sync_service.sync_dataset(
        remote_path="salary_model.onnx",
        local_path="models/salary_model.onnx"
    )

    predictor = ONNXSalaryPredictor("models/salary_model.onnx")

    return SalaryPredictionService(
        predictor=predictor,
        data_sync_service=sync_service
    )


# === ENDPOINT ===
@app.post("/api/v1/hr/predict_salary", response_model=SalaryResponse)
def predict(
    request: SalaryRequest,
    service: SalaryPredictionService = Depends(get_service)
):
    result = service.predict(request.dict())

    return SalaryResponse(predicted_salary=result)
