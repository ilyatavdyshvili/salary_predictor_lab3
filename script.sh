#!/usr/bin/env bash
set -e

# === CONFIG ===
DATA_DIR="data"
CSV_FILE="$DATA_DIR/hr_data.csv"

echo "=== START SCRIPT ==="

# === 1. Wait for MinIO ===
echo "Waiting for MinIO..."
sleep 5

# === 2. Create data directory ===
mkdir -p ${DATA_DIR}

# === 3. Create dataset ===
echo "Creating dataset..."

cat > ${CSV_FILE} << EOF
experience,city,position,skills,salary
1,Riga,Junior Python,"python,sql",1300
3,Riga,Python Developer,"python,django,sql",2300
5,Berlin,Senior Python,"python,docker,kubernetes",4500
2,London,Data Analyst,"python,pandas,sql",2700
7,London,ML Engineer,"python,tensorflow,ml",6000
4,Riga,Backend Developer,"python,fastapi,postgres",3000
EOF

echo "Dataset created at ${CSV_FILE}"

# === 4. Add to DVC ===
echo "Adding dataset to DVC..."
dvc add ${CSV_FILE}

# === 5. Git commit (если есть изменения) ===
git add ${CSV_FILE}.dvc .gitignore
git commit -m "Add dataset via script" || echo "Nothing to commit"

# === 6. Push to DVC remote (MinIO) ===
echo "Pushing dataset to DVC remote..."
dvc push

# === 7. Install mc (MinIO client) if not exists ===
if ! command -v mc &> /dev/null
then
    echo "Installing MinIO client (mc)..."
    curl https://dl.min.io/client/mc/release/linux-amd64/mc -o mc
    chmod +x mc
    sudo mv mc /usr/local/bin/
fi

# === 8. Upload file as plain object (для boto3) ===
echo "Uploading file to MinIO as plain object..."

mc alias set local http://localhost:9000 minioadmin minioadmin

# создаём bucket если нет
mc mb local/datasets || true

mc cp ${CSV_FILE} local/datasets/hr_data.csv

echo "File uploaded as datasets/hr_data.csv"

# === 9. Remove local file ===
echo "Removing local dataset..."
rm -f ${CSV_FILE}

echo "Local file removed"

# === DONE ===
echo "=== DONE ==="
echo "Now run:"
echo "python -m src.presentation.cli"
