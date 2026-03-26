# Proyecto MLOps – Avance 4
**Proyecto Integrador – Natalia Díaz**

---

## Descripción general

Este proyecto implementa un pipeline completo de Machine Learning siguiendo principios de MLOps, incluyendo:

- Entrenamiento de modelo supervisado
- Exposición mediante API (FastAPI)
- Interfaz de usuario (Streamlit)
- Contenerización con Docker
- Testing automatizado
- Integración continua con GitHub Actions
- Análisis de calidad con SonarCloud
- Monitoreo básico de la API

---

## Modelo de Machine Learning

Se entrenó un modelo para predecir el comportamiento de clientes en función de variables financieras.

### Variables utilizadas:
- Edad del cliente
- Salario
- Cantidad de créditos vigentes
- Ratio deuda
- Capacidad de pago
- Tipo de crédito
- Tipo laboral

---

## API – FastAPI

La API permite realizar predicciones mediante el endpoint:

### Endpoint: