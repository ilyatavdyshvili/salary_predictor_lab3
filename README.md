## Лабораторная работа №2. Вариант 14 "Предсказание зарплаты"

### Клонирование проекта
```bash
git clone <REPO_URL>
cd quality-grading-ai-lab2-main
```
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

### 2. Запуск MinIO

```
docker-compose up -d
```

Открыть: http://localhost:9001
Логин: minioadmin / minioadmin

Создать bucket: `datasets`

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

```
dvc pull
```
После этого появится файл:
```data/hr_data.csv```
---

### 5. Запуск

```
python -m src.presentation.cli
```
Пример работы:
```
Введите должность: Data Scientist
Предсказанная зарплата: 82500.0
```
---




