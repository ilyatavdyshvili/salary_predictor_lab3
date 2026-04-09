import subprocess


class DataSyncService:
    def sync(self):
        print("[Sync] Running dvc pull...")  # можно оставить или убрать

        subprocess.run(
            ["dvc", "pull"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        print("[Sync] Dataset is up to date")
