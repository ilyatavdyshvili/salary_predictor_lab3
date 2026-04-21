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
dvc pull data/hr_data.csv
```
После этого появится файл:
```data/hr_data.csv```
---

### 5. Обучаем модель

```
python scripts/train_model.py
```
### 6. Запускаем API
```
poetry run uvicorn src.presentation.api:app --reload
```
Переходим в браузер: ```http://127.0.0.1:8000/docs```
### 7. Проверка работы модели:
## 1. Базовые (из датасета):
```
{
  "experience": 1,
  "city": "Riga",
  "position": "Junior Python"
}
```
Ожидаемый вывод: "predicted_salary": 2627
```
{
  "experience": 7,
  "city": "London",
  "position": "ML Engineer"
}
```
Ожидаемый вывод: "predicted_salary": 4699
```
{
  "experience": 3,
  "city": "Riga",
  "position": "Python Developer"
}
```
Ожидаемый вывод: "predicted_salary": 3090
## 2. Новые комбинации
```
{
  "experience": 6,
  "city": "Berlin",
  "position": "Senior Python"
}
```
Ожидаемый вывод: "predicted_salary": 4613
```
{
  "experience": 2,
  "city": "London",
  "position": "Backend Developer"
}
```
Ожидаемый вывод: "predicted_salary": 2570
```
{
  "experience": 4,
  "city": "Riga",
  "position": "ML Engineer"
}
```
Ожидаемый вывод: "predicted_salary": 3289
## 3. Неизвестные данные:
```
{
  "experience": 10,
  "city": "Paris",
  "position": "DevOps Engineer"
}
```
Ожидаемый вывод: "predicted_salary": 4896
```
{
  "experience": 0,
  "city": "Riga",
  "position": "Intern"
}
```
Ожидаемый вывод: "predicted_salary": 2627
