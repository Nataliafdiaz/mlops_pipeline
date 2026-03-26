import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "modelo_pago_v1.pkl"

modelo = joblib.load(MODEL_PATH)

def predecir(data: dict):
    df = pd.DataFrame([data])
    pred = modelo.predict(df)
    return int(pred[0])