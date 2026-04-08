## Лабораторная работа №2. Вариант 14 "Предсказание зарплаты"

### Подготовка

Создаем в корне проекта файл .env, со следующим содержимым:
```
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=datasets
```
Получаем данные:
```
dvc pull
```


### 1. Установка

```
poetry install

poetry shell
```

---

### 2. MinIO

```
docker-compose up -d
```

Открыть: http://localhost:9001
Логин: minioadmin / minioadmin

Создать bucket: `datasets`

---

### 3. DVC

```
dvc init
git commit -m "init"
```

---

### 4. Remote

```
dvc remote add -d myremote s3://datasets
dvc remote modify myremote endpointurl http://localhost:9000
dvc remote modify myremote access_key_id minioadmin
dvc remote modify myremote secret_access_key minioadmin
```

---

### 5. Данные

```
dvc add data/hr_data.csv
git add .
git commit -m "data v1"
dvc push
```

---

### 6. Запуск

```
python -m src.presentation.cli
```

---

### 7. Обновление данных

Изменить зарплаты → затем:

```
dvc add data/hr_data.csv
git commit -am "data v2"
dvc push
```

---

### 8. Проверка версий

Возвращаемся к версии "data v1"
```
git log --oneline
git checkout <hash_old_commit>
dvc checkout
python -m src.presentation.cli
```
После проверки первичной версии переходим к "data v2" и перепроверяем снова
```
git checkout main
dvc checkout
python -m src.presentation.cli
```


