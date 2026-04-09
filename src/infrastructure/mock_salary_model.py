import pandas as pd
from src.domain.salary_predictor import ISalaryPredictor


class MockSalaryPredictor(ISalaryPredictor):

    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.df = None

    def _load(self):
        self.df = pd.read_csv(self.dataset_path)

    def predict(self, features: dict) -> float:
        self._load()

        position = features.get("position")
        subset = self.df[self.df["position"] == position]

        if subset.empty:
            return float(self.df["salary"].mean())

        return float(subset["salary"].mean())
