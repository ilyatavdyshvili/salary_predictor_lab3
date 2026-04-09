#!/usr/bin/env bash
set -e

# === CONFIG ===
DATA_DIR="data"
CSV_FILE="$DATA_DIR/hr_data.csv"

# === 1. Wait a bit for environment (optional) ===
echo "Waiting for services..."
sleep 3

# === 2. Create dataset directory ===
mkdir -p ${DATA_DIR}

# === 3. Create CSV dataset ===
cat > ${CSV_FILE} << EOF
experience,city,position,skills,salary
1,Riga,Junior Python,"python,sql",1300
3,Riga,Python Developer,"python,django,sql",2300
5,Berlin,Senior Python,"python,docker,kubernetes",4500
2,London,Data Analyst,"python,pandas,sql",2700
7,London,ML Engineer,"python,tensorflow,ml",6000
4,Riga,Backend Developer,"python,fastapi,postgres",3000
8,Moscow,SQLDeveloper,"sql,data analysis",9999
9,Kazan,QA Developer,"android, java",100000
EOF

echo "Dataset created at ${CSV_FILE}"

# === 4. Add file to DVC ===
echo "Adding file to DVC..."
dvc add ${CSV_FILE}

# === 5. Stage DVC metadata ===
git add ${CSV_FILE}.dvc .gitignore

# === 6. Commit changes ===
git commit -m "Add dataset via automation script" || echo "Nothing to commit"

# === 7. Push to DVC remote ===
echo "Pushing data to DVC remote..."
dvc push

# === 8. Remove local CSV (simulate clean environment) ===
rm -f ${CSV_FILE}
echo "Local dataset removed."

echo "Done. Now anyone can run: dvc pull"
