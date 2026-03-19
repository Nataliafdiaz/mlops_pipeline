import os
import joblib
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def get_models() -> dict:
    """
    Define los modelos base a comparar.
    """
    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ),
        "Decision Tree": DecisionTreeClassifier(
            random_state=42,
            class_weight="balanced"
        ),
        "Random Forest": RandomForestClassifier(
            random_state=42,
            class_weight="balanced",
            n_estimators=200,
            max_depth=10
        )
    }

    return models


def evaluate_models(
    models: dict,
    preprocessor,
    X_train,
    X_test,
    y_train,
    y_test
) -> pd.DataFrame:
    """
    Entrena y evalúa múltiples modelos.
    """
    results = []

    for name, model in models.items():
        clf = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("classifier", model)
        ])

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        if hasattr(clf.named_steps["classifier"], "predict_proba"):
            y_proba = clf.predict_proba(X_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_proba)
        else:
            roc_auc = np.nan

        results.append({
            "Modelo": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred, zero_division=0),
            "Recall": recall_score(y_test, y_pred, zero_division=0),
            "F1-Score": f1_score(y_test, y_pred, zero_division=0),
            "ROC-AUC": roc_auc
        })

    results_df = pd.DataFrame(results).sort_values(by="ROC-AUC", ascending=False)
    return results_df


def fit_final_model(model, preprocessor, X_train, y_train):
    """
    Entrena el pipeline final.
    """
    final_pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", model)
    ])

    final_pipeline.fit(X_train, y_train)
    return final_pipeline


def save_model(model, output_path: str = "../models/modelo_pago_v1.pkl") -> None:
    """
    Guarda el modelo serializado en disco.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(model, output_path)