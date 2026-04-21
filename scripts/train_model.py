import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import numpy as np

# === загрузка данных ===
df = pd.read_csv("data/hr_data.csv")

# кодируем категориальные признаки
le_city = LabelEncoder()
le_position = LabelEncoder()

df["city"] = le_city.fit_transform(df["city"])
df["position"] = le_position.fit_transform(df["position"])

# признаки
X = df[["experience", "city", "position"]].values.astype(np.float32)
y = df["salary"].values.astype(np.float32)

# модель
model = RandomForestRegressor()
model.fit(X, y)

# конвертация в ONNX
initial_type = [("float_input", FloatTensorType([None, 3]))]

onnx_model = convert_sklearn(model, initial_types=initial_type)

# сохраняем
with open("models/salary_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Model saved to models/salary_model.onnx")
