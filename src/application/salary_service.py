from src.domain.salary_predictor import ISalaryPredictor
from src.application.services import DataSyncService


class SalaryPredictionService:

    def __init__(self, predictor: ISalaryPredictor, data_sync_service: DataSyncService):
        self.predictor = predictor
        self.data_sync_service = data_sync_service

    def predict(self, features: dict) -> float:
        self.data_sync_service.sync_dataset()

        return self.predictor.predict(features)
