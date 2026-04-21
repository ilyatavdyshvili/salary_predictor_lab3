## Лабораторная работа №3. Вариант 14 "Предсказание зарплаты"

### Клонирование проекта
```bash
git clone https://github.com/ilyatavdyshvili/salary_predictor_lab3
cd salary_predictor_lab3
```
### Подготовка

Создаем в корне проекта файл ```.env```, со следующим содержимым:
```
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=datasets
```


### 1. Установка

```
poetry install

poetry shell
```

---

### 2. Запуск MinIO

```
docker-compose up -d
```

Открыть: http://localhost:9001
Логин: minioadmin / minioadmin

Проверяем создался ли bucket "datasets"
---

### 3. Настройка DVC remote (если требуется)

Убедитесь, что remote настроен:

```
dvc remote list
```
Если нужно:
```
dvc remote add -d myremote s3://datasets
dvc remote modify myremote endpointurl http://localhost:9000
dvc remote modify myremote access_key_id minioadmin
dvc remote modify myremote secret_access_key minioadmin
```

---

### 4. Загрузка данных
Для начала запускаем:
```
./script.sh
```
Скачиваем датасет:
```
dvc pull
```
После этого появится файл:
```data/hr_data.csv```
---

### 5. Обучаем модель

```
python -m scirpts.train_model
```
### 6. Запускаем API
```
poetry run uvicorn src.presentation.api:app --reload
```
Переходим в браузер: ```http://127.0.0.1:8000/docs```

