import time
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8010"
CHECK_INTERVAL = 60  # segundos

payload = {
    "edad_cliente": 35,
    "salario_cliente": 500000,
    "cant_creditosvigentes": 2,
    "total_otros_prestamos": 150000,
    "capital_prestado": 200000,
    "cuota_pactada": 25000,
    "plazo_meses": 12,
    "capacidad_pago": 0.45,
    "ratio_deuda": 0.30,
    "ratio_credito_salario": 0.40,
    "tendencia_ingresos": 1.0,
    "creditos_sectorReal": 1,
    "creditos_sectorFinanciero": 0,
    "creditos_sectorCooperativo": 0,
    "tipo_credito": 1,
    "tipo_laboral": 1
}


def log_message(message: str) -> None:
    with open("monitor_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(f"{datetime.now()} - {message}")


def check_home() -> None:
    try:
        response = requests.get(f"{API_URL}/", timeout=10)
        if response.status_code == 200:
            log_message("Endpoint '/' OK")
        else:
            log_message(f"Endpoint '/' ERROR - status {response.status_code}")
    except Exception as e:
        log_message(f"Endpoint '/' ERROR - {e}")


def check_predict() -> None:
    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            log_message(f"Endpoint '/predict' OK - respuesta: {result}")
        else:
            log_message(f"Endpoint '/predict' ERROR - status {response.status_code}")
    except Exception as e:
        log_message(f"Endpoint '/predict' ERROR - {e}")


if __name__ == "__main__":
    log_message("Inicio del monitoreo de la API")
    while True:
        check_home()
        check_predict()
        time.sleep(CHECK_INTERVAL)
        