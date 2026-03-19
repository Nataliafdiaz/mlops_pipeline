# Proyecto Integrador - Avance 2

## Descripción general
En este avance se desarrolló el proceso de ingeniería de características y modelamiento supervisado para la predicción del comportamiento de pago de clientes, dentro de un flujo de trabajo orientado a MLOps.

A lo largo del desarrollo se realizó la preparación del dataset, la detección y corrección de data leakage, la construcción de variables derivadas, el entrenamiento de modelos supervisados, la optimización del modelo final y su almacenamiento para etapas posteriores de despliegue y monitoreo.

---

## Estructura del proyecto

```plaintext
mlops_pipeline/
│
├── models/
│   └── modelo_pago_v1.pkl
│
├── src/
│   ├── Cargar_datos.ipynb
│   ├── comprension_eda.ipynb
│   ├── Avance_2_modelado.ipynb
│   ├── ft_engineering.py
│   ├── model_training_evaluation.py
│   ├── model_deploy.py
│   └── model_monitoring.py
│
├── Base_de_datos.xlsx
├── README.md
├── requirements.txt
└── .gitignore