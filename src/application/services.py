import subprocess


class DataSyncService:
    def sync_dataset(self):
        subprocess.run(
            ["dvc", "pull"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
