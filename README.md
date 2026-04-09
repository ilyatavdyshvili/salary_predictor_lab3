## Лабораторная работа №2. Вариант 14 "Предсказание зарплаты"

### Клонирование проекта
```bash
git clone https://github.com/ilyatavdyshvili/quality-grading-ai-lab2.git
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
Вносим изменения в датасет
```
echo '10,Paris,DevOps Engineer,"python,docker",5000' >> data/hr_data.csv
```
Фиксируем текущую версию
```
dvc add data/hr_data.csv
git add data/hr_data.csv.dvc
git commit -m "Обновление датасета"
dvc push
```
Удаляем файл
```
rm data/hr_data.csv
```
Подтягиваем новую версию
```
dvc pull
```
Запускаем cli.py для проверки
```
python -m src.presentation.cli
```
Пример работы:
```
Введите должность: DevOps Engineer
Предсказанная зарплата: 5000.0
```
