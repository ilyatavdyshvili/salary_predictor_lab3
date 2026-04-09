import os
from dotenv import load_dotenv

from src.infrastructure.mock_salary_model import MockSalaryPredictor
from src.application.services import DataSyncService
from src.application.salary_service import SalaryPredictionService

load_dotenv()


def main():
    # сервис синхронизации через DVC
    sync_service = DataSyncService()

    # модель (читает локальный файл после dvc pull)
    predictor = MockSalaryPredictor("data/hr_data.csv")

    # бизнес-сервис
    salary_service = SalaryPredictionService(
        predictor=predictor,
        data_sync_service=sync_service,
    )

    print("\nSalary Prediction CLI")
    print("Введите должность (например: Data Scientist, Data Analyst, Junior Python)")

    while True:
        position = input("\nВведите должность (или 'exit'): ")

        if position.lower() == "exit":
            print("Выход...")
            break

        result = salary_service.predict({
            "position": position
        })

        print(f"Предсказанная зарплата: {result}")


if __name__ == "__main__":
    main()
