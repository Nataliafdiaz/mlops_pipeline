# Avance 3 - Monitoreo y Detección de Data Drift

## Objetivos del avance
- Desarrollar una aplicación en Streamlit para visualizar los resultados.
- Documentar el proceso y los principales hallazgos.
- Incorporar una base simple de CI/CD para automatizar validaciones del proyecto.

---

## Descripción del proyecto
Se implementa un sistema de monitoreo de **Data Drift** para detectar cambios entre un dataset de referencia (entrenamiento) y un dataset actual (producción).

El objetivo es asegurar que el modelo no pierda rendimiento cuando los datos cambian con el tiempo.

---

## Tecnologías utilizadas
- Python
- Pandas
- Streamlit
- Evidently AI
- GitHub Actions (CI/CD)

---

## Estructura del proyecto
```text
avance_3/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── referencia.csv
│   └── actual.csv
├── reports/
│   └── drift_summary.csv
├── src/
│   ├── prepare_data.py
│   └── drift.py
├── README.md
├── requirements.txt
└── .gitignore