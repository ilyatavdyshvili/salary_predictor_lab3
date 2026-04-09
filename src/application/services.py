import subprocess


class DataSyncService:

    def sync_dataset(self) -> None:
        print("[Sync] Running dvc pull...")
        subprocess.run(["dvc", "pull"], check=True)
        print("[Sync] Dataset is up to date")
