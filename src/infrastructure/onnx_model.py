import numpy as np
import onnxruntime as ort

from src.domain.salary_predictor import ISalaryPredictor


class ONNXSalaryPredictor(ISalaryPredictor):

    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name

        self.city_map = {
            "Riga": 0,
            "Berlin": 1,
            "London": 2,
        }

        self.position_map = {
            "Junior Python": 0,
            "Python Developer": 1,
            "Senior Python": 2,
            "Data Analyst": 3,
            "ML Engineer": 4,
            "Backend Developer": 5,
        }

    def predict(self, features: dict) -> float:

        city_encoded = self.city_map.get(features["city"], 0)
        position_encoded = self.position_map.get(features["position"], 0)

        input_data = np.array([[
            features["experience"],
            city_encoded,
            position_encoded
        ]], dtype=np.float32)

        result = self.session.run(None, {self.input_name: input_data})

        return float(result[0].ravel()[0])
