import subprocess


class DataSyncService:
    def sync_dataset(self):
        try:
            subprocess.run(
                ["dvc", "pull"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except subprocess.CalledProcessError:
            pass
