from src.domain.salary_predictor import ISalaryPredictor
from src.application.services import DataSyncService


class SalaryPredictionService:

    def __init__(self, predictor: ISalaryPredictor, data_sync_service: DataSyncService):
        self.predictor = predictor
        self.data_sync_service = data_sync_service

        
        self.data_sync_service.sync_dataset(
            remote_path="hr_data.csv",       # файл в MinIO
            local_path="data/hr_data.csv"    # локальный путь
        )

    def predict(self, features: dict) -> float:
        return self.predictor.predict(features)
