from fastapi import FastAPI
from pydantic import BaseModel
from app.model_deploy import predecir

app = FastAPI(
    title="API Modelo Pago",
    description="API para predecir el estado de pago",
    version="1.0"
)

class InputData(BaseModel):
    edad_cliente: float
    salario_cliente: float
    cant_creditosvigentes: float
    total_otros_prestamos: float
    capital_prestado: float
    cuota_pactada: float
    plazo_meses: float
    capacidad_pago: float
    ratio_deuda: float
    ratio_credito_salario: float
    tendencia_ingresos: float
    creditos_sectorReal: float
    creditos_sectorFinanciero: float
    creditos_sectorCooperativo: float
    tipo_credito: float
    tipo_laboral: float

@app.get("/")
def home():
    return {"mensaje": "La API está funcionando correctamente"}

@app.post("/predict")
def predict(data: InputData):
    resultado = predecir(data.dict())
    return {"prediccion": int(resultado)}