from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()


def test_predict():
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

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediccion" in response.json()