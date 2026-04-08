import subprocess


class DataSyncService:

    def __init__(self, storage):
        self.storage = storage  # можно оставить, но не используется

    def sync_dataset(self) -> None:
        print("[DVC] Pulling dataset...")
        subprocess.run(["dvc", "pull"], check=True)
