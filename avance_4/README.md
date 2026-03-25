API de Predicción de Estado de Pago

## Proyecto Integrador – 

Este proyecto implementa el despliegue de un modelo de Machine Learning para predecir el estado de pago de clientes utilizando:

* 🔹 FastAPI (API del modelo)
* 🔹 Streamlit (interfaz web)
* 🔹 Docker (contenedorización)

---

# Objetivo

Disponibilizar un modelo de Machine Learning mediante una API REST y permitir su consumo desde una aplicación web interactiva.

---

#  Modelo

El modelo fue entrenado previamente y guardado como:

```
models/modelo_pago_v1.pkl
```

Se carga en producción mediante:

```
app/model_deploy.py
```

---

# Arquitectura

```
Usuario → Streamlit → FastAPI → Modelo ML
```

---

# Estructura del Proyecto

```
avance_4/
│
├── app/
│   ├── api.py
│   ├── model_deploy.py
│   └── streamlit_app.py
│
├── models/
│   └── modelo_pago_v1.pkl
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# 🚀 Cómo ejecutar el proyecto

## 🔹 1. Ejecutar API (FastAPI)

```bash
uvicorn app.api:app --reload
```

Abrir en navegador:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 2. Ejecutar Streamlit

```bash
streamlit run app/streamlit_app.py
```

Abrir:

```
http://localhost:8501
```

---

## 🔹 3. Ejecutar con Docker

### Construir imagen

```bash
docker build -t modelo-pago-api .
```

### Ejecutar contenedor

```bash
docker run -p 8010:8010 modelo-pago-api
```

Abrir:

```
http://127.0.0.1:8010/docs
```

---

#  Endpoint de predicción

## POST `/predict`

### Ejemplo JSON:

```json
{
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
```

---

## Respuesta

```json
{
  "prediccion": 1
}
```

---

# Consideraciones

Las variables categóricas fueron codificadas previamente:

* `tipo_credito`
* `tipo_laboral`
 Deben enviarse como valores numéricos.

---

# Tecnologías utilizadas

* FastAPI
* Uvicorn
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Docker

---

# 📈 Estado del proyecto

✔ API funcional
✔ Modelo desplegado
✔ Interfaz web operativa
✔ Docker funcionando

---

Proyecto Integrador – MLOps
