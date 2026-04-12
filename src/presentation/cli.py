import os
from dotenv import load_dotenv

from src.infrastructure.storage import S3Storage
from src.infrastructure.mock_salary_model import MockSalaryPredictor
from src.application.services import DataSyncService
from src.application.salary_service import SalaryPredictionService


def main():
    load_dotenv()

    # Cоздаём S3Storage из .env
    storage = S3Storage(
        endpoint_url=os.getenv("S3_ENDPOINT"),
        access_key=os.getenv("S3_ACCESS_KEY"),
        secret_key=os.getenv("S3_SECRET_KEY"),
        bucket=os.getenv("S3_BUCKET"),
    )

    # DataSyncService
    sync_service = DataSyncService(storage=storage)

    predictor = MockSalaryPredictor("data/hr_data.csv")

    salary_service = SalaryPredictionService(
        predictor=predictor,
        data_sync_service=sync_service,
    )

    print("\nSalary Prediction CLI")

    while True:
        position = input("\nВведите должность (Например: Junior Python, ML Engineer или Senior Python)(или 'exit'): ")

        if position.lower() == "exit":
            print("Выход...")
            break

        result = salary_service.predict({
            "position": position
        })

        print(f"Предсказанная зарплата: {result}")


if __name__ == "__main__":
    main()
