from pathlib import Path
from src.domain.interfaces import IDataStorage


class DataSyncService:
    """Сервис синхронизации данных с MinIO через IDataStorage"""

    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def sync_dataset(self, remote_path: str, local_path: str) -> None:
        local_file = Path(local_path)

        if not local_file.exists():
            print(f"[Sync] Файл {local_path} не найден. Скачиваю из хранилища...")

            # создаём папки если их нет
            local_file.parent.mkdir(parents=True, exist_ok=True)

            # скачиваем через интерфейс
            self.storage.download_file(remote_path, local_path)

        else:
            print(f"[Sync] Файл {local_path} уже существует. Пропускаю.")
