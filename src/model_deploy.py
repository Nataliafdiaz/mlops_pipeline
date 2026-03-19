"""
model_deploy.py

Este módulo será utilizado en avances posteriores para cargar
el modelo entrenado y exponerlo mediante una API o servicio
de inferencia.
"""

import joblib


def load_model(model_path: str = "../models/modelo_pago_v1.pkl"):
    """
    Carga el modelo serializado desde disco.
    """
    model = joblib.load(model_path)
    return model


if __name__ == "__main__":
    model = load_model()
    print("Modelo cargado correctamente para despliegue.")